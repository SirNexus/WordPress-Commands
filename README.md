# WordPress-Commands
This repository contains useful commands for porting a transcription to WordPress

## headers.py

**python <install_dir>/headers.py**

The first file, headers.py, is a file that automatically converts the headers of your post into a WordPress-friendly table of contents that links each element to an included header.

headers.py expects an input file, **input.txt**, to be located in your **Downloads** folder with included headers on each line without spaces.

The output of the code is an **output.txt** which includes the code you can just copy and paste into WordPress

## resize.py

**python <install_dir>/resize.py**

The second file, resize.py, is a file that automatically resizes the images in your **Downloads** directory so that they are less that or equal to 1024 pixels wide. If they are already this size, the program leaves them alone. Also if the files are not an image filetype, the program will leave them alone.

**Note: The program accesses any file in your Downloads directory, including folders. Please make sure that nothing important is getting resized!**
