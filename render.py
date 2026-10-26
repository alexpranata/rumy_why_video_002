#!/usr/bin/env python3
"""RUMY WHY Video #002: deterministic offline FFmpeg render.

No AI media generation, downloads, or synthetic substitutions. Python 3 stdlib only.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import motion_graphics

CALL_OUTS = {
    1: "726 FEET", 4: "4 TUNNELS", 5: "NEARLY 3 MILES",
    12: "3.25 MILLION YD³", 13: "1936",
}


def run(cmd: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode:
        tail = '\n'.join((proc.stderr or proc.stdout).splitlines()[-28:])
        raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(cmd[:5])} ...\n{tail}")
    return proc


def probe(path: Path, ffprobe: str) -> dict[str, Any]:
    output = run([ffprobe, '-v', 'error', '-show_entries',
                  'format=duration:stream=codec_type,width,height,r_frame_rate',
                  '-of', 'json', str(path)])
    return json.loads(output.stdout)


def seconds(data: dict[str, Any]) -> float:
    return float(data.get('format', {}).get('duration') or 0)


def ass_time(t: float) -> str:
    cs = max(0, round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02}:{cs // 100 % 60:02}.{cs % 100:02}"


def srt_seconds(s: str) -> float:
    x = re.match(r'^(\d\d):(\d\d):(\d\d)[,.](\d{3})$', s.strip())
    if not x:
        raise ValueError(f'Invalid SRT timestamp: {s}')
    h, m, sec, ms = (int(y) for y in x.groups())
    return h * 3600 + m * 60 + sec + ms / 1000


def read_srt(path: Path) -> list[tuple[float, float, str]]:
    data = path.read_text(encoding='utf-8-sig').strip()
    entries = []
    for block in re.split(r'\r?\n\s*\r?\n', data):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        timing = next((x for x in lines if ' --> ' in x), None)
        if not timing:
            continue
        i = lines.index(timing)
        a, b = timing.split(' --> ', 1)
        entries.append((srt_seconds(a), srt_seconds(b), ' '.join(lines[i+1:])))
    if not entries:
        raise ValueError('No valid caption entries in SRT')
    return entries


def escape_ass(s: str) -> str:
    return s.replace('\\', r'\\').replace('{', r'\{').replace('}', r'\}')


def line_wrap(s: str, n: int = 27) -> str:
    out, current = [], ''
    for w in s.split():
        if current and len(current) + 1 + len(w) > n:
            out.append(current)
            current = w
        else:
            current = f'{current} {w}'.strip()
    if current:
        out.append(current)
    return r'\N'.join(escape_ass(x) for x in out)


def write_ass(path: Path, captions: list[tuple[float, float, str]],
              scenes: list[dict[str, Any]], w: int, h: int, total: float) -> None:
    size = max(19, round(64 * w / 1080))
    c_margin = round(h * .22)
    t_margin = round(h * .24)
    header = f'''[Script Info]
Title: RUMY WHY 002 captions (rough; verify against narration)
ScriptType: v4.00+
PlayResX: {w}
PlayResY: {h}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Narration,DejaVu Sans,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H60000000,-1,0,0,0,100,100,1,0,1,{max(2, round(size*.085))},1,2,{int(w*.075)},{int(w*.075)},{c_margin},1
Style: Callout,DejaVu Sans,{max(17, int(size*1.10))},&H0000E7FF,&H0000E7FF,&H00000000,&H60000000,-1,0,0,0,100,100,1,0,1,{max(2, round(size*.09))},1,8,{int(w*.07)},{int(w*.07)},{t_margin},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
    lines = [header]
    for start, end, content in captions:
        start, end = max(0, start), min(total, end)
        if end > start:
            lines.append(f'Dialogue: 0,{ass_time(start)},{ass_time(end)},Narration,,0,0,0,,{line_wrap(content)}\n')
    at = 0.0
    for sc in scenes:
        d = float(sc['target_duration_sec'])
        label = CALL_OUTS.get(int(sc['id']))
        if label and d > .9:
            a, b = at + d*.2, at + min(d*.78, d*.2+2.7)
            lines.append(f'Dialogue: 1,{ass_time(a)},{ass_time(b)},Callout,,0,0,0,,{escape_ass(label)}\n')
        at += d
    path.write_text(''.join(lines), encoding='utf-8')


def ffmpeg_filter_path(s: str) -> str:
    # Forward slashes and relative paths only; quote filtergraph metacharacters.
    return s.replace('\\', '/').replace(':', r'\:').replace("'", r"\'").replace(',', r'\,').replace('[', r'\[').replace(']', r'\]')


def build_filter(scenes: list[dict[str, Any]], fps: int, w: int, h: int,
                 voice_index: int, music_index: int | None, ass: str | None,
                 total: float, graphics_ass: str | None = None) -> str:
    filters = []
    for i, sc in enumerate(scenes):
        dur = float(sc['target_duration_sec'])
        offset = float(sc.get('trim_start_sec', 0))
        base = (f'[{i}:v]trim=start={offset:.4f}:duration={dur:.4f},'
                f'setpts=PTS-STARTPTS,fps={fps},'
                f'scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,'
                f'crop={w}:{h},setsar=1')
        motion = sc.get('camera_motion', '').lower()
        # Mild editorial zooms on top of the already animated footage; no effects on tracking/pans.
        if 'zoom' in motion or 'punch' in motion:
            if 'zoom out' in motion or 'pull back' in motion:
                zoom = f"max(1.0,1.095-on*{.095/max(1, dur*fps-1):.8f})"
            else:
                zoom = f"min(1.095,1.0+on*{.095/max(1, dur*fps-1):.8f})"
            base += (f",zoompan=z='{zoom}':d=1:"
                     f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={w}x{h}:fps={fps}")
        base += f',trim=duration={dur:.4f},setpts=PTS-STARTPTS,format=yuv420p[v{i}]'
        filters.append(base)
    filters.append(''.join(f'[v{i}]' for i in range(len(scenes))) + f'concat=n={len(scenes)}:v=1:a=0[joined]')
    current = 'joined'
    if graphics_ass:
        filters.append(f"[{current}]ass=filename='{ffmpeg_filter_path(graphics_ass)}'[withgraphics]")
        current = 'withgraphics'
    if ass:
        filters.append(f"[{current}]ass=filename='{ffmpeg_filter_path(ass)}'[vout]")
    else:
        filters.append(f'[{current}]null[vout]')
    filters.append(f'[{voice_index}:a]aresample=48000,volume=1.0,apad,atrim=duration={total:.3f},asetpts=PTS-STARTPTS[vo]')
    if music_index is not None:
        fade_start = max(0.0, total-2.0)
        filters.append(f'[{music_index}:a]aresample=48000,volume=0.09,atrim=duration={total:.3f},'
                       f'afade=t=in:st=0:d=1,afade=t=out:st={fade_start:.3f}:d=2,asetpts=PTS-STARTPTS[mus]')
        filters.append('[vo][mus]amix=inputs=2:duration=first:dropout_transition=0,'
                       'alimiter=limit=0.89[aout]')
    else:
        filters.append('[vo]alimiter=limit=0.89[aout]')
    return ';'.join(filters)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description='Render RUMY WHY Hoover Dam short from existing Google Flow media.')
    ap.add_argument('--project', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--video-dir', type=Path, default=Path('assets/video'))
    ap.add_argument('--voice', type=Path, default=Path('assets/audio/voiceover.wav'))
    ap.add_argument('--music', type=Path, default=Path('assets/audio/music.mp3'))
    ap.add_argument('--output', type=Path, default=Path('output/rumy_why_002.mp4'))
    ap.add_argument('--srt', type=Path, default=Path('captions_rough.srt'))
    ap.add_argument('--check', action='store_true', help='Validate structure and list missing media (returns success).')
    ap.add_argument('--no-captions', action='store_true')
    ap.add_argument('--no-callouts', action='store_true')
    ap.add_argument('--no-graphics', action='store_true', help='Disable animated yellow motion graphics.')
    ap.add_argument('--graphics-config', type=Path, default=Path('motion_graphics.json'))
    ap.add_argument('--width', type=int, default=1080)
    ap.add_argument('--height', type=int, default=1920)
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--crf', type=int, default=20)
    ap.add_argument('--preset', default='medium', choices=('ultrafast','superfast','veryfast','faster','fast','medium','slow'))
    ap.add_argument('--ffmpeg', default='ffmpeg')
    ap.add_argument('--ffprobe', default='ffprobe')
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    project = args.project.resolve()
    relative = lambda p: p if p.is_absolute() else project / p
    scene_path = project / 'scenes.json'
    if not scene_path.exists():
        raise FileNotFoundError(f'Missing scenes.json at {scene_path}. Unzip entire project folder.')
    data = json.loads(scene_path.read_text(encoding='utf-8'))
    scenes = data.get('scenes', [])
    if len(scenes) != 14 or [int(s['id']) for s in scenes] != list(range(1,15)):
        raise ValueError('scenes.json must contain 14 ordered scenes with ids 1..14')
    if any(float(s['target_duration_sec']) <= 0 or float(s.get('trim_start_sec',0)) < 0 for s in scenes):
        raise ValueError('Each target_duration_sec must be positive and trim_start_sec nonnegative')
    total = sum(float(s['target_duration_sec']) for s in scenes)
    video_dir, voice, music, output, srt, graphics_config = [relative(x) for x in (args.video_dir,args.voice,args.music,args.output,args.srt,args.graphics_config)]
    videos = [video_dir / str(s['clip_filename']) for s in scenes]
    missing = [str(p.relative_to(project) if p.is_relative_to(project) else p) for p in [*videos, voice] if not p.is_file()]
    ffmpeg, ffprobe = shutil.which(args.ffmpeg), shutil.which(args.ffprobe)
    issues = []
    if not ffmpeg or not ffprobe:
        issues.append('Install FFmpeg and FFprobe and make sure both are on PATH.')
    if not args.no_graphics:
        if not graphics_config.is_file():
            issues.append(f'Motion graphics config missing: {graphics_config}')
        else:
            try:
                motion_graphics.validate(motion_graphics.load(graphics_config))
            except (ValueError, json.JSONDecodeError, KeyError) as exc:
                issues.append(f'Motion graphics config invalid: {exc}')
    if not args.no_captions or not args.no_graphics:
        if not args.no_captions and not srt.is_file():
            issues.append(f'Caption file missing: {srt}')
        elif ffmpeg:
            filters = run([ffmpeg,'-hide_banner','-filters']).stdout
            if not re.search(r'\bass\b', filters):
                issues.append('FFmpeg is missing the libass subtitle filter. Install FFmpeg with --enable-libass or use --no-captions.')
    print(f'Project: {project}\nScenes: {len(scenes)} | target duration: {total:.2f}s | export: {args.width}x{args.height} @{args.fps}fps')
    print('FFmpeg:', ffmpeg or 'NOT FOUND')
    print('Optional music:', str(music) if music.exists() else 'not supplied (skipped)')
    print('Yellow motion graphics:', 'OFF' if args.no_graphics else str(graphics_config))
    if missing:
        print(f'\nMissing source media ({len(missing)}):')
        for name in missing:
            print('  -',name)
    for issue in issues:
        print('WARNING:',issue)
    if args.check:
        print('\nCHECK ONLY: no video render attempted. Add files and run without --check.')
        return 0
    if missing or issues:
        print('\nCannot render: supply existing source media / fix issues and retry.', file=sys.stderr)
        return 2
    if args.width < 120 or args.height < 120 or args.width%2 or args.height%2 or args.fps < 1:
        raise ValueError('Width/height must be even >=120 and FPS >=1')
    details = []
    for sc, path in zip(scenes, videos):
        meta = probe(path, ffprobe)
        length = seconds(meta)
        start = float(sc.get('trim_start_sec',0))
        duration = float(sc['target_duration_sec'])
        if length+0.05 < start+duration:
            raise ValueError(f'{path.name} is {length:.2f}s; requires at least {start+duration:.2f}s. Adjust trim_start_sec or generate a longer clip.')
        if not any(s.get('codec_type')=='video' for s in meta.get('streams',[])):
            raise ValueError(f'{path.name} contains no video stream')
        details.append({'scene':sc['id'],'path':str(path),'source_duration_sec':round(length,3),
                        'trim_start_sec':start,'trim_end_sec':start+duration,'timeline_duration_sec':duration,
                        'camera_motion':sc.get('camera_motion','')})
    voice_meta = probe(voice, ffprobe)
    voice_len = seconds(voice_meta)
    if not any(s.get('codec_type')=='audio' for s in voice_meta.get('streams',[])):
        raise ValueError(f'Voiceover contains no audio stream: {voice}')
    if voice_len > total+0.25:
        raise ValueError(f'Voiceover length {voice_len:.2f}s exceeds timeline {total:.2f}s. Retime scenes or rerecord voiceover; script will not cut narration.')
    warnings = ['captions_rough.srt is scene-timed and not word-aligned. Review voice and subtitle sync manually.']
    if voice_len < total-2:
        warnings.append(f'Voiceover ends {total-voice_len:.1f}s before video end; trailing section will be silent except optional music.')
    if not args.no_graphics:
        warnings.append('Animated annotations are editorial placements, not object tracked. Check that arrows/rings point at visible features.')
    if not music.exists():
        warnings.append('No licensed music file found; voiceover-only audio will be rendered.')
    output.parent.mkdir(parents=True,exist_ok=True)
    staging = project/'_build'
    staging.mkdir(exist_ok=True)
    ass_name = None
    motion_name = None
    if not args.no_graphics:
        motion_graphics.write_motion_ass(staging/'motion.ass', motion_graphics.load(graphics_config), scenes,
                                          args.width, args.height, with_labels=not args.no_callouts)
        motion_name = '_build/motion.ass'
    if not args.no_captions:
        captions = read_srt(srt)
        global CALL_OUTS
        if args.no_callouts or motion_name:
            CALL_OUTS = {}  # Avoid duplicated statistics when animated graphics already show them.
        write_ass(staging/'captions.ass',captions,scenes,args.width,args.height,total)
        ass_name = '_build/captions.ass'
    cmd = [ffmpeg,'-hide_banner','-y']
    for path in videos:
        cmd += ['-i',str(path)]
    voice_index = len(videos)
    cmd += ['-i',str(voice)]
    music_index = None
    if music.is_file():
        music_index = voice_index+1
        cmd += ['-stream_loop','-1','-i',str(music)]
    cmd += ['-filter_complex',build_filter(scenes,args.fps,args.width,args.height,
                  voice_index,music_index,ass_name,total,motion_name),
            '-map','[vout]','-map','[aout]',
            '-c:v','libx264','-preset',args.preset,'-crf',str(args.crf),'-pix_fmt','yuv420p',
            '-r',str(args.fps),'-c:a','aac','-b:a','192k','-ar','48000',
            '-t',f'{total:.3f}','-movflags','+faststart',
            '-metadata','title=RUMY WHY - How Engineers Built Hoover Dam',
            '-metadata','comment=AI-generated historical reconstruction; not archival footage',
            str(output)]
    print(f'\nRendering to: {output}', flush=True)
    run(cmd,cwd=project)
    out_meta = probe(output,ffprobe)
    report = {'project':data.get('project'),'output':str(output),'output_duration_sec':round(seconds(out_meta),3),
              'target_duration_sec':total,'voice_duration_sec':round(voice_len,3),
              'dimensions':f'{args.width}x{args.height}','fps':args.fps,'clips':details,'warnings':warnings,
              'captions': 'rough SRT burned in' if ass_name else 'off', 'music_used':music.is_file(),
              'motion_graphics': 'yellow ASS overlays' if motion_name else 'off',
              'motion_graphics_config': str(graphics_config) if motion_name else None,
              'annotation_warning': 'Positions are not tracked: verify every arrow, ring, and bracket against real footage.' if motion_name else None}
    report_path=output.parent/'render_report.json'
    report_path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'SUCCESS: {output}\nReport: {report_path}')
    for w in warnings:
        print('REVIEW:',w)
    return 0


if __name__=='__main__':
    try:
        sys.exit(main())
    except (OSError,ValueError,RuntimeError,json.JSONDecodeError) as e:
        print(f'ERROR: {e}',file=sys.stderr)
        sys.exit(2)
