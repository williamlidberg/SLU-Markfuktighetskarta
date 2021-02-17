#Script by William Lidberg
import arcpy
import sys
import os
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')
#arcpy.env.scratchWorkspace = 'R:/GIS/Arcmap/Scratch.gdb'
inraster = sys.argv[1]

#Environment
#Set workspace to the location of all DEM files. This script will make a rasterstack for each file in this folder.
arcpy.env.workspace = 'S:/10mTWI/WetnessIndex10m' #use m.2 drive as workspace to reduce processing tim
#arcpy.env.workspace = 'E:/DEM' #use m.2 drive as workspace to reduce processing time
arcpy.env.pyramid = 'NONE'
arcpy.env.overwriteOutput = True
#temp
arcpy.env.parallelProcessingFactor = "100%"

#Input raster locations
TWI10m = 'S:/10mTWI/WetnessIndex10m' #band1

#Output folder location
TWI2m = 'D:/MLWAM_Production/Rasters/clipped/SoilDepth'

inraster10m = os.path.join(TWI10m, str(inraster))
outraster2m = os.path.join(TWI2m, str(inraster))


print ('start run')
try:
        Soil2m = arcpy.Resample_management(inraster10m, outraster2m, '2', "BILINEAR")

except Exception as e:
    print(e)
    MessageBox(None, inraster, 'ERROR', 0)

print ('Done')
