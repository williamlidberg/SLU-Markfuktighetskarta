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
arcpy.env.workspace = 'E:/MLWAM_TEMP/Student' #use m.2 drive as workspace to reduce processing tim
#arcpy.env.workspace = 'E:/DEM' #use m.2 drive as workspace to reduce processing time
arcpy.env.pyramid = 'NONE'
arcpy.env.overwriteOutput = True

#Input raster locations
DEM = 'E:/DEM' #band1
DTW05ha = 'D:/MLWAM_Production/Rasters/clipped/DTW05ha'
DTW1ha = 'D:/MLWAM_Production/Rasters/clipped/DTW1ha'
DTW5ha = 'D:/MLWAM_Production/Rasters/clipped/DTW5ha'
DTW30ha = 'D:/MLWAM_Production/Rasters/clipped/DTW30ha'
STDV5 = 'D:/MLWAM_Production/Rasters/clipped/STDV5'
Winter = 'D:/MLWAM_Production/Rasters/clipped/Winter'
Summer = 'D:/MLWAM_Production/Rasters/clipped/Summer'
Autum = 'D:/MLWAM_Production/Rasters/clipped/Autum'
Soil = 'D:/MLWAM_Production/Rasters/clipped/Soil32BitFloat'
Wetlands = 'D:/MLWAM_Production/Rasters/clipped/Wetlands32BitFloat'
TWI24 = 'D:/MLWAM_Production/Rasters/clipped/TWI24'
TWI48 = 'D:/MLWAM_Production/Rasters/clipped/TWI48'
DI2m = 'D:/MLWAM_Production/Rasters/clipped/DI_2m'
X_Coordinate = 'D:/MLWAM_Production/Rasters/Original/X_Coordinates'
Y_Coordinate = 'D:/MLWAM_Production/Rasters/Original/Y_Coordinates'
SoilDepth = 'D:/MLWAM_Production/Rasters/clipped/SoilDepth'
NMDWet = 'D:/MLWAM_Production/Rasters/clipped/NMDwet'
CVA = 'D:/MLWAM_Production/Rasters/clipped/CircularVarianceOfAspect'
DFME = 'D:/MLWAM_Production/Rasters/clipped/DeviationfromMeanElevation'
Rugged = 'D:/MLWAM_Production/Rasters/clipped/RuggednessIndex'
SDFS = 'D:/MLWAM_Production/Rasters/clipped/StandardDeviationFromSlope'

#Output folder location
StackFolder = 'E:/MLWAM_TEMP/studentstacks'
#StackFolder = 'F:/MLWAM_Production/RasterStacks/DemoStacks'
#Input raster bands
Band1 = os.path.join(DEM, str(inraster))
Band2 = os.path.join(DTW05ha, str(inraster))
Band3 = os.path.join(DTW1ha, str(inraster))
Band4 = os.path.join(DTW5ha, str(inraster))
Band5 = os.path.join(DTW30ha, str(inraster))
Band6 = os.path.join(STDV5, str(inraster))
Band7 = os.path.join(Winter, str(inraster))
Band8 = os.path.join(Summer, str(inraster))
Band9 = os.path.join(Autum, str(inraster))
Band10 = os.path.join(Soil, str(inraster))
Band11 = os.path.join(Wetlands, str(inraster))
Band12 = os.path.join(TWI24, str(inraster))
Band13 = os.path.join(TWI48, str(inraster))
Band14 = os.path.join(DI2m, str(inraster))
Band15 = os.path.join(X_Coordinate, str(inraster.replace('.tif', '_Y.tif')))
Band16 = os.path.join(Y_Coordinate, str(inraster.replace('.tif', '_Y.tif')))
Band17 = os.path.join(SoilDepth, str(inraster))
Band18 = os.path.join(NMDWet, str(inraster))

#output
Rasterstacks = os.path.join(StackFolder, str(inraster))

#make list of all bands. THE ORDER IS IMPORTANT
listbands = [Band1,Band2,Band3,Band4,Band5,Band6,Band7,Band8,Band9,Band10,Band11,Band12,Band13,Band14,Band15,Band16,Band17,Band18]

print ('start run')
try:
        Rasterstacks = arcpy.CompositeBands_management(listbands, Rasterstacks)

except Exception as e:
    print(e)
    MessageBox(None, inraster, 'ERROR', 0)

print ('Done')
