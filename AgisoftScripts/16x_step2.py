# open existing project

import PhotoScan as ps, os
doc = ps.app.document
ps.app.gpu_mask = 15

project_path = ps.app.getSaveFileName('Specify project filename for opening: ')
if not project_path:
    print('Script aborted')

if project_path[-4:].lower() != '.psx':
    project_path += '.psx'

doc.open(project_path)
doc.save()
ps.app.update()

# align NIR and RGB chunks, RGB Master
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
  project_path[:-4]+'_ngb_DSM.tif',
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
  project_path[:-4]+'_ngb_ORTHO.tif',
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
print("Script Completed.")



