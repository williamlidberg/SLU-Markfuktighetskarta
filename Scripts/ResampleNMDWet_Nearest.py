# Resample TIFF image to a higher resolution

import arcpy
arcpy.env.parallelProcessingFactor = "100%"
arcpy.env.workspace = r"T:\copyNMDWet\copy2nearest"
print('Resampling NMDWet Nearest')
arcpy.Resample_management("CopyNMDW.tif", "NMDWet2mN.tif", "2", "NEAREST")
