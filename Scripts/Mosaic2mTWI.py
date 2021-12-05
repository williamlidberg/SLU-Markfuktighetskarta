##==================================
##Mosaic To New Raster
##Usage: MosaicToNewRaster_management inputs;inputs... output_location raster_dataset_name_with_extension
##                                    {coordinate_system_for_the_raster} 8_BIT_UNSIGNED | 1_BIT | 2_BIT | 4_BIT
##                                    | 8_BIT_SIGNED | 16_BIT_UNSIGNED | 16_BIT_SIGNED | 32_BIT_FLOAT | 32_BIT_UNSIGNED
##                                    | 32_BIT_SIGNED | | 64_BIT {cellsize} number_of_bands {LAST | FIRST | BLEND  | MEAN
##                                    | MINIMUM | MAXIMUM} {FIRST | REJECT | LAST | MATCH}
print('Start Script')
import os
import arcpy
from arcpy import (CheckOutExtension, da)
from arcpy.management import MosaicToNewRaster
from os import path
arcpy.env.parallelProcessingFactor = "100%"
arcpy.env.pyramid = 'NONE' #Don't build pyramids


import arcpy, time



arcpy.env.workspace = r"S:\10mTWI\ResampledTWI"
workspace = r"S:\10mTWI\ResampledTWI"
arcpy.env.workspace = workspace
sr = arcpy.SpatialReference(3006) # Swereff 99 TM
arcpy.CheckOutExtension("Spatial")

#Make list of rasters to mosaic

rasters = []
walk = arcpy.da.Walk(workspace, topdown=True, datatype="RasterDataset")
for dirpath, dirnames, filenames in da.Walk(workspace, topdown=True, datatype="RasterDataset"):
     for filename in filenames:
          rasters.append(filename)


ras_list = ';'.join(rasters)
print('List of input raster files')
print('')
print(ras_list)
MosaicToNewRaster(rasters, r'S:\10mTWI\MosaicResampledTWI', 'TWI10m.tif', '', '8_BIT_UNSIGNED', 2, 1, 'MAXIMUM')
print('Done')
