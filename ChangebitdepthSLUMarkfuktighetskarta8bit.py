#Script by William.lidberg@slu.se
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'R:/GIS/SWEWAM/' #use m.2 drive as workspace to reduce processing time
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST LZ77 SKIP_FIRST"

in_raster = 'R:/GIS/SWEWAM/SLUMarkfuktighetskarta/probcon3.tif'
out_raster = 'R:/GIS/SWEWAM/SLUMarkfuktighetskarta/SLUMarkfuktighetskarta.tif' #The name of the input shapefile will be used to name the output raster
print('Running')
try:
    arcpy.CopyRaster_management(in_raster, out_raster,"","","-128","NONE","NONE","8_BIT_SIGNED","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
    
except:
    print("Error, you are doing it wrong!")


    
print('done, finished raster is located at R:/GIS/SWEWAM/SLUMarkfuktighetskarta')
