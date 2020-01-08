# start new project and save as specific unique project name
import os
import PhotoScan as ps
doc = ps.app.document
ps.app.gpu_mask = 3

project_path = ps.app.getSaveFileName('Specify project filename for saving: ')
if not project_path:
    print('Script aborted')

if project_path[-4:].lower() != '.psx':
    project_path += '.psx'

doc.save(project_path)
ps.app.update()

# get folder of RGB photos
path_photos_rgb = ps.app.getExistingDirectory('Specify folder with RGB photos: ')
path_photos_rgb += '/'

# get folder of NIR photos
path_photos_nir = ps.app.getExistingDirectory('Specify folder with NIR photos: ')
path_photos_nir += '/'

# create 'RGB' chunk and add photos
chunk = doc.addChunk()
chunk.label = 'RGB'
image_list = os.listdir(path_photos_rgb)
photo_list = list()

for photo in image_list:
    if photo.rsplit('.',1)[1].upper() in ['JPG', 'JPEG', 'TIF', 'PNG', 'TIFF']:
           photo_list.append(path_photos_rgb + photo)
           print(photo)
    else:
           print('No photo available.')

chunk.addPhotos(photo_list)
doc.save()
ps.app.update()

# create 'NIR' chunk and add photos
chunk = doc.addChunk()
chunk.label = 'NIR'
image_list = os.listdir(path_photos_nir)
photo_list = list()

for photo in image_list:
    if photo.rsplit('.',1)[1].upper() in ['JPG', 'JPEG', 'TIF', 'PNG', 'TIFF']:
           photo_list.append(path_photos_nir + photo)
           print(photo)
    else:
           print('No photo available.')

chunk.addPhotos(photo_list)
doc.save()
ps.app.update()


# match and align RGB chunk
chunk = doc.chunks[0]
chunk.matchPhotos(
  accuracy = ps.HighAccuracy,
  reference_preselection=True,
  filter_mask = False,
  keypoint_limit=150000, 
  tiepoint_limit=20000)
chunk.alignCameras()
doc.save()
ps.app.update()


# match and align NIR chunk
chunk = doc.chunks[1]
chunk.matchPhotos(
  accuracy = ps.HighAccuracy,
  reference_preselection=True,
  filter_mask = False,
  keypoint_limit=150000, 
  tiepoint_limit=20000)
chunk.alignCameras()
doc.save()
ps.app.update()


# align NIR and RGB chunks
doc.alignChunks(doc.chunks, 
  doc.chunks[0], 
  method='points', 
  fix_scale=False, 
  accuracy=ps.HighAccuracy, 
  preselection=False, 
  filter_mask=False, 
  point_limit=100000
  )
doc.save()
ps.app.update()

# for RGB Chunk
chunk = doc.chunks[0]
# build dense point cloud
chunk.buildDenseCloud(
  quality = ps.MediumAccuracy,
  filter = ps.MildFiltering)
doc.save()
ps.app.update()

# for NIR Chunk
chunk = doc.chunks[1]
# build dense point cloud
chunk.buildDenseCloud(
  quality = ps.MediumAccuracy,
  filter = ps.MildFiltering)
doc.save()
ps.app.update()

# For RGB Chunk
chunk = doc.chunks[0]

# build DSM
chunk.buildDem(
  source=ps.DenseCloudData, 
  interpolation=ps.EnabledInterpolation)
doc.save()
ps.app.update()

# build Orthophoto
chunk.buildOrthomosaic(
  surface=ps.ElevationData, 
  blending=ps.MosaicBlending, 
  color_correction=False, 
  fill_holes=True,
  projection=chunk.crs, 
  # ][, region ][, dx ][, dy ][, progress ]
  )
doc.save()
ps.app.update()

# export DSM
chunk.exportDem(
  project_path[:-4]+'_rgb_DSM.tif',
  #format=ps.RasterFormatXYZ,
  image_format=ps.ImageFormatTIFF,
  #projection=ps.EPSG:4326,
  #][, region][, dx][, dy]
  # [, blockw][, blockh][, 
  nodata = -99999,
  write_kml=False,
  write_world=False)

# export Orthophoto
chunk.exportOrthomosaic(
  project_path[:-4]+'_rgb_ORTHO.tif',
  #format=ps.RasterFormatXYZ,
  image_format=ps.ImageFormatTIFF,
  raster_transform=ps.RasterTransformNone,
  #projection=ps.CoordinateSystem,
  #[, region ][, dx ]
  #[, dy][, blockw][, blockh],
  write_kml=False, 
  write_world=False, 
  write_alpha=False, 
  tiff_compression=ps.TiffCompressionNone, 
  tiff_big=False, 
  jpeg_quality=90)


# for NIR Chunk
chunk = doc.chunks[1]

# build DSM
chunk.buildDem(
  source=ps.DenseCloudData, 
  interpolation=ps.EnabledInterpolation)
doc.save()
ps.app.update()

# build Orthophoto
chunk.buildOrthomosaic(
  surface=ps.ElevationData, 
  blending=ps.MosaicBlending, 
  color_correction=False, 
  fill_holes=True,
  projection=chunk.crs,
  # ][, region ][, dx ][, dy ][, progress ]
  )
doc.save()
ps.app.update()

# export DSM
chunk.exportDem(
  project_path[:-4]+'_nir_DSM.tif',
  #format=ps.RasterFormatXYZ,
  image_format=ps.ImageFormatTIFF,
  #projection=ps.EPSG:4326,
  #][, region][, dx][, dy]
  # [, blockw][, blockh][, 
  nodata = -99999,
  write_kml=False,
  write_world=False)

# export Orthophoto
chunk.exportOrthomosaic(
  project_path[:-4]+'_nir_ORTHO.tif',
  #format=ps.RasterFormatXYZ,
  image_format=ps.ImageFormatTIFF,
  raster_transform=ps.RasterTransformNone,
  #projection=ps.CoordinateSystem,
  #[, region ][, dx ]
  #[, dy][, blockw][, blockh],
  write_kml=False, 
  write_world=False, 
  write_alpha=False, 
  tiff_compression=ps.TiffCompressionNone, 
  tiff_big=False, 
  jpeg_quality=90)

doc.save()
ps.app.update()
print("Script Completed. Layers saved at " + project_path[:-4])
