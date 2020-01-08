import piexif
import os
from PIL import Image
import glob

photoList = glob.glob('*tif')

img = Image.open(photoList[0])

exif_dict = piexif.load(photoList[0])

# print all keys with values
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

# print all keys/tags
for ifd in ('0th', 'Exif', 'GPS', 'Interop', '1st'):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], piexif.TAGS[ifd][tag])

# print the ImageDescription text that contains the coordinate data
print(piexif.TAGS['0th'][270]['name'], exif_dict['0th'][270])

