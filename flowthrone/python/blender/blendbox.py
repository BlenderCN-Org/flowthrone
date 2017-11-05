"""
This script generates a simple scene in blender and renders a pair of images,
and a pair of EXR files. It is meant to be passed into blender, like so:
    blender --background --factory-startup --python blendbox.py -- \
            --filepath /tmp/ --pose1 0,10,0 --pose2 0,11,0 
this will generate 4 files:
    /tmp/0001.exr
    /tmp/0002.exr
    /tmp/0001.jpg
    /tmp/0002.jpg
containing images of a scene with a camera at (0,0,0), and a cube at
(0,10,0) and (0,11,0). The exr's will also contain opticalflow.

If you are interested in interacting with Blender GUI, call the script as:
    blender --python blendbox.py -- \
            --filepath /tmp/ --pose1 0 10 0 --pose2 0 11 0 --no-clear
"""

import bpy
from math import pi
import random
import sys

def main():
  import sys
  import argparse
  parser = argparse.ArgumentParser(description='Read source to see how to run')
  parser.add_argument('--filepath', default='/tmp/', \
                      help='Where the images/exrs are saved')
  parser.add_argument('--pose1', default=[0, 5, 0], type=float, nargs=3, \
                      help='cube location at t')
  parser.add_argument('--pose2', default=[0, 6, 0], type=float, nargs=3, \
                      help='cube location at t+1')
  parser.add_argument('--no-clear', action='store_true', default=False,
                      help='if true, will not clear scene at the end. This is '
                           'only useful if you are using blender GUI')
  parser.add_argument('--image_size', default=128, type=int, help='image size')
  parser.add_argument('--scale', default=[1, 1], type=float, nargs=2, \
                      help='Scale of the rectangle.')

  args = parser.parse_args(get_args())
  ## Reinterpret as a 3-vector
  args.pose1 = tuple(args.pose1)
  args.pose2 = tuple(args.pose2)
  args.scale = tuple(args.scale)
  generate_scene(args)

def get_args():
  if "--" not in sys.argv:
    return []
  else:
    return sys.argv[sys.argv.index("--") + 1:]

def delete_all_objects(bpy):
  """ Deletes all existing objects. """
  for obj in bpy.data.objects:
    obj.select = True
  bpy.ops.object.delete()

def create_lamp(bpy, position):
  """ Create a point lamp. """
  lamp_data = bpy.data.lamps.new(name="lamp", type='POINT')
  lamp_object = bpy.data.objects.new(name="lamp", object_data=lamp_data)
  lamp_object.select = True
  lamp_object.location = position
  bpy.context.scene.objects.link(lamp_object)
  bpy.context.scene.objects.active = lamp_object

def create_camera(bpy, location, rotation):
  """ Create a camera at specified position/orientation """
  cam_data = bpy.data.cameras.new(name="camera")
  cam_object = bpy.data.objects.new(name="camera", object_data=cam_data)
  cam_object.select = True
  cam_object.location = location
  cam_object.rotation_euler = rotation
  bpy.context.scene.objects.link(cam_object)
  bpy.context.scene.objects.active = cam_object
  bpy.context.scene.camera = cam_object

def add_texture(bpy, ob):
  mtex = ob.data.materials[0].texture_slots.add()
  mtex.texture = get_clouds_texture()

def get_clouds_texture():
  tex = bpy.data.textures.new('ColorTex', type = 'CLOUDS')
  tex.noise_scale = random.uniform(0.1, 0.5)
  tex.noise_depth = random.uniform(5.0, 10.0)
  tex.nabla = random.uniform(1.0, 1.0)
  tex.contrast = random.uniform(1.0, 10.0)
  tex.cloud_type = 'COLOR'
  tex.factor_red = random.uniform(0.0, 1.0)
  tex.factor_green = random.uniform(0.0, 1.0)
  tex.factor_blue = random.uniform(0.0, 1.0)
  return tex

def create_cube(bpy, location, scale, rotation):
  ob = bpy.data.objects.get("cube")
  if not ob:
    bpy.ops.mesh.primitive_cube_add()
    ob = bpy.context.object
  ob.name = "cube"
  mat = bpy.data.materials.new("cube_material")
  ob.data.materials.append(mat)
  set_cube_pose(location, scale, rotation)

def set_cube_pose(location, scale, rotation):
  ob = bpy.data.objects.get("cube")
  ob.location = location
  ob.rotation_euler = rotation
  ob.scale = scale

def generate_scene(args):
  cube_scale = (args.scale[0], 0.001, args.scale[1])
  cube_rotation = (0.0, 0.0, 0.0)
  camera_position = (0, 0, 0)
  camera_rotation = (pi/2, 0, 0)
  lamp_position = (0.0, 2.5, 5.0)
  image_size = (args.image_size, args.image_size)
  delete_all_objects(bpy)
  bpy.context.scene.frame_current = 0
  create_camera(bpy, camera_position, camera_rotation)
  create_lamp(bpy, lamp_position)
  create_cube(bpy, args.pose1, cube_scale, cube_rotation)
  cube = bpy.data.objects.get("cube")
  add_texture(bpy, cube)

  bpy.context.scene.frame_start = 0
  bpy.context.scene.frame_end = 1
  bpy.context.scene.frame_current = 0
  bpy.context.scene.update()
  bpy.context.scene.objects.active = None

  bpy.context.scene.frame_current = 0
  set_cube_pose(args.pose1, cube_scale, cube_rotation)
  cube.keyframe_insert('location', group='LocRotScale', frame=0)
  
  bpy.context.scene.frame_current = 1
  set_cube_pose(args.pose2, cube_scale, cube_rotation)
  cube.keyframe_insert('location', group='LocRotScale', frame=1)
  bpy.context.scene.update()
  bpy.context.scene.objects.active = None
  kf = bpy.data.objects['cube'].animation_data.action.fcurves[0].keyframe_points[0]
  kf.interpolation = 'CONSTANT'
  # Create sky:
  bpy.data.worlds[0].use_sky_blend = True
  bpy.data.worlds[0].use_sky_paper = True
  bpy.data.worlds[0].use_sky_real = True
  bpy.data.worlds[0].horizon_color = ((random.uniform(0, 0.5),
                                       random.uniform(0, 0.5),
                                       random.uniform(0, 0.5)))
  bpy.data.worlds[0].zenith_color  = ((random.uniform(0, 0.5),
                                       random.uniform(0, 0.5),
                                       random.uniform(0, 0.5)))
  bpy.data.worlds[0].ambient_color = ((random.uniform(0, 0.5),
                                       random.uniform(0, 0.5),
                                       random.uniform(0, 0.5)))
  slot = bpy.data.worlds[0].texture_slots.add()
  slot.texture = get_clouds_texture()
  # Set render options.
  bpy.context.scene.render.resolution_x = image_size[0]
  bpy.context.scene.render.resolution_y = image_size[1]
  bpy.context.scene.render.resolution_percentage = 100.0
  bpy.context.scene.render.filepath = args.filepath
  
  bpy.context.scene.render.layers['RenderLayer'].use_pass_vector = True
  bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR_MULTILAYER'
  bpy.ops.render.render(animation=True)
  bpy.context.scene.render.image_settings.file_format = 'JPEG'
  bpy.ops.render.render(animation=True)
  if not args.no_clear:
      delete_all_objects(bpy)

if __name__ == "__main__":
  main() 
