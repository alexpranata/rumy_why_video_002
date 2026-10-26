"""Original schematic 3D animation. No external models, textures or source footage."""
import bpy,math,random
from mathutils import Vector
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/animation_demo'; OUT.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
s=bpy.context.scene;s.render.engine='BLENDER_WORKBENCH';s.cycles.device='CPU';s.cycles.samples=16;s.cycles.use_denoising=False
s.render.threads_mode='FIXED';s.render.threads=3;s.render.resolution_x=540;s.render.resolution_y=960;s.render.resolution_percentage=100
s.render.fps=30;s.frame_start=1;s.frame_end=240;s.render.image_settings.file_format='PNG';s.render.filepath=str(OUT/'frames/frame_')
s.world.color=(.22,.22,.22)
s.view_settings.view_transform='Standard'
s.display.shading.light='STUDIO';s.display.shading.color_type='MATERIAL';s.display.shading.show_shadows=True;s.display.shading.show_cavity=True;s.display.shading.cavity_type='BOTH'
def mat(name,color,metal=0):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=.7;p.inputs['Metallic'].default_value=metal
 return m
sand=mat('Cutaway sandstone',(.50,.39,.25));rock=mat('Canyon rock',(.62,.48,.30));concrete=mat('Foundation concrete',(.62,.66,.68));base=mat('Midnight plinth',(.027,.045,.064));water=mat('River water',(.035,.36,.46),.15);yellow=mat('Engineering yellow', (1,.72,.003));tunnel=mat('Tunnel lining',(.10,.13,.15))
def cube(name,loc,scale,m,bevel=.08):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(m)
 if bevel:
  mod=o.modifiers.new('Soft machined edges','BEVEL');mod.width=bevel;mod.segments=3;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return o
def curve(name,pts,r,m):
 c=bpy.data.curves.new(name,'CURVE');c.dimensions='3D';c.resolution_u=12;c.bevel_depth=r;c.bevel_resolution=3
 poly=c.splines.new('BEZIER');poly.bezier_points.add(len(pts)-1)
 for b,p in zip(poly.bezier_points,pts):b.co=p;b.handle_left_type='AUTO';b.handle_right_type='AUTO'
 o=bpy.data.objects.new(name,c);bpy.context.collection.objects.link(o);o.data.materials.append(m);return o
cube('Floating diorama base',(0,0,-.38),(9.8,12,.55),base,.18)
for sign in [-1,1]:
 cube('Exposed bank section',(sign*3.0,0,-.03),(3.6,11.5,.25),sand,.10)
 # Deliberately low cutaway walls leave the tunnels visible, not a geographic survey.
 for j in range(7):
  rng=random.Random(j+20+(sign+1)*100)
  cube('Faceted canyon rim',(sign*4.45,-4.8+j*1.6,.25+rng.random()*.25),(.75,1.5,.8+rng.random()*.55),rock,.10)
# Separate water reaches allow the central work area to drain after diversion.
for y,length,name in [(4.15,3.7,'Upstream river'),(-4.15,3.7,'Downstream river')]:cube(name,(0,y,.075),(2.15,length,.13),water,.04)
center=cube('River over future foundation',(0,0,.08),(2.15,4.6,.14),water,.04)
cube('Exposed construction foundation',(0,0,-.045),(2.1,4.5,.09),concrete,.04)
center.scale.z=1;center.keyframe_insert('scale',frame=146);center.scale.z=.001;center.location.z=-.09;center.keyframe_insert('scale',frame=190);center.keyframe_insert('location',frame=190)
center.location.z=.08;center.keyframe_insert('location',frame=146)
paths=[]
for sign in [-1,1]:
 for n in range(2):
  x=2.2+n*.95
  pts=[(sign*1.0,4.45-n*.5,.25),(sign*(x-.3),3.5,.25),(sign*x,1.8,.25),(sign*x,-1.8,.25),(sign*(x-.3),-3.5,.25),(sign*1.0,-4.45+n*.5,.25)]
  outer=curve('Exposed tunnel lining',pts,.19,tunnel)
  inner=curve('Water route / four tunnels',[(x,y,z+.17) for x,y,z in pts],.115,water)
  trace=curve('Yellow route highlight',[(x,y,z+.32) for x,y,z in pts],.023,yellow)
  for o in [outer,inner,trace]:
   o.data.bevel_factor_end=0;o.data.keyframe_insert('bevel_factor_end',frame=55)
   o.data.bevel_factor_end=1;o.data.keyframe_insert('bevel_factor_end',frame=104)
  paths.append((pts,outer))
  # Visible portal collars, four at either end, make branch count readable.
  for point in [pts[0],pts[-1]]:
   bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=6,radius=.20,location=point);o=bpy.context.object;o.name='Schematic tunnel portal';o.scale=(1,1,.55);o.data.materials.append(tunnel)
# Temporary barriers rise only after diversion routes open.
for y in [-2.3,2.3]:
 o=cube('Temporary cofferdam',(0,y,-.35),(2.5,.38,.65),rock,.06)
 o.keyframe_insert('location',frame=119);o.location.z=.27;o.keyframe_insert('location',frame=151)
 cap=cube('Cofferdam yellow marker',(0,y,-.015),(2.55,.40,.045),yellow,.01)
 cap.keyframe_insert('location',frame=119);cap.location.z=.62;cap.keyframe_insert('location',frame=151)
# Animated flow beads on central river (first phase) and each diversion route.
def sampled(obj):
 from mathutils.geometry import interpolate_bezier
 bpy.context.view_layer.update()
 points=obj.data.splines[0].bezier_points
 out=[]
 for a,b in zip(points,points[1:]):
  out.extend(interpolate_bezier(a.co,a.handle_right,b.handle_left,b.co,40)[:-1])
 return out
for index,(pts,path_object) in enumerate(paths):
 path=sampled(path_object)
 for n in range(5):
  bpy.ops.mesh.primitive_uv_sphere_add(segments=8,ring_count=4,radius=.065);o=bpy.context.object;o.name='Flow direction particle';o.data.materials.append(yellow)
  o.hide_render=True;o.keyframe_insert('hide_render',frame=1);o.keyframe_insert('hide_render',frame=102);o.hide_render=False;o.keyframe_insert('hide_render',frame=103)
  for fr in range(103,241,2):
   u=((fr-103)/100+n/5)%1;o.location=path[min(len(path)-1,int(u*(len(path)-1)))]+Vector((0,0,.38));o.keyframe_insert('location',frame=fr)
for n in range(8):
 o=cube('Initial river flow marker',(0,0,.17),(.12,.42,.035),yellow,.01)
 for fr in range(1,148,2):
  o.location.y=5.2-(((fr-1)/110+n/8)%1)*10.4;o.keyframe_insert('location',frame=fr)
 o.hide_render=False;o.keyframe_insert('hide_render',frame=1);o.keyframe_insert('hide_render',frame=145);o.hide_render=True;o.keyframe_insert('hide_render',frame=146)
# Camera drift supplies restrained parallax without making screen overlays target-dependent.
bpy.ops.object.camera_add(location=(5,-18,26));cam=bpy.context.object;cam.rotation_euler=(Vector((0,0,0))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=24.7;s.camera=cam
cam.data.keyframe_insert('ortho_scale',frame=1);cam.data.ortho_scale=23.8;cam.data.keyframe_insert('ortho_scale',frame=240)
for loc,power,size in [((0,-5,15),1800,8),((-8,4,8),1000,7)]:
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=power;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,0))-o.location).to_track_quat('-Z','Y').to_euler()
# Dark, clean composited background.
s.world.use_nodes=True;s.world.node_tree.nodes['Background'].inputs['Color'].default_value=(.08,.11,.16,1);s.world.node_tree.nodes['Background'].inputs['Strength'].default_value=.5
for action in bpy.data.actions:
 for fc in action.fcurves:
  if fc.data_path not in ['hide_render']:
   for k in fc.keyframe_points:k.interpolation='LINEAR'
s.render.film_transparent=True
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'animations/river_diversion_demo/river_diversion.blend'))
s.frame_set(205);s.render.filepath=str(OUT/'design_check.png');bpy.ops.render.render(write_still=True)

s.render.filepath=str(OUT/"frames/frame_");bpy.ops.render.render(animation=True)
