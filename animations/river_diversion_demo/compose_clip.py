"""Add original RUMY WHY typography and encode the local 3D prototype."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import subprocess,math,json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'output/animation_demo'
W,H=1080,1920;YELLOW='#FFD400';WHITE='#F7F9FD';INK='#0B1523'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
def font(size):return ImageFont.truetype(FONT,size)
def smooth(v):v=max(0,min(1,v));return v*v*(3-2*v)
def text_center(d,y,text,size,color=WHITE,stroke=0):
 f=font(size);b=d.textbbox((0,0),text,font=f,stroke_width=stroke)
 d.text(((W-(b[2]-b[0]))/2,y-b[1]),text,font=f,fill=color,stroke_width=stroke,stroke_fill=INK)
def frame(n):
 t=(n-1)/30
 im=Image.new('RGB',(W,H),INK)
 d=ImageDraw.Draw(im)
 # A quiet technical field; no externally sourced textures.
 for x in range(0,W,90):d.line([(x,120),(x,H-120)],fill='#101D2D',width=1)
 for y in range(120,H-120,90):d.line([(0,y),(W,y)],fill='#101D2D',width=1)
 src=Image.open(OUT/f'frames/frame_{n:04}.png').convert('RGBA').resize((W,H),Image.Resampling.LANCZOS)
 im=Image.alpha_composite(im.convert('RGBA'),src).convert('RGB');d=ImageDraw.Draw(im)
 if t<1.8:headline='MOVE THE RIVER';micro='BEFORE BUILDING THE DAM';start=0;caption='The river occupies the worksite.';step=0
 elif t<3.55:headline='4 DIVERSION TUNNELS';micro='TWO THROUGH EACH CANYON WALL';start=1.8;caption='Open a path around the site.';step=1
 elif t<5.0:headline='DIVERT THE FLOW';micro='TEMPORARY COFFERDAMS';start=3.55;caption='Block the old river channel.';step=2
 elif t<6.4:headline='ISOLATE THE WORKSITE';micro='THE RIVER BYPASSES THE CENTER';start=5;caption='Drain the protected work zone.';step=2
 else:headline='DRY WORKSITE';micro='READY FOR EXCAVATION';start=6.4;caption='Now construction can begin.';step=3
 rise=round(20*(1-smooth((t-start)/.3)))
 text_center(d,90,'RUMY WHY  /  ORIGINAL 3D EXPLAINER',26,'#8DA1B7')
 text_center(d,232+rise,headline,68 if len(headline)<20 else 58,YELLOW,2)
 text_center(d,330+rise,micro,29,WHITE,1)
 # Caption placement is separate from the model and upper headlines.
 text_center(d,1595,caption,45,WHITE,3)
 # Four restrained stage markers.
 bar_y=1732
 for k in range(4):
  x=170+k*190;d.rounded_rectangle((x,bar_y,x+155,bar_y+7),radius=3,fill=YELLOW if k<=step else '#27394E')
 text_center(d,1808,'SCHEMATIC CUTAWAY  /  NOT TO SCALE',26,'#8DA1B7')
 text_center(d,1852,'Prototype • no narration • no archival footage',22,'#6C8198')
 return im
files=list((OUT/'frames').glob('frame_*.png'));assert len(files)==240,len(files)
cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-','-an','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart','-metadata','comment=Original procedural 3D schematic; not to scale; no archival footage',str(OUT/'river_diversion_original_3d_demo.mp4')]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for n in range(1,241):
 im=frame(n)
 if n in [20,90,150,230]:im.save(OUT/f'preview_{n:04}.jpg',quality=92)
 p.stdin.write(im.tobytes())
p.stdin.close();assert p.wait()==0
print('Encoded original 3D demo:',OUT/'river_diversion_original_3d_demo.mp4')
