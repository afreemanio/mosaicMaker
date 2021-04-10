from PIL import Image, ImageEnhance
import os
import os.path
from statistics import mean
import numpy as np
import time
from tqdm import tqdm


def arrayOfImagesFromSourceFolder(sourcedir):

    imgs = []
    valid_images = [".jpg", ".png"]
    for f in tqdm(os.listdir(sourcedir)):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        d = {'name': f, 'image': Image.open(os.path.join(sourcedir, f))}
        imgs.append(d)
    # #to show all images
    # for image in imgs:
    #     image.show()
    # print(str(imgs))
    return imgs


# i guess what we should do here is unshape and reshape the array (if it can)
# nono, just make it work with 2d arrays in a different method sheesh
def imageDictToDictWithAverages(sourceImagesRaw):
    for d in tqdm(sourceImagesRaw):
        avgRGB = getRGBAverage(d["image"])
        # print(str(d['name'] + " returned avg rgb value of " + str(avgRGB)))
        d["avgRGB"] = avgRGB
    return sourceImagesRaw


# returns average colour from all three bands (r,g,b)
# better than opencv confusing me with b,g,r
# 0 is red, 1 is green, 2 is blue, so in range 3
def getRGBAverage(image):

    average_colour = [mean(image.getdata(band)) for band in range(3)]

    # print("average colour is found to be: " + str(average_colour))

    return average_colour


# returns tuple of base image
# TODO: make this better
def chooseBaseImage(name, sourcedir):
    valid_images = [".jpg", ".png"]

    ext = os.path.splitext(name)[1]
    # TODO: proper exception handling
    if ext.lower() not in valid_images:
        print("error, exception found here")
        return 0
    d = {'name': name, 'image': Image.open(os.path.join(sourcedir, name))}
    return d


# slices images into nxm tiles
# n is width, m is height
def sliceImageToTiles(image, xPixels, yPixels):
    timeStart = time.perf_counter()

    tiles = []

    imageWidth = image.size[0]
    imageHeight = image.size[1]

    n = imageWidth / xPixels
    m = imageHeight / yPixels
    n = int(n)
    m = int(m)

    # TODO: watch this, or make it variable, this changes whether we have rows or columns as [x][y] for the tiles
    tiles = []
    row = []
    tileNum = 0
    for x in range(0, imageWidth, n):
        for y in range(0, imageHeight, m):
            row.append(image.crop((x, y, x+n, y+m)))
            tileNum += 1
        tiles.append(row)
        row = []

    timeEnd = time.perf_counter()
    print("Creating " + str(xPixels) + "x" + str(yPixels) + " = " +
          str(tileNum) + " tiles, " + str(n*m*tileNum) + " pixels in total.")
    print("The original image is " + str(imageWidth) + "x" +
          str(imageHeight) + " = " + str(imageWidth*imageHeight) + " pixels in total.")

    print("Took " + str(timeEnd-timeStart) + " seconds to complete.")
    return tiles


# make new image of height and width of all the incoming tiles combined
# paste them in the right places, how hard can it be?
def reformImageFromTiles(tiles):

    # calculate height of image based on height of one tile, how many tiles there are
    # how many y tiles there are is length of tiles

    timeStart = time.perf_counter()
    print("Now stitching imageMosaic from the swapped tiles...")
    exampleTileDict = tiles[0][0]
    exampleTile = exampleTileDict.get('image')
    tileHeight = exampleTile.size[1]
    tileWidth = exampleTile.size[0]

    yTiles = len(tiles)
    xTiles = len(tiles[0])

    # FIXME: are all tiles the same size?
    # height of new image is number of tiles in y direction * height of one tile (this assumes all tiles are same size!!!)
    newImageHeight = yTiles*tileHeight
    newImageWidth = xTiles*tileWidth

    print("There are " + str(yTiles*xTiles) + " tiles, each of width " + str(tileWidth) + " and height " + str(tileHeight) + ", combining to make an image of width " +
          str(newImageWidth) + " and height " + str(newImageHeight) + ", a total of " + str(newImageWidth*newImageHeight) + " pixels.")

    # then make new image base based on these height and width values:
    newImage = Image.new('RGB', (newImageWidth, newImageHeight))

    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            newImage.paste(tiles[x][y].get('image'),
                           (tileWidth*x, tileHeight*y))

    timeEnd = time.perf_counter()
    print("Stitching complete!")
    print("Took " + str(timeEnd-timeStart) + " seconds to complete.")
    newImage.show()
    return newImage


# turn tiles to dict to allow for reusing methods
def baseImageTilesToDict(tiles):
    tileOutput = []
    row = []
    for j in range(len(tiles)):
        for i in range(len(tiles[j])):
            d = {'name': "tile"+str(j)+str(i), 'image': tiles[j][i]}
            row.append(d)
        tileOutput.append(row)
        row = []
    return tileOutput


# i guess what we should do here is unshape and reshape the array (if it can)
# nono, just make it work with 2d arrays in a different method sheesh
def image2dDictToDictWithAverages(sourceImagesRaw):
    for j in sourceImagesRaw:
        for d in j:
            avgRGB = getRGBAverage(d["image"])
            d["avgRGB"] = avgRGB
    return sourceImagesRaw


# converts 2d array to 1d array, does the averaging operations, makes it 2d again
def baseImagePrepare(baseImageTiles):
    baseImageTileDict = baseImageTilesToDict(baseImageTiles)

    arrayWidth = len(baseImageTileDict)
    arrayHeight = len(baseImageTileDict[0])

    # TODO: fix this list array stuff?
    # convert to 1d array/list

    # turn into 1d array like we have the input stuff for
    baseImageTiles1d = []
    for i in range(arrayWidth):
        for j in range(arrayHeight):
            baseImageTiles1d.append(baseImageTileDict[i][j])

    print("Now calculating average RGB of all " +
          str(arrayWidth*arrayHeight) + " base image tiles...")
    timeStart = time.perf_counter()
    # add averages using the average thing we had before
    baseImageTiles1dWithAverages = imageDictToDictWithAverages(
        baseImageTiles1d)
    timeEnd = time.perf_counter()
    print("average RGB of base image tiles calculation complete!")
    print("Took " + str(timeEnd-timeStart) + " seconds to complete.")

    # associate the images with their rgb values
    # turn back into 2d array

    baseImageOutput = baseImageTiles1dWithAverages
    baseImageTilesComplete = []
    row = []
    k = 0
    for i in range(arrayWidth):
        for j in range(arrayHeight):
            row.append(baseImageOutput[k])
            k += 1
        baseImageTilesComplete.append(row)
        row = []
    return baseImageTilesComplete


def fixBrightness(originalImage, reformedImage):

    timeStart = time.perf_counter()

    print("The newly created image may be discoloured, checking...")
    # output brightness of each one
    print("Now getting the average colour of the original image...")
    originalRGB = getRGBAverage(originalImage)
    print("Now getting the average colour of the image mosaic...")
    reformedRGB = getRGBAverage(reformedImage)

    print("The average colour of the original image is " + str(originalRGB))
    print("The average colour of the reformed image is " + str(reformedRGB))

    print("Correcting...")
    # use image transform matrix to apply an adjustment on each pixel based on the ratio between the original
    # and reformed RGB values

    redRatio = originalRGB[0] / reformedRGB[0]
    greenRatio = originalRGB[1] / reformedRGB[1]
    blueRatio = originalRGB[2] / reformedRGB[2]

    # # green 1.5 matrix
    # colourMatrix = (1, 0,  0, 0,
    #                 0,   1.5,  0, 0,
    #                 0,   0,  1, 0)

    colourMatrix = (redRatio, 0,  0, 0,
                    0,   greenRatio,  0, 0,
                    0,   0,  blueRatio, 0)

    outputImage = reformedImage.convert("RGB", colourMatrix)
    outputRGB = getRGBAverage(outputImage)
    print("The average colour of the reformed image after correction is " + str(outputRGB))

    timeEnd = time.perf_counter()
    print("Took " + str(timeEnd-timeStart) + " seconds to complete.")
    outputImage.show()


    return outputImage
