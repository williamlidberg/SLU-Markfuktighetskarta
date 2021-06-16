##Clip Raster Dataset by known extent - Left Bottom Right Top
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'D:/MLWAM_Production/Rasters/clipped/Summer/'

#Set Local variables
#SUMMERIN = 'D:/MLWAM_Production/Rasters/clipped/Summer/'
#SUMMEROUT = 'D:/MLWAM_Production/Rasters/clipped/Summer32BitFLoat/' #path to output folder were copiedrasters will be saved
#AUTUMNIN = 'D:/MLWAM_Production/Rasters/clipped/Autum/'
#AUTUMNOUT = 'D:/MLWAM_Production/Rasters/clipped/Autum32BitFloat/'
WINTERIN = 'D:/MLWAM_Production/Rasters/clipped/Winter/'
WINTEROUT = 'D:/MLWAM_Production/Rasters/clipped/Winter32BitFLoat/'

#Loop to find all shapefiles in a folder and clip based on their extent
# for file in os.listdir(SUMMERIN):
#     if file.endswith('.tif'):
#         #local variables
#         summerin_raster = SUMMERIN  + file
#         summerout_raster = SUMMEROUT + file #The name of the input shapefile will be used to name the output raster
#         try:
#             print('copying summerfile = ' + file)
#             arcpy.CopyRaster_management(summerin_raster, summerout_raster,"","","","NONE","NONE","32_BIT_FLOAT","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
#         except:
#             print("Error, you are doing it wrong!")

#Loop to find all shapefiles in a folder and clip based on their extent
# autumin = os.listdir(AUTUMNIN)
# autumout = os.listdir(AUTUMNOUT)
#
# for file in autumin:
#     if file.endswith('.tif') and file not in autumout:
#         autumnin_raster = AUTUMNIN + file
#         atumnoutraster = AUTUMNOUT + file
#         try:
#             print('Running for file {0}'.format(file))
#             arcpy.CopyRaster_management(autumnin_raster, atumnoutraster,"","","","NONE","NONE","32_BIT_FLOAT","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
#         except:
#             print("Error, you are doing it wrong!")

winterinfiles = os.listdir(WINTERIN)
winteroutfiles = os.listdir(WINTEROUT)
#Loop to find all shapefiles in a folder and clip based on their extent
for file in winterinfiles:
    if file.endswith('.tif') and file not in winteroutfiles:
        winterinraster = WINTERIN + file
        winteroutraster = WINTEROUT + file
        try:
            print('Running for file {0}'.format(file))
            arcpy.CopyRaster_management(winterinraster, winteroutraster,"","","","NONE","NONE","32_BIT_FLOAT","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
        except:
            print("Error, you are doing it wrong!")

input('Script complete enter to close')
