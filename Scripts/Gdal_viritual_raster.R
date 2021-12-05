library(gdalUtils)
setwd('Z:/Sverige/PreProcessing/failures/DTW/05/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DTW05.vrt")

setwd('Z:/Sverige/PreProcessing/failures/DTW/1/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DTW1.vrt")

setwd('Z:/Sverige/PreProcessing/failures/DTW/2/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DTW2.vrt")

setwd('Z:/Sverige/PreProcessing/failures/DTW/5/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DTW5.vrt")

setwd('Z:/Sverige/PreProcessing/failures/DTW/30/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DTW30.vrt")

setwd('Z:/Sverige/PreProcessing/failures/DownSlopeIndex/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DI2m.vrt")

setwd('F:/MLWAM_Production/PredictedTwoClassedProbability/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "Probability.vrt")

setwd('Y:/RIP_NATURE/Finland/Finland/CHM/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "Probability.vrt")

#create viritual raster using gdal
library(gdalUtils)
setwd("F:/Finland/CHM")
listoftiffiles<-dir(path = "F:/Finland/CHM", pattern = "\\.tif$", full.names = TRUE, recursive = TRUE)
dataframe<-as.data.frame(listoftiffiles)
#write.table(x,"filename.txt",sep="\t",row.names=FALSE)
write.table(dataframe, "F:/Finland/CHM/listoftiffiles.txt", append = FALSE, sep = " ",
            row.names = FALSE, col.names = FALSE)

gdalbuildvrt(input_file_list = "F:/Finland/CHM/listoftiffiles.txt", output.vrt = "CMH.vrt")

library(gdalUtils)
setwd('Z:/Sverige/PreProcessing/failures/DTW/05/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "DTW05.vrt")

library(rgdal)
library(gdalUtils)
setwd('Y:/William/DeepLearning/DitchnetProduction/DEM1m/FilesWithinAOI/')
gdalbuildvrt(gdalfile = "*.tif", # uses all tiffs in the current folder
             output.vrt = "AOITiles.vrt")
