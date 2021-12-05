# Import system modules
import os
import arcpy
from arcpy import env
# Set environment settings
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'E:/Workfolder/Jordarter/William_erased/' #use m.2 drive as workspace to reduce processing time

# Set local variables
inFeature = 'E:/Workfolder/Jordarter/William_erased/Soilmap_North_SGU.shp'
outRaster = 'D:/MLWAM_Production/Convet_shape_to_raster/Jordarter/North_SGU.tif'
cellSize = 'D:/MLWAM_Production/Rasters/Original/DEM/mosaic/hojddata2.tif'
field = 'code'

# Execute FeatureToRaster
arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)
