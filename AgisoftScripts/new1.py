# start new project and save as specific unique project name
import os
import PhotoScan as ps

doc = ps.app.document
ps.app.gpu_mask = 15

project_path = ps.app.getSaveFileName('Specify project filename for saving: ')
if not project_path:
    print('Script aborted')

if project_path[-4:].lower() != '.psx':
    project_path += '.psx'


# get folder of NGB photos
path_photos_nir = ps.app.getExistingDirectory('Specify folder with NGB photos: ')
path_photos_nir += '/'

doc.save(project_path)
ps.app.update()

# create 'NGB' chunk and add photos
chunk = doc.addChunk()
chunk.label = 'NGB'
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


# match and align NIR chunk
chunk = doc.chunks[0]
chunk.matchPhotos(
  accuracy = ps.HighAccuracy,
  reference_preselection=False,
  filter_mask = False,
  keypoint_limit=150000, 
  tiepoint_limit=20000)
chunk.alignCameras()
doc.save()
ps.app.update()


# build dense point cloud
chunk.buildDenseCloud(
  quality = ps.MediumAccuracy, # HighAccuracy
  filter = ps.MildFiltering)
doc.save()
ps.app.update()









