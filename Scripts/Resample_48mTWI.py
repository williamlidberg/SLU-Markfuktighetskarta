# Resample TIFF image to a higher resolution

import arcpy
arcpy.env.parallelProcessingFactor = "100%"
arcpy.env.workspace = r"D:/MLWAM_Production/TWI_resample/TWI48m"
print('Resampling 48mTWI')
arcpy.Resample_management("TWI_48.tif", "R48to2m.tif", "2", "NEAREST")
