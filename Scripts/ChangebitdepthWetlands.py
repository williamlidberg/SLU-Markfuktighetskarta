##Clip Raster Dataset by known extent - Left Bottom Right Top
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'D:/MLWAM_Production/Rasters/clipped/Wetlands/' #use m.2 drive as workspace to reduce processing time

#Set Local variables
INRASTER = 'D:/MLWAM_Production/Rasters/clipped/Wetlands/'
COPIEDRASTERS = 'D:/MLWAM_Production/Rasters/clipped/Wetlands32BitFloat/' #path to output folder were copiedrasters will be saved

#Loop to find all shapefiles in a folder and clip based on their extent
for file in os.listdir(INRASTER):
    if file.endswith('.tif'):
        #local variables

        in_raster = INRASTER + file
        out_raster = COPIEDRASTERS + file #The name of the input shapefile will be used to name the output raster

        try:
            print('Running for Wetland file = ' + file)
            arcpy.CopyRaster_management(in_raster, out_raster,"","",16,"NONE","NONE","32_BIT_FLOAT","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
        except:
            print("Error, you are doing it wrong!")
