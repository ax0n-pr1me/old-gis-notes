# open existing project

import PhotoScan as ps, os
doc = ps.app.document
ps.app.gpu_mask = 255 #15

project_path = '/engineering/graben/GIS/PS/graben.psx'
#project_path = '/home/c3rb3ru5/dataSetName/ps/agisoftProjectName.psx'
if not project_path:
    print('Script aborted')

if project_path[-4:].lower() != '.psx':
    project_path += '.psx'

doc.open(project_path)
doc.save()
ps.app.update()


## # match and align chunks
#for i in range(0, 1):
#  chunk = doc.chunks[i]
#  chunk.matchPhotos(
#    accuracy = ps.HighAccuracy,
#    reference_preselection=True,
#    filter_mask = False,
#    keypoint_limit=150000, 
#    tiepoint_limit=20000)
#  chunk.alignCameras()
#
#doc.save()
#ps.app.update()
#print("Sparse Cloud Completed.")

print()
print()
print("Building Depth Maps")
print()
print()

# build depth maps
for i in range(0, 1):
  chunk = doc.chunks[i]
  chunk.buildDepthMaps(
    quality = ps.MediumQuality, #HighQuality
    filter = ps.AggressiveFiltering)

doc.save()
ps.app.update()
print("Depth Maps Completed.")

print()
print()
print("Building Dense Cloud")
print()
print()



# build dense point cloud
for i in range(0, 1):
  chunk = doc.chunks[i]
  chunk.buildDenseCloud()

doc.save()
ps.app.update()
print("Dense Cloud Completed.")

# merge chunks
#doc.mergeChunks(doc.chunks, merge_dense_clouds=True)


#for i in range(0, 1):
#  chunk = doc.chunks[i]
#  chunk.buildDem(
#    source=ps.DenseCloudData, 
#    interpolation=ps.EnabledInterpolation)
# 
#
#doc.save()
#ps.app.update()
#
#for i in range(0, 1):
#  chunk = doc.chunks[i]
#  chunk.buildOrthomosaic(
#    surface=ps.ElevationData, 
#    blending=ps.MosaicBlending, 
#    color_correction=False, 
#    fill_holes=True,
#    projection=chunk.crs)
#    doc.save()
#    ps.app.update()

# # export DSM
# for i in range(0, 13):
# 	chunk = doc.chunks[i]
# 	chunk.exportDem(
# 		chunk.label +'_DSM.tif',
#   		#format=ps.RasterFormatXYZ,
#   		image_format=ps.ImageFormatTIFF,
#   		#projection=ps.EPSG:4326,
#   		#][, region][, dx][, dy]
#   		# [, blockw][, blockh][, 
#   		nodata = -99999,
#   		write_kml=False,
#   		write_world=False)
# 
# 
# for i in range(0, 13):
# 	chunk = doc.chunks[i]
# 	chunk.exportOrthomosaic(
# 		chunk.label +'_Ortho.tif',
#     	#format=ps.RasterFormatXYZ,
#     	image_format=ps.ImageFormatTIFF,
#     	raster_transform=ps.RasterTransformNone,
#     	#projection=ps.CoordinateSystem,
#     	#[, region ][, dx ]
#     	#[, dy][, blockw][, blockh],
#     	write_kml=False, 
#     	write_world=False, 
#     	write_alpha=False, 
#     	tiff_compression=ps.TiffCompressionNone, 
#     	tiff_big=False, 
#     	jpeg_quality=90)


#doc.save()
#ps.app.update()
#print("Script Completed.")
