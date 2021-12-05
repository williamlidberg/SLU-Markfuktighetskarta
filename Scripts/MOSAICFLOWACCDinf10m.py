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

#build full pyramids
arcpy.env.pyramid = "PYRAMIDS -1 CUBIC LZ77 NO_SKIP"
#arcpy.env.pyramid = 'NONE'

import arcpy, time


arcpy.env.workspace = "Y:/Skogsstyrelsen/DinfFlowacc10m/"
workspace = "Y:/Skogsstyrelsen/DinfFlowacc10m/"
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
MosaicToNewRaster(rasters, r'Y:\Skogsstyrelsen\DinfFlowacc10mMosaic', 'FlowAccumulatio10mnDinf.tif', '', '', 10, 1, "MAXIMUM","")
input('Script complete enter to close')
