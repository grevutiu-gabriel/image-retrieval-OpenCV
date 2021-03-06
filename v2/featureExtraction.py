'''
Step 2: Extracting Features from Dataset
1. read in list of filenames for all jpg images in directory
2. write the path and name into database
3. extract features out using the feature descriptor and write feature vectors into database
'''
#!/usr/bin/python
# USAGE:
# python featureExtraction.py --dataset dataset

# import pkgs
import cv2
from FeatureDescriptor import *
from Index import *
import getopt, sys
import os

# parse arguments
try:
    optlist, args = getopt.getopt(sys.argv[1:],'',['dataset='])
    # print optlist, args
except getopt.GetoptError as e:
    print (str(e))
    print 'Usage: %s --dataset path/to/dataset' % sys.argv[0]
    sys.exit(2)

data_dir = ''
for opt, val in optlist:
    if opt == '--dataset':
	data_dir = val
print data_dir
print 

# initialize feature descriptor
# set bin = 16, H= 
feature_descriptor = FeatureDescriptor((8, 12, 3))

# write all images' path into db
index_obj = Index()
index_obj.write_img_path_into_Image(data_dir)

# read in list of filenames for all jpg images in directory
data_list = index_obj.read_img_path_from_Image()

# extract feature for each image in dataset directory and store into db
for f in data_list: 
    img = cv2.imread(f[0]) # read img by dir ./dataset/xxx.png
    imgID = f[1]
    feature = feature_descriptor.describe(img)
	
    # write id, features to output
    index_obj.write_all_features_into_Index(imgID, feature)
