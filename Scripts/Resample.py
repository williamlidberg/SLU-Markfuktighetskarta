# Resample TIFF image to a higher resolution

import arcpy
arcpy.env.parallelProcessingFactor = "100%"
arcpy.env.workspace = r"S:/Jorddjup"
print('Resampling Jorddjup')
arcpy.Resample_management("jorddjup_10x10.tif", "resample2m.tif", "2", "NEAREST")
