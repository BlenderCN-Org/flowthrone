## Tools for generating groundtruth optical flow using Blender.

Example:

![toy dataset](https://github.com/vasiliykarasev/flowthrone/blob/gh-pages/docs/static/blender_toy_dataset.jpg?raw=true)

Each 2x2 block shows a pair of images (top row) and forward/backward optical flow (bottom row).


A toy dataset like this can be generated using `generate_groundtruth_flow.py` as:

    python generate_groundtruth_examples.py --output_path /tmp/ --num_examples 100

This will write 100 image/flow pairs to `/tmp`. The scene is quite trivial, and 
thes script can just be viewed as an example of obtaining optical flow from Blender.

In brief, this is done by repeatedly calling blender with *another* script
(`blendbox.py`) that generates a pair of images and a pair of EXR files
that contain optical flow (and some other useful data).

## aperitivo

To be able to use modules here, you might need to install:

  * openEXR: `sudo pip install openexr`
  * blender: `sudo apt-get install blender`


