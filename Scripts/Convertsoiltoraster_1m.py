# Import system modules
import os
import arcpy
from arcpy import env
# Set environment settings
arcpy.env.overwriteOutput = True ## 1
arcpy.env.workspace = 'E:/Workfolder/Jordarter/William_erased/' #use m.2 drive as workspace to reduce processing time

# Set local variables
inFeature = 'E:/Workfolder/Jordarter/William_erased/1m_soilmap.shp'
outRaster = 'D:/MLWAM_Production/Convet_shape_to_raster/Jordarter/1m.tif'
cellSize = 'D:/MLWAM_Production/Rasters/Original/DEM/mosaic/hojddata2.tif'
field = 'code'

# Execute FeatureToRaster
arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)
