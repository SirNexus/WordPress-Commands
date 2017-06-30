# WordPress-Commands
This repository contains useful commands for porting a transcription to WordPress

## headers.py

**python headers.py -f FILENAME**

The first file, headers.py, is a file that automatically converts the headers of your post into a WordPress-friendly table of contents that links each element to an included header.

headers.py expects an input file, denoted with **-f FILENAME**, to be included in the same directory and with included headers on each line without spaces.

The output of the code is an **output.txt** which includes the code you can just copy and paste into WordPress

## resize.py

**python resize.py**

The second file, resize.py, is a file that automatically resizes the images in your current directory so that they are less that or equal to 1024 pixels wide. If they are already this size, the program leaves them alone. Also if the files are not an image filetype, the program will leave them alone.

The program produces an **image_backup** folder in the same directory that holds the images before processing.

## rename.py

**python rename.py**

This file is a work in progress... It includes an absolute path on my home system, so won't work for 99% of test cases. More information to come soon.
