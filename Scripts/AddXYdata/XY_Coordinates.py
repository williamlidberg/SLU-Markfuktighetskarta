import arcpy
import sys
import os
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

from arcpy import env
arcpy.env.overwriteOutput = True
arcpy.env.pyramid = 'NONE'
#arcpy.env.outputCoordinateSystem = arcpy.SpatialReference('SWEREF99_TM')
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
#arcpy.env.scratchWorkspace = 'R:/GIS/Arcmap/Scratch.gdb'
infeature = sys.argv[1]
#arcpy.env.extent = infeature
#arcpy.env.snapRaster = infeature
env.workspace = 'E:/DEM/'

RASTERS= 'E:/DEM/'
PointsToRaster = 'D:/MLWAM_Production/Convet_shape_to_raster/XYRaster/Points/'
PointsToRasterX = 'D:/MLWAM_Production/Convet_shape_to_raster/XYRaster/Raster/X/'
PointsToRasterY = 'D:/MLWAM_Production/Convet_shape_to_raster/XYRaster/Raster/Y/'

print ('start run')
#Parameters for RasterToPoints
inRaster = infeature
outPoint = os.path.join(PointsToRaster, str(infeature).replace('.tif', '.shp'))
field = 'VALUE'
#Parameters for points to rasters
valFieldX = 'POINT_X'
valFieldY = 'POINT_Y'
outRasterX = os.path.join(PointsToRasterX, str(infeature))
outRasterY = os.path.join(PointsToRasterY, str(infeature))
assignmentType = 'MEAN'
priorityField = ''
cellSize = 2

try:
        PointsToRaster = arcpy.RasterToPoint_conversion(inRaster, outPoint, field)
        arcpy.AddXY_management(outPoint)
        X_Raster = arcpy.PointToRaster_conversion(outPoint, valFieldX, outRasterX, assignmentType, priorityField, cellSize)
        Y_Raster = arcpy.PointToRaster_conversion(outPoint, valFieldY, outRasterY, assignmentType, priorityField, cellSize)
except Exception as e:
    print(e)
    MessageBox(None, infeature, 'ERROR', 0)

print('Done')
