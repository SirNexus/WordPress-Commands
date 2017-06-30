import os
import glob
import re

import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="This program is used to convert "
                                                    "headers into a table of contents")
    parser.add_argument("-f", "--filename", type=str, help="Ex: reedy-conf2016-slide")
    return parser


parser = parse_args()
args = parser.parse_args()
list = []
if len(sys.argv) == 1:
    print parser.print_help()
else:


path = '/home/aidan/Pictures/NGINX/Blog Post/Load Balancing a Dynamic Infrastructure/'
files = os.listdir(path)

#reading from file

i = 0

array = []

with open("headers.txt") as f:
	for line in f:
		line = re.sub(r"\d+:\d+ ", "", line)
		line = re.sub(r"[^a-zA-Z0-9 ]", "", line)
		array.append(line.lower().replace(' ', '-'))
		print array[i]
		i = i + 1
i = 1

for file in sorted(glob.glob('/home/aidan/Pictures/NGINX/Blog Post/Load Balancing a Dynamic Infrastructure/*')):
	print file
	os.rename(os.path.join(path, file), os.path.join(path, "reedy-conf2016-slide" + str(i) + "_" + array[i - 1] + ".png"))
	i = i + 1
