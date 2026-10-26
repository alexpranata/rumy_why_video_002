import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import motion_graphics
import render

class MotionGraphicsTests(unittest.TestCase):
    def setUp(self):
        self.scenes=json.loads((ROOT/'scenes.json').read_text())['scenes']
        self.config=motion_graphics.load(ROOT/'motion_graphics.json')

    def test_exact_yellow_brand(self):
        self.assertEqual(motion_graphics.ass_color('#FFD400'),'&H0000D4FF&')
        motion_graphics.validate(self.config)
        self.assertEqual(len(self.config['annotations']),14)
        self.assertEqual({a['type'] for a in self.config['annotations']},
                         {'reticle','arrow','measure_v','measure_h','underline'})

    def test_invalid_layout(self):
        c=dict(self.config)
        c['accent_color']='#00FFFF'
        with self.assertRaises(ValueError):
            motion_graphics.validate(c)

    def test_ass_has_every_scene(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'graphic.ass'
            motion_graphics.write_motion_ass(p,self.config,self.scenes)
            content=p.read_text()
            self.assertIn('726 FEET', content)
            self.assertIn('4 TUNNELS', content)
            self.assertIn('HOOVER DAM', content)
            # Object graphic coordinates are placeholders, so no yellow shape is drawn before verification.
            self.assertNotIn('\\p1', content)
            self.assertIn('&H0000D4FF&',content)
            self.assertEqual(content.count('\\an8\\move(540,'),14)
            self.assertTrue(content.count('Dialogue:')>=14)

    def test_no_text_labels(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'graphic.ass'
            motion_graphics.write_motion_ass(p,self.config,self.scenes,with_labels=False)
            content=p.read_text()
            self.assertNotIn('726 FEET', content)
            self.assertEqual(content.count('Dialogue:'),0)


    def test_verified_geometry_is_rendered_only_for_selected_scene(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'graphic.ass'
            c=json.loads(json.dumps(self.config))
            c['annotations'][0]['geometry_verified']=True
            motion_graphics.write_motion_ass(p,c,self.scenes)
            content=p.read_text()
            self.assertEqual(content.count('\\p1'),1)
            self.assertIn('\\an8\\move(540,',content)

    def test_graphics_filter(self):
        graph=render.build_filter(self.scenes,30,1080,1920,14,None,
                                  '_build/captions.ass',70,'_build/motion.ass')
        self.assertIn("ass=filename='_build/motion.ass'",graph)
        self.assertIn("ass=filename='_build/captions.ass'",graph)
        self.assertLess(graph.index('_build/motion.ass'),graph.index('_build/captions.ass'))

if __name__=='__main__':
    unittest.main()
