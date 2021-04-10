from PIL import Image
import os
import os.path
from statistics import mean
import numpy as np
import time


def replacePixelAverages(sourceImages, baseImageTiles):
    baseImageWidth = len(baseImageTiles)
    baseImageHeight = len(baseImageTiles[0])

    exampleTileDict = baseImageTiles[0][0]
    exampleTile = exampleTileDict.get('image')
    tileHeight = exampleTile.size[1]
    tileWidth = exampleTile.size[0]

    print("Now swapping all tiles with source images...")
    timeStart = time.perf_counter()
    averageDiff = []
    # for each tile
    for i in range(baseImageWidth):
        for j in range(baseImageHeight):
            # for each source image
            for k in range(len(sourceImages)):
                # calculate difference of each source image to the current tile
                # d["avgRGB"]
                # TODO: fix this so its less scuffed, isolate the R G B values?
                avgrgb1 = baseImageTiles[i][j].get('avgRGB')
                avgrgb2 = sourceImages[k].get('avgRGB')
                currentDiff = abs(
                    avgrgb1[0] - avgrgb2[0]) + abs(avgrgb1[1] - avgrgb2[1]) + abs(avgrgb1[2] - avgrgb2[2])
                # print("current diff is " + str(currentDiff))
                averageDiff.append(currentDiff)
            # get the index of the minimum value (minimum difference = tile that is closest in average values)
            minValue = min(averageDiff)
            minIndex = averageDiff.index(minValue)
            # replace item baseImageTiles[i][j] with sourceImages[minIndex]
            # haha need to resize i FORGOT
            baseImageTiles[i][j] = sourceImages[minIndex]
            baseImageTiles[i][j]['image'] = baseImageTiles[i][j].get(
                'image').resize((tileWidth, tileHeight))
            averageDiff = []

    timeEnd = time.perf_counter()
    print("Took " + str(timeEnd-timeStart) + " seconds to complete.")
    print("Tile swapping complete!")
    return baseImageTiles
