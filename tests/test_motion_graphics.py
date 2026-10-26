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
        # Exercise the safe default independently of the reviewed production keys.
        for a in self.config['annotations']:
            a['geometry_verified']=False
            a['label_enabled']=True

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

    def test_selective_titles(self):
        for a in self.config['annotations']:
            a['label_enabled']=False
        self.config['annotations'][0]['label_enabled']=True
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'motion.ass'
            motion_graphics.write_motion_ass(p,self.config,self.scenes)
            text=p.read_text()
            self.assertIn('726 FEET',text)
            self.assertNotIn('BLACK CANYON',text)
            self.assertEqual(text.count('\\an8\\move('),1)

    def test_advanced_flow_is_gated_and_moves(self):
        c=json.loads(json.dumps(self.config));a=c['annotations'][1]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'flow.ass'
            motion_graphics.write_motion_ass(p,c,self.scenes,with_labels=False)
            self.assertNotIn('\\p1',p.read_text())
            a['geometry_verified']=True
            motion_graphics.write_motion_ass(p,c,self.scenes,with_labels=False)
            shapes=[line.split('}',1)[1] for line in p.read_text().splitlines() if '\\p1' in line]
            self.assertGreater(len(shapes),90)
            self.assertGreater(len(set(shapes)),30)

    def test_dimension_count_reaches_published_height(self):
        c=json.loads(json.dumps(self.config));c['annotations'][13]['geometry_verified']=True
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'height.ass'
            motion_graphics.write_motion_ass(p,c,self.scenes,with_labels=False)
            text=p.read_text()
            self.assertIn('726 FT',text)
            self.assertIn('221 m',text)
            self.assertIn('TOTAL HEIGHT',text)
            self.assertIn('\\p1',text)

    def test_mismatched_flow_keys_rejected(self):
        c=json.loads(json.dumps(self.config));c['annotations'][1]['flow_path_keyframes'][1]['points'].pop()
        with self.assertRaises(ValueError):motion_graphics.validate(c)

    def test_centerline_curve_passes_endpoints(self):
        points=[(.2,.3),(.4,.5),(.6,.4)]
        curve=motion_graphics.smooth_path(points)
        for actual,expected in zip(curve[0],points[0]):self.assertAlmostEqual(actual,expected)
        for actual,expected in zip(curve[-1],points[-1]):self.assertAlmostEqual(actual,expected)

    def test_keyframed_geometry_requires_verification(self):
        c=json.loads(json.dumps(self.config))
        a=c['annotations'][10]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'motion.ass'
            motion_graphics.write_motion_ass(p,c,self.scenes)
            self.assertNotIn('\\p1',p.read_text())
            a['geometry_verified']=True
            motion_graphics.write_motion_ass(p,c,self.scenes)
            drawings=[line for line in p.read_text().splitlines() if '\\p1' in line]
            self.assertGreater(len(drawings),30)
            self.assertNotEqual(drawings[10].split('}',1)[1],drawings[-10].split('}',1)[1])

    def test_invalid_key_order(self):
        c=json.loads(json.dumps(self.config))
        c['annotations'][10]['geometry_keyframes'][1]['time_sec']=0
        with self.assertRaises(ValueError):
            motion_graphics.validate(c)

    def test_late_title_is_not_clamped_to_scene_start(self):
        c=json.loads(json.dumps(self.config))
        c['annotations'][0].update(enter_sec=3,hold_sec=1)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'motion.ass'
            motion_graphics.write_motion_ass(p,c,self.scenes)
            first=next(line for line in p.read_text().splitlines() if line.startswith('Dialogue:'))
            self.assertEqual(first.split(',')[1:3],['0:00:03.16','0:00:04.00'])

if __name__=='__main__':
    unittest.main()
