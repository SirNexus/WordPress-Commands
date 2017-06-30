#!/usr/bin/env python
import os
import glob
import shutil
import PIL
from PIL import Image

# path = '/home/aidan/Pictures/NGINX/Blog Post/Load Balancing a Dynamic Infrastructure/'
# files = os.listdir(path)
# truth = ''
# truth = raw_input("\nWould you like to resize all images in the current\ndirectory with width greater than 1024 pixels? (y/n)")
# print "\n"

def backup_image(file):
	if not os.path.exists('./image_backup'):
		os.makedirs('image_backup')
	print "               \t", file
	shutil.copy2(file, './image_backup')

basewidth = 1024

# if truth == "y":
for file in glob.glob('./*'):
	if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg') or file.lower().endswith('.png'):
		img = Image.open(file)
		width, height = img.size
		if (width > 1024):
			backup_image(file)
			wpercent = (basewidth / float(img.size[0]))
			hsize = int((float(img.size[1]) * float(wpercent)))
			img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
			img.save(file)
		else:
			print "not processed: ", file, " width <= 1024"
	else:
		print "not processed: ", file
