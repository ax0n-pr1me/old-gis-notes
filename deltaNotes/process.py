from lib import warp as w

imgs1 = w.list_files("data/img/nov23/", "tif")
imgs2 = w.list_files("data/img/dec27/", "tif")

for i in range(0, len(imgs1)):
    w.warp(imgs1[i], imgs2[i])

#works. :)

