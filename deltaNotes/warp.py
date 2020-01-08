#-------------------------------------------------------------------------------
# Name:        warp.py
# Purpose:     Toolbox to create difference rasters from two instances of multi-temporal imagery
#               Currently, this module only enables warping one image to another based on ORB features.
#               The wdifferencing functionality is a WIP
#
# Author:      JES
#
# Created:     TBD
#-------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import glob
import cv2

# Return sorted lists of images in directory - a weak hack for now.
#   we should be finding by common ITL, but measures of proximity (compare geotags) 
#   or homography (from OpenCV) I have some notes on this elsewhere.

def list_files(directory, extension):
    '''create a sorted list of files with a certain extension
     (photos) in a directory (from a given date when directory is by date)'''
    print('############  Creating sorted list of images in %s ############' % directory)
    print()
    x = glob.glob(directory + '*.' + extension)
    x.sort()
    print('############  Sorted list of images in %s created ############' % directory)
    print()
    return x


## given this result from initial function.... 
#img1_path  = 'data/img/nov23/DSC_1636.png'
#img2_path  = 'data/img/dec27/DSC_0934.png'

def warp(img1_path, img2_path):
    '''warp img2 to img1 using ORB and Harris methods from OpenCV3'''
    
    # Initialize ORB feature match with Harris corner detector
    orb = cv2.ORB_create(edgeThreshold=15, 
                         patchSize=31, 
                         nlevels=8, 
                         fastThreshold=20, 
                         scaleFactor=1.2, 
                         WTA_K=2, 
                         scoreType=cv2.ORB_HARRIS_SCORE, 
                         nfeatures=10000, 
                         #scoreType=cv2.ORB_FAST_SCORE, 
                         firstLevel=0)
    FLANN_INDEX_LSH = 6
    index_params= dict(algorithm = FLANN_INDEX_LSH,
                       table_number = 6, # 12
                       key_size = 12,     # 20
                       multi_probe_level = 1) #2
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # read in images to OpenCV3
    img1 = cv2.imread(img1_path, 0) # Time1 Image
    img2 = cv2.imread(img2_path, 0) # Time2 Image

    # create keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    matches = flann.knnMatch(des1, des2, k=2)
    if len(matches)>0:
        print("%d total matches found" % (len(matches)))
    else:
        print("No matches were found")
        sys.exit()

    # store all the good matches as per Lowe's ratio test
    good = []
    for m_n in matches:
       if len(m_n) != 2:
            continue
       (m,n) = m_n
       if m.distance < 0.6*n.distance:
            good.append(m)
    print('%d good matches remain after filtering' % (len(good)))

    list_kp1 = []
    list_kp2 = []
    for match in good:
        # Get the matching keypoints for each of the images
        img1_idx = match.queryIdx
        img2_idx = match.trainIdx
        # x - columns
        # y - rows
        # Get the coordinates
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt
        # Append to each list
        list_kp1.append((x1, y1))
        list_kp2.append((x2, y2))

    print('length of list_kp1 is %d' % len(list_kp1))
    print()

    print('length of list_kp2 is %d' % len(list_kp2))
    print()

    # call GDAL Translate using keypoints as GCPs between two images
    cmd = "gdal_translate -of GTiff"
    for i in range(0, len(list_kp2)):
        a = str(list_kp2[i][0])
        b = str(list_kp2[i][1])
        c = str(list_kp1[i][0])
        d = "-" + str(list_kp1[i][1])
        cmd += (" -gcp " + a + " " + b + " " + c + " " + d)
    cmd += img2_path
    cmd += " " + img2_path
    cmd += " " + "tmp/unwarped/" + (img2_path.split('/')[3]).split('.')[0] + '_unwarped.' + 'tif'
    #print(cmd) # this is really long but can be usefull once or twice.
    os.system(cmd) # this method is now being discouraged... but still works.

    cmd = "gdalwarp -r bilinear -order 2 -co COMPRESS=NONE -refine_gcps 1.5 650" 
    cmd += " " + "tmp/unwarped/" + (img2_path.split('/')[3]).split('.')[0] + '_unwarped.' + 'tif'
    cmd += " " + "tmp/warp_img/" + (img2_path.split('/')[2]).split('.')[0] + "/" + (img2_path.split('/')[3]).split('.')[0] + '-warped.' + 'tif'
    #print(cmd)
    os.system(cmd)

    cmd = "rm -r tmp/unwarped/*"
    os.system(cmd)

    