# Import system modules and set environmental veriables
import arcpy, os
from arcpy import env
env.overwriteOutput = True
arcpy.env.parallelProcessingFactor = '100%'
arcpy.env.compression = 'NONE'
# Set workspace
env.workspace = 'D:/WilliamLidberg/NH/Isobasins'

#The buffered isobasins will also be used to clipp the swedish 2m DM
Swedish10mDEM = 'S:/10mTWI/DEM10m/DEM10m2.tif'
BufferedBasin = 'Z:/Sverige/split_avr_1km/'
ClippedDEMfiles = 'S:/10mTWI/Clip10mDEM/'

#This loop will clip the DEM with the buffered isobasins. Each isobasin will be processed separately.
print ('Clip 10m m DEM with buffered isobasins')
for inputFilename in os.listdir(BufferedBasin) :
    if inputFilename.endswith('.shp') :
        #Set paths
        BufferPath = os.path.join(BufferedBasin, inputFilename)
        RasteroutputPath = os.path.join(ClippedDEMfiles, inputFilename.replace('.shp','.tif'))
        #Clip raster with buffered isobasins
        print ('Clipping isobasin nr ' + inputFilename.replace('.shp', ''))
        arcpy.Clip_management('S:/10mTWI/DEM10m/DEM10m2.tif', "#", RasteroutputPath, BufferPath, '0 ', 'ClippingGeometry')
print ('DEM clipped')
