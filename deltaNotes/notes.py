# Subtract two rasters of different dimensions
# Pixel coordinates define overlap

# Use GDAL to get information about images
# extents are used to align pixels between images
# coords from this method allow querries for future maths

def get_extent(fn):
    '''Returns min_x, max_y, max_x, min_y'''
    ds = gdal.Open(fn)
    gt = ds.GetGeoTransform()
    return (gt[0], gt[3], gt[0] + gt[1] * ds.RasterXSize,
        gt[3] + gt[5] * ds.RasterYSize)

print('extent of warped.tif is %s' % str(get_extent('DSC_0934-warped.tif')))
print('extent of 1636.png is %s' % str(get_extent('DSC_1636.png')))




####################  Section II  ####################

# Example Maths to new Raster
from osgeo import gdal
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *

fileName = "DSC_1636.png"
bandNum1 = 1
bandNum2 = 2

outFile = "out.tiff"

#Open the dataset
ds1 = gdal.Open(fileName, GA_ReadOnly)
band1 = ds1.GetRasterBand(bandNum1)
band2 = ds1.GetRasterBand(bandNum2)

#Read the data into numpy arrays
data1 = BandReadAsArray(band1)
data2 = BandReadAsArray(band2)

#The actual calculation
dataOut = numpy.sqrt(data1*data1+data2*data2)

#Write the out file
driver = gdal.GetDriverByName("GTiff")
dsOut = driver.Create("out.tiff", ds1.RasterXSize, ds1.RasterYSize, 1, band1.DataType)
CopyDatasetInfo(ds1,dsOut)
bandOut=dsOut.GetRasterBand(1)
BandWriteArray(bandOut, dataOut)

#Close the datasets
band1 = None
band2 = None
ds1 = None
bandOut = None
dsOut = None






####################  Section III  ####################
#using Grass (not in conda easily)

import grass.script as grass
import grass.script.array as garray

def map_info(fn):
    map = fn

    # read map
    a = garray.array()
    a.read(map)

    # get raster map info
    print grass.raster_info(map)['datatype']
    i = grass.raster_info(map)
    
    # get computational region info
    c = grass.region()
    print "rows: %d" % c['rows']
    print "cols: %d" % c['cols']

    # new array for result
    b = garray.array()
    # calculate new map from input map and store as GRASS raster map
    b[...] = (a / 50).astype(int) * 50
    b.write("elev.50m")










#    nerve:red_dif axon$ gdalinfo ../tmp/DSC_1636.png
#    Driver: PNG/Portable Network Graphics
#    Files: ../tmp/DSC_1636.png
#    Size is 7380, 4928
#    Coordinate System is `'
#    Image Structure Metadata:
#      INTERLEAVE=PIXEL
#    Corner Coordinates:
#    Upper Left  (    0.0,    0.0)
#    Lower Left  (    0.0, 4928.0)
#    Upper Right ( 7380.0,    0.0)
#    Lower Right ( 7380.0, 4928.0)
#    Center      ( 3690.0, 2464.0)
#    Band 1 Block=7380x1 Type=Byte, ColorInterp=Red
#      Mask Flags: PER_DATASET ALPHA 
#    Band 2 Block=7380x1 Type=Byte, ColorInterp=Green
#      Mask Flags: PER_DATASET ALPHA 
#    Band 3 Block=7380x1 Type=Byte, ColorInterp=Blue
#      Mask Flags: PER_DATASET ALPHA 
#    Band 4 Block=7380x1 Type=Byte, ColorInterp=Alpha
#
#
#    nerve:red_dif axon$ gdalinfo ../tmp/DSC_0934-warped.tif 
#    Driver: GTiff/GeoTIFF
#    Files: ../tmp/DSC_0934-warped.tif
#    Size is 7743, 5507
#    Coordinate System is `'
#    Origin = (-375.383121421060196,692.516776406875124)
#    Pixel Size = (1.080555593255244,-1.080555593255244)
#    Image Structure Metadata:
#      INTERLEAVE=PIXEL
#    Corner Coordinates:
#    Upper Left  (    -375.383,     692.517) 
#    Lower Left  (    -375.383,   -5258.103) 
#    Upper Right (    7991.359,     692.517) 
#    Lower Right (    7991.359,   -5258.103) 
#    Center      (    3807.988,   -2282.793) 
#    Band 1 Block=7743x1 Type=Byte, ColorInterp=Red
#      Mask Flags: PER_DATASET ALPHA 
#    Band 2 Block=7743x1 Type=Byte, ColorInterp=Green
#      Mask Flags: PER_DATASET ALPHA 
#    Band 3 Block=7743x1 Type=Byte, ColorInterp=Blue
#      Mask Flags: PER_DATASET ALPHA 
#    Band 4 Block=7743x1 Type=Byte, ColorInterp=Alpha
