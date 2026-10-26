import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import render

ROOT = Path(__file__).resolve().parents[1]

class RenderHelpers(unittest.TestCase):
    def test_timestamp(self):
        self.assertEqual(render.ass_time(65.22), '0:01:05.22')
        self.assertEqual(render.srt_seconds('00:01:05,220'), 65.22)

    def test_all_scenes(self):
        scenes = json.loads((ROOT/'scenes.json').read_text())['scenes']
        self.assertEqual(len(scenes), 14)
        self.assertEqual([x['id'] for x in scenes], list(range(1,15)))
        self.assertEqual(sum(x['target_duration_sec'] for x in scenes), 70)

    def test_srt(self):
        entries = render.read_srt(ROOT/'captions_rough.srt')
        self.assertEqual(len(entries), 14)
        self.assertEqual(entries[0][0], 0)
        self.assertEqual(entries[-1][1], 70)

    def test_ass_and_filters(self):
        scenes = json.loads((ROOT/'scenes.json').read_text())['scenes']
        captions = render.read_srt(ROOT/'captions_rough.srt')
        with tempfile.TemporaryDirectory() as d:
            dest = Path(d)/'subtitles.ass'
            render.write_ass(dest, captions, scenes, 1080,1920,70)
            self.assertIn('726 FEET', dest.read_text())
            self.assertIn('Dialogue:', dest.read_text())
        graph = render.build_filter(scenes,30,1080,1920,14,None,'_build/captions.ass',70)
        self.assertIn('concat=n=14',graph)
        self.assertIn('[vout]',graph)
        self.assertIn('[aout]',graph)

if __name__=='__main__':
    unittest.main()
