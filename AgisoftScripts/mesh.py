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



doc.chunk.buildModel(
  surface=PhotoScan.Arbitrary, 
  interpolation=PhotoScan.EnabledInterpolation, 
  face_count=PhotoScan.HighFaceCount, 
  source=PhotoScan.DenseCloudData)
doc.save()
ps.app.update()

doc.chunk.buildTexture(
  blending=PhotoScan.MosaicBlending, 
  color_correction=True, 
  size=4096)
doc.save()
ps.app.update()



print("Script Completed.")



