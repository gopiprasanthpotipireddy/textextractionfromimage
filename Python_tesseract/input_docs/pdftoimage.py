import sys
from wand.image import Image as Img
with Img(filename=sys.argv[1], resolution=300) as img:
    img.compression_quality = 99
    img.save(filename=sys.argv[2])


