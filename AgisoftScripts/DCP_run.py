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

# match and align chunk[1]
chunk = doc.chunks[1]
chunk.matchPhotos(
  accuracy = ps.HighAccuracy,
  reference_preselection=False,
  filter_mask = False,
  keypoint_limit=40000, 
  tiepoint_limit=4000)
chunk.alignCameras()
doc.save()
ps.app.update()

# match and align chunk[2]
chunk = doc.chunks[2]
chunk.matchPhotos(
  accuracy = ps.HighAccuracy,
  reference_preselection=False,
  filter_mask = False,
  keypoint_limit=40000, 
  tiepoint_limit=4000)
chunk.alignCameras()
doc.save()
ps.app.update()

# match and align chunk[3]
chunk = doc.chunks[3]
chunk.matchPhotos(
  accuracy = ps.HighAccuracy,
  reference_preselection=False,
  filter_mask = False,
  keypoint_limit=40000, 
  tiepoint_limit=4000)
chunk.alignCameras()
doc.save()
ps.app.update()

# align all chunks, doc.chunk[0] Master
doc.alignChunks(doc.chunks, 
  doc.chunks[0], 
  method='points', 
  fix_scale=False, 
  accuracy=ps.HighAccuracy, 
  preselection=False, 
  filter_mask=False, 
  point_limit=10000
  )
doc.save()
ps.app.update()

################################################################

# for Chunk[1]
chunk = doc.chunks[1]

# build DSM
chunk.buildDem(
  source=ps.PointCloudData, 
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

# for Chunk[2]
chunk = doc.chunks[2]

# build DSM
chunk.buildDem(
  source=ps.PointCloudData, 
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

# for Chunk[3]
chunk = doc.chunks[3]

# build DSM
chunk.buildDem(
  source=ps.PointCloudData, 
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

