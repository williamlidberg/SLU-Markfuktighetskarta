#Script by William.lidberg@slu.se
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'D:/MLWAM_Production/Rasters/clipped/Wetlands/' #use m.2 drive as workspace to reduce processing time
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST LZ77 SKIP_FIRST"

in_raster = 'R:/GIS/SWEWAM/SLUMarkfuktighetskartaKlassad/SLUMFKKlassadVattenMaskad/SLUMarkfuktighetskartaKlassad.tif'
out_raster = 'R:/GIS/SWEWAM/SLUMarkfuktighetskartaKlassad/SLUMarkfuktighetskartaKlassad.tif' #The name of the input shapefile will be used to name the output raster

try:
    print('Running')
    arcpy.CopyRaster_management(in_raster, out_raster,"","",15,"NONE","NONE","4_BIT","NONE","NONE", "TIFF", "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
except:
    print("Error, you are doing it wrong!")
    
print('done, finished raster is located at R:/GIS/SWEWAM/SLUMarkfuktighetskartaKlassad/')
