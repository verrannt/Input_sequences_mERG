# Generate input stimuli for mERG recordings and retina modeling
#
# @author Pascal Schröder (Github: verrannt)
# @date   2018/Oct/03
#
# USAGE
# python gen_hex_input *mode* *radius* *output_directory* *output_size*
#   - *mode* is the image type (e.g. RGB or 1 for 1-bit black-white)
#    --> see python pillow documentation on image modes
#   - *radius* is the radius for each hexagon (all have the same)
#   - *size_x* and *size_y* the dimensions of the image
#   - *output_directory* is the directory the images will be saved in
#   - *output_size* is the amount of images to generate
# NOTE
# Make sure the image size is big enough so that all hexagons can be seen
# -----------------------------------------------------------------------------
from PIL import Image, ImageDraw
import sys, math, os, time
import numpy as np

# Helper functions
def create_hexagon(cx,cy, r, g, f, o):
    """
    Create a hexagon of custom location and size
    @params
    cx : x-coordinate
    cy : y-coordinate
    r  : radius
    g  : r/2 * sqrt(3)
    f  : fill-color
    o  : outline-color
    """
    coords = [(0,-r),(-g,-r/2),(-g,r/2),(0,r),(g,r/2),(g,-r/2)]
    coords = [(i[0]+cx,i[1]+cy) for i in coords]
    draw.polygon(coords,fill=f,outline=o)
gen_m = lambda : "black" if np.random.sample() < 0.5 else "white"

# Parameters for all images
im_mode = sys.argv[1]
r = int(sys.argv[2]) # radius of each hexagon
size_x = int(sys.argv[3])
size_y = int(sys.argv[4])
output_dir = sys.argv[5] if sys.argv[5][-1]=="/" else sys.argv[5]+"/"
output_size = int(sys.argv[6])
output_filename_length = len(sys.argv[6])

colored = False # Make this TRUE if you want a beautifully colored image
colors = ["green", "red", "orange", "yellow", "blue", "purple"]
background = "white" if colored else "black"

# Check if output directory exists, if not create it
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

print("Generating images...")
startTime = time.time()
for n in range(output_size):

    # Create new image using python's PIL library
    im = Image.new(mode=im_mode, size=(size_x,size_y), color=background)
    draw = ImageDraw.Draw(im)
    # Coordinates of central pixel
    cx = im.size[0] / 2
    cy = im.size[1] / 2
    # This will be used a lot so we make a variable for it (it's the opposite leg)
    g = r/2 * math.sqrt(3)

    # Ring 1
    c = colors[0] if colored else gen_m()
    create_hexagon(cx, cy, r, g, c, 0)

    # Ring 2
    coords_ring2_1 = [(g, -3/2*r), (-g,-3/2*r), (-2*g, 0)]
    coords_ring2_2 = [(-i[0], -i[1]) for i in coords_ring2_1]
    coords_ring2 = coords_ring2_1 + coords_ring2_2
    for i in coords_ring2:
        c = colors[1] if colored else gen_m()
        create_hexagon(cx+i[0], cy+i[1], r, g, c, 0)

    # Ring 3
    coords_ring3_1 = [(0,-3*r), (2*g, -3*r), (3*g, -3/2*r), (4*g, 0)]
    coords_ring3_2 = [(i[0], -i[1]) for i in coords_ring3_1[:-1]]
    coords_ring3_3 = [(-i[0], i[1]) for i in coords_ring3_1[1:] + coords_ring3_2[1:]]
    coords_ring3 = coords_ring3_1 + coords_ring3_2 + coords_ring3_3
    for i in coords_ring3:
        c = colors[2] if colored else gen_m()
        create_hexagon(cx+i[0], cy+i[1], r, g, c, 0)

    # Ring 4
    coords_ring4_1 = [(g,-9/2*r),(3*g,-9/2*r),(4*g,-3*r),(5*g,-3/2*r),(6*g,0)]
    coords_ring4_2 = [(i[0], -i[1]) for i in coords_ring4_1[:-1]]
    coords_ring4_3 = [(-i[0], i[1]) for i in coords_ring4_1 + coords_ring4_2]
    coords_ring4 = coords_ring4_1 + coords_ring4_2 + coords_ring4_3
    for i in coords_ring4:
        c = colors[3] if colored else gen_m()
        create_hexagon(cx+i[0], cy+i[1], r, g, c, 0)

    # Ring 5
    coords_ring5_1 = [(0,-6*r),(2*g,-6*r),(4*g,-6*r),(5*g,-9/2*r),(6*g,-3*r),(7*g,-3/2*r),(8*g,0)]
    coords_ring5_2 = [(i[0], -i[1]) for i in coords_ring5_1[:-1]]
    coords_ring5_3 = [(-i[0], i[1]) for i in coords_ring5_1[1:] + coords_ring5_2[1:]]
    coords_ring5 = coords_ring5_1 + coords_ring5_2 + coords_ring5_3
    for i in coords_ring5:
        c = colors[4] if colored else gen_m()
        create_hexagon(cx+i[0], cy+i[1], r, g, c, 0)

    # Ring 6
    coords_ring6_1 = [(i[0]+g,i[1]-3/2*r) for i in coords_ring5_1[:3]]
    coords_ring6_2 = [(i[0]+2*g,i[1]) for i in coords_ring5_1[2:]]
    coords_ring6_3 = [(i[0]+4*g,i[1]) for i in coords_ring5_1[2:5]]
    coords_ring6_4 = [(i[0], -i[1]) for i in coords_ring6_1 + coords_ring6_2[:-1] + coords_ring6_3]
    coords_ring6_5 = [(-i[0], i[1]) for i in coords_ring6_1 + coords_ring6_2 + coords_ring6_3 + coords_ring6_4]
    coords_ring6 = coords_ring6_1 + coords_ring6_2 + coords_ring6_3 + coords_ring6_4 + coords_ring6_5
    for i in coords_ring6:
        c = colors[5] if colored else gen_m()
        create_hexagon(cx+i[0], cy+i[1], r, g, c, 0)

    del draw

    im.save("{0}im{1:0{2}d}.png".format(output_dir,n,output_filename_length), format="PNG")
    print("Image {} generated.".format(n))

endTime = time.time()
print("Done. That took {:.3f} milliseconds.".format((endTime-startTime)*1000))
