##Clip Raster Dataset by known extent - Left Bottom Right Top
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'T:/DeepLearning/Krycklan/selected/'  #use m.2 drive as workspace to reduce processing time

#Set Local variables
LIDARSQUARES = 'T:/DeepLearning/Krycklan/selected/' #selected demoareas to copy
SPLITDEMFILES = 'V:/MLWAM_Production/Rasters/Clipped/DEM/' #Folder with all splitted raster files
COPIED_RASTERS = 'T:/DeepLearning/Krycklan/Rasters/' #path to output folder were copiedrasters will be saved

#Loop to find all shapefiles in a folder and clip based on their extent
for file in os.listdir(LIDARSQUARES):
    if file.endswith('.shp'):
        #local variables

        in_raster = SPLITDEMFILES + file.replace('.shp', '.tif')
        out_raster = COPIED_RASTERS + file.replace('.shp', '.tif') #The name of the input shapefile will be used to name the output raster

        try:
            print('Running for file = ' + file)
            arcpy.CopyRaster_management(in_raster, out_raster)
        except:
            print("Error, you are doing it wrong!")
