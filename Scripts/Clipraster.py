##Clip Raster Dataset by known extent - Left Bottom Right Top
import os
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'V:/MLWAM_Production/Shapefiles/testsquares/'

#Local variables

LIDARSQUARES = 'V:/MLWAM_Production/Shapefiles/testsquares/'
CLIPPEDRASTERS = 'T:/Split_raster/DTW1ha/'

#in_template_dataset = ?
for file in os.listdir(LIDARSQUARES):
    if file.endswith('.shp'):
        #local variables
        out_raster = CLIPPEDRASTERS + file.replace('.shp', '.tif')
        in_raster = 'S:/DTW_1ha_mosaic/0.tif'
#        in_template_dataset = '' use DTW for this later
        #get extent of polygon file to clip raster
        desc = arcpy.Describe(file)
        frame = str(desc.extent)
        
        try:
            print('Running for file = ' + file)
            arcpy.management.Clip(in_raster, frame, out_raster)
        except:
            print("Expected error, I have no idea what I'm doing")


#arcpy.management.Clip(r"S:\DTW_2ha_mosaic\DTW_2ha.tif.tif", "422499,999999999 6975000 425000 6977500", r"T:\Split_raster\test2.tif", r"V:\MLWAM_Production\Shapefiles\testsquares\18786.shp", -3,402823e+38, "NONE", "NO_MAINTAIN_EXTENT")
