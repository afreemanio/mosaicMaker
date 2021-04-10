#!/usr/bin/env python3
"""
This is a Python project created for my Winter 2021 Semester at the King's University.
It creates photomosaic images from all images in the "inputImages" folder, based on tiling the specified input on the command line, and saves it to the outputImages folder.
Next steps are to make it look fancier by adding more command line stuff like help, proper argument parsing, etc.
I hope I get a good grade, I worked really hard on this!
Thank you!

"""

__author__ = "Andrew Freeman"
__version__ = "1.0"
__license__ = "MIT"


import os
import time
import sys

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

import averages
import operations


# path of this file
thisPath = os.path.realpath(__file__)
# dir of this file
thisDir = os.path.abspath(os.path.join(thisPath, os.pardir))
# cwd
cwd = os.getcwd()
# parent dir of dir of this file
parentDir = os.path.abspath(os.path.join(thisDir, os.pardir))



# Can change this depending on where its being run, etc...
# where the input images will be located
inputImageDir = parentDir + "\\tileImages"
# for images to be used as tiles for the mosaic
outputImageDir = parentDir + "\\outputImages"
workingImageDir = parentDir + "\\workingImages"
# for images to be used as base for the mosaic
sourceImageDir = parentDir + "\\sourceImages\\"

# output image size in pixels, change this to change resolution of output image
# outputSize = (5000,5000)


def main():
    print("Welcome to mosaicMaker!")

    outputSize = (int(sys.argv[2]), int(sys.argv[3]))
    # get source images from folder
    # TODO: make it so we can choose/specify which ones we want
    print("Now fetching all images from inputImages folder...")
    timeStart = time.perf_counter()
    sourceImagesRaw = operations.arrayOfImagesFromSourceFolder(inputImageDir)
    print("Took " + str(time.perf_counter()-timeStart) + " seconds to complete.")

    # get RGB averages from each source image, store in dictionary
    print("Now getting the average RGB values of all images from source folder...")
    timeStart = time.perf_counter()
    sourceImagesWithAverages = operations.imageDictToDictWithAverages(
        sourceImagesRaw)
    print("Took " + str(time.perf_counter()-timeStart) + " seconds to complete.")

    # choose a base image, can be done in a function or something else
    # baseImageTuple = operations.chooseBaseImage("bart.jpg", inputImageDir)
    baseImageTuple = operations.chooseBaseImage(sys.argv[1], sourceImageDir)

    print("You have chosen your base image as " + str(baseImageTuple.get('name')))
    originalImage = baseImageTuple.get('image')

    # resize image tuple
    baseImageTuple['image'] = baseImageTuple['image'].resize(outputSize)

    # cut base image into a bunch of sections
    baseImageTiles = operations.sliceImageToTiles(
        baseImageTuple.get('image'), int(sys.argv[4]), int(sys.argv[5]))

    # prepare the tiles for reformation
    baseImagePrepared = operations.baseImagePrepare(baseImageTiles)

    # then, what we do is we take base image prepared, sourceImagesWithAverages, and do a function on them by
    # difference of average RGB values to swap every tile in base image prepared with sourceImagesWithAverages

    finalTiles = averages.replacePixelAverages(
        sourceImagesWithAverages, baseImagePrepared)

    # reform tiles into one big image
    reformedImage = operations.reformImageFromTiles(finalTiles)

    # change brightness here:
    # takes original image, output image, makes sure the average brightness is the same
    reformedImage = operations.fixBrightness(originalImage, reformedImage)

    # save it in the output images folder with the set timestamp
    timestr = time.strftime("%Y%m%d-%H%M%S")
    outputDir = os.path.join(outputImageDir, (str(timestr)+".jpg"))
    reformedImage.save(outputDir, "JPEG")



# Ah yes, Python
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    main()