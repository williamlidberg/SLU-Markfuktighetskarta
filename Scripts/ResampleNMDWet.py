# Resample TIFF image to a higher resolution

import arcpy
arcpy.env.parallelProcessingFactor = '100%'
arcpy.env.pyramid ='NONE'
arcpy.env.workspace = r"D:/MLWAM_Production/Rasters/Original/copyNMDWet"
print('Resampling NMDWet')
arcpy.Resample_management("CopyNMDW.tif", "NMDWet2mB.tif", "2", "BILINEAR")
input('Script complete enter to close')
