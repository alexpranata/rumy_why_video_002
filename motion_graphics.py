#!/usr/bin/env python3
"""Generate lightweight, editable After-Effects-inspired ASS motion graphics.

Offline Python stdlib only. Shapes are editorial annotations, not object tracking.
All coordinates derive from normalized config; manually adjust after inspecting footage.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

YELLOW = '#FFD400'
WHITE = '#F7F9FD'
INK = '#0B1523'


def ass_color(hex_color: str) -> str:
    s = hex_color.removeprefix('#')
    if len(s) != 6 or any(c not in '0123456789abcdefABCDEF' for c in s):
        raise ValueError(f'Expected #RRGGBB, got {hex_color}')
    return '&H00' + s[4:6] + s[2:4] + s[0:2] + '&'


def clock(t: float) -> str:
    cs = round(max(0.0, t) * 100)
    return f'{cs//360000}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}'


def text_safe(value: str) -> str:
    return (str(value).replace('\\', '').replace('{','').replace('}','')
            .replace('\n',' ').replace('\r',' '))


def poly(points: list[tuple[float,float]]) -> str:
    pt = lambda p: f'{round(p[0])} {round(p[1])}'
    return 'm ' + pt(points[0]) + ' l ' + ' '.join(pt(p) for p in points[1:]) + ' ' + pt(points[0])


def bar(x1:float,y1:float,x2:float,y2:float,t:float) -> str:
    dx,dy = x2-x1,y2-y1
    mag = math.hypot(dx,dy) or 1
    nx,ny=-dy/mag*t/2,dx/mag*t/2
    return poly([(x1+nx,y1+ny),(x2+nx,y2+ny),(x2-nx,y2-ny),(x1-nx,y1-ny)])


def arrow(x1:float,y1:float,x2:float,y2:float,thickness=5,head=25) -> str:
    dx,dy=x2-x1,y2-y1
    length=math.hypot(dx,dy) or 1
    ux,uy=dx/length,dy/length
    bx,by=x2-ux*head,y2-uy*head
    nx,ny=-uy,ux
    return (bar(x1,y1,bx,by,thickness) + ' ' +
            poly([(x2,y2),(bx+nx*head*.40,by+ny*head*.40),
                  (bx-nx*head*.40,by-ny*head*.40)]))


def reticle(cx: float,cy:float,r:float,weight=5) -> str:
    paths=[]
    for i in range(4):
        start=math.radians(i*90+9)
        stop=math.radians(i*90+81)
        samples=14
        outer=[];inner=[]
        for k in range(samples+1):
            a=start+(stop-start)*k/samples
            outer.append((cx+math.cos(a)*(r+weight/2),cy+math.sin(a)*(r+weight/2)))
        for k in range(samples,-1,-1):
            a=start+(stop-start)*k/samples
            inner.append((cx+math.cos(a)*(r-weight/2),cy+math.sin(a)*(r-weight/2)))
        paths.append(poly(outer+inner))
    for a in (0,90,180,270):
        theta=math.radians(a)
        paths.append(bar(cx+math.cos(theta)*(r+13),cy+math.sin(theta)*(r+13),
                         cx+math.cos(theta)*(r+29),cy+math.sin(theta)*(r+29),weight))
    return ' '.join(paths)


def bracket(cx:float,cy:float,length:float,vertical:bool,weight=5) -> str:
    d=length/2
    if vertical:
        x1,y1,x2,y2=cx,cy-d,cx,cy+d
        return ' '.join([bar(x1,y1,x2,y2,weight),bar(x1-20,y1,x1+20,y1,weight),
                         bar(x2-20,y2,x2+20,y2,weight)])
    x1,y1,x2,y2=cx-d,cy,cx+d,cy
    return ' '.join([bar(x1,y1,x2,y2,weight),bar(x1,y1-20,x1,y1+20,weight),
                     bar(x2,y2-20,x2,y2+20,weight)])


def event(layer:int,start:float,end:float,style:str,override:str,content:str) -> str:
    if end <= start:
        return ''
    return f'Dialogue: {layer},{clock(start)},{clock(end)},{style},,0,0,0,,{{{override}}}{content}\n'


def validate(config:dict) -> None:
    if config.get('accent_color') != YELLOW:
        raise ValueError(f'Brand accent must be {YELLOW} for this template')
    annotations=config.get('annotations')
    if not isinstance(annotations,list) or len(annotations)!=14:
        raise ValueError('motion_graphics.json must contain 14 annotations')
    if [int(a['scene']) for a in annotations] != list(range(1,15)):
        raise ValueError('annotation scene indices must be ordered 1..14')
    for a in annotations:
        if a.get('type') not in ('reticle','arrow','measure_v','measure_h','underline'):
            raise ValueError(f'Unrecognized overlay type {a.get("type")}')
        for k in ('x','y'):
            if not (0.05 <= float(a[k]) <= 0.95):
                raise ValueError(f'scene {a["scene"]} {k} is outside 5%-95% safe limits')
        for k in ('target_x','target_y'):
            if k in a and not (0.05 <= float(a[k]) <= 0.95):
                raise ValueError(f'scene {a["scene"]} {k} is outside 5%-95% bounds')
        if not str(a.get('label','')).strip():
            raise ValueError(f'scene {a["scene"]} has empty label')


def write_motion_ass(path:Path, config:dict, scenes:list[dict], width:int=1080,
                     height:int=1920, *, with_labels:bool=True) -> None:
    validate(config)
    accent=ass_color(config['accent_color'])
    white=ass_color(WHITE)
    dark=ass_color(INK)
    sx,sy=width/1080,height/1920
    fscale=min(sx,sy)
    header=f'''[Script Info]
Title: RUMY WHY engineering yellow motion graphics
ScriptType: v4.00+
PlayResX: {width}
PlayResY: {height}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Highlight,DejaVu Sans,{round(56*fscale)},{accent},{accent},{dark},&H60000000,-1,0,0,0,100,100,1.4,0,1,{max(1,round(3*fscale))},1,7,40,40,0,1
Style: Micro,DejaVu Sans,{round(27*fscale)},{white},{white},{dark},&H60000000,-1,0,0,0,100,100,1.3,0,1,{max(1,round(2*fscale))},1,7,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
    lines=[header]
    cursor=0.0
    for sc,annotation in zip(scenes,config['annotations']):
        dur=float(sc['target_duration_sec'])
        if dur < 1.2:
            cursor+=dur
            continue
        start=cursor+min(float(annotation.get('enter_sec',0.42)),dur*.2)
        end=cursor+dur-min(float(annotation.get('exit_before_end_sec',0.35)),dur*.12)
        if end <= start+.3:
            cursor+=dur
            continue
        fx=width*float(annotation['x'])
        fy=height*float(annotation['y'])
        typ=annotation['type']
        thickness=max(2,round(5*fscale))
        geometry=''
        if typ=='reticle':
            geometry=reticle(fx,fy,float(annotation.get('radius',90))*fscale,thickness)
        elif typ=='arrow':
            tx,ty=width*float(annotation['target_x']),height*float(annotation['target_y'])
            geometry=arrow(fx,fy,tx,ty,thickness,max(12,round(24*fscale)))
        elif typ=='measure_v':
            geometry=bracket(fx,fy,float(annotation.get('span',390))*sy,True,thickness)
        elif typ=='measure_h':
            geometry=bracket(fx,fy,float(annotation.get('span',400))*sx,False,thickness)
        elif typ=='underline':
            geometry=bar(fx,fy,fx+float(annotation.get('span',290))*sx,fy,thickness)
        # Signature: yellow tech annotation, appears before animated label.
        lines.append(event(2,start,end,'Highlight',
                           f'\\an7\\pos(0,0)\\p1\\bord0\\shad0\\1c{accent}\\fad(220,280)',geometry))
        if with_labels:
            label=text_safe(annotation['label']).upper()
            tx=width*float(annotation.get('label_x',max(.09,float(annotation['x'])-.05)))
            ty=height*float(annotation.get('label_y',max(.12,float(annotation['y'])-.13)))
            # Staggered entry, subtle 22px horizontal motion + yellow highlight.
            label_start=min(end-.32,start+.16)
            if label_start < end:
                ms=min(250,max(70,round((end-label_start)*300)))
                direction=int(22*fscale)
                pos=(f'\\an7\\move({round(tx-direction)},{round(ty)},{round(tx)},{round(ty)},0,{ms})'
                     f'\\fad(170,300)\\1c{accent}\\3c{dark}')
                lines.append(event(3,label_start,end,'Highlight',pos,label))
            micro=annotation.get('micro')
            if micro:
                lines.append(event(3,min(end-.25,start+.30),end,'Micro',
                                   f'\\an7\\pos({round(tx)},{round(ty+64*fscale)})\\fad(240,270)\\1c{white}',
                                   text_safe(micro).upper()))
        cursor+=dur
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(''.join(lines),encoding='utf-8')


def load(path:Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))
