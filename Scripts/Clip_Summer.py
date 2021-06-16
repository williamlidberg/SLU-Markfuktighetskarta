##Clip Raster Dataset by known extent - Left Bottom Right Top
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'T:/Split_raster/DEM/' #use m.2 drive as workspace to reduce processing time

#Set Local variables
LIDARSQUARES = 'T:/Split_raster/DEM/' #Save clip files on m.2 drive to reduce processing time
#LIDARSQUARES = 'C:/Fast_GIS/LaserSquare_New_Split_DEM/' #Save clip files on m.2 drive to reduce processing time
RASTERTOBECLIPPED = 'S:/SMHI_Summer/summer.tif'
CLIPPED_RASTERS = 'T:/Split_raster/Summer/' #path to output folder were clipped rasters will be saved

#Loop to find all shapefiles in a folder and clip based on their extent
for file in os.listdir(LIDARSQUARES):
    if file.endswith('.tif'):
        #local variables
        out_raster = CLIPPED_RASTERS + file #The name of the input shapefile will be used to name the output raster
        in_raster = 'S:/SMHI_Summer/summer.tif' #Raster mosaic to be clipped
        in_template_dataset = LIDARSQUARES + file #use DEM for all other tools
        #get extent of file to clip raster
        desc = arcpy.Describe(file)
        clippextent = str(desc.extent)


        try:
            print('Running for file = ' + file)
            arcpy.management.Clip(in_raster, clippextent, out_raster, in_template_dataset, "#", "#", "MAINTAIN_EXTENT")
        except:
            print("Error, you are doing it wrong!")
