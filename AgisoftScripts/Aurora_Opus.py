# open existing project

import PhotoScan as ps, os
doc = ps.app.document
ps.app.gpu_mask = 65535


project_path = '/mnt/mesos/sandbox/data/Aurora_Opus/ps/AuroraRanch_opus.psx'
if not project_path:
    print('Script aborted')

if project_path[-4:].lower() != '.psx':
    project_path += '.psx'

doc.open(project_path)
doc.save()
ps.app.update()


# # match and align chunks
# for i in range(0, 13):
#   chunk = doc.chunks[i]
#   chunk.matchPhotos(
#     accuracy = ps.HighAccuracy,
#     reference_preselection=False,
#     filter_mask = False,
#     keypoint_limit=150000, 
#     tiepoint_limit=20000)
#   chunk.alignCameras()
# 
# doc.save()
# ps.app.update()


# build dense point cloud
for i in range(0, 13):
  chunk = doc.chunks[i]
  chunk.buildDenseCloud(
    quality = ps.MediumAccuracy, # actually HighAccuracy
    filter = ps.MildFiltering)
	doc.save()
	ps.app.update()


# for i in range(0, 13):
#   chunk = doc.chunks[i]
#   chunk.buildDem(
#     source=ps.DenseCloudData, 
#     interpolation=ps.EnabledInterpolation)
#  
# 
# doc.save()
# ps.app.update()
# 
# for i in range(0, 13):
#   chunk = doc.chunks[i]
#   chunk.buildOrthomosaic(
#     surface=ps.ElevationData, 
#     blending=ps.MosaicBlending, 
#     color_correction=False, 
#     fill_holes=True,
#     projection=chunk.crs)
#     doc.save()
#     ps.app.update()

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


doc.save()
ps.app.update()
print("Script Completed.")
