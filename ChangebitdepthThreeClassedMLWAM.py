##Clip Raster Dataset by known extent - Left Bottom Right Top
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'F:/MLWAM_Production/Predict3classedonFailedRasterStacks/'

#Set Local variables
MLWAMIN = 'F:/MLWAM_Production/Predict3classedonFailedRasterStacks/'
MLWAMOUT = 'F:/MLWAM_Production/FourBitRasters/ThreeClassed/'

mlwaminfiles = os.listdir(MLWAMIN)
mlwamoutfiles = os.listdir(MLWAMOUT)
#Loop to find all shapefiles in a folder and clip based on their extent
for file in mlwaminfiles:
    if file.endswith('.tif') and file not in mlwamoutfiles:
        mlwaminraster = MLWAMIN + file
        mlwamoutraster = MLWAMOUT + file
        try:
            print('Running for file {0}'.format(file))
            arcpy.CopyRaster_management(mlwaminraster, mlwamoutraster,"","","","NONE","NONE","4_BIT","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
        except:
            print("Error, you are doing it wrong!")

input('Script complete enter to close')
