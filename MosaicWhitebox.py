import os
import sys
from os import path

sys.path.insert(1, r'C:\William_Program\WhiteboxTools_win_amd64\WBT') #This is where whitebox tools is stored.


wb_dir = os.path.dirname('C:/William_Program/WhiteboxTools_win_amd64/WBT/')
wbt = WhiteboxTools()
wbt.set_whitebox_dir(wb_dir)
from whitebox_tools import WhiteboxTools
def main():
    #####################################################################
    # Script Settings: modify these as is appropriate to your use-case. #
    #####################################################################
    source_data_dir = "F:/MLWAM_Production/PredictedThreeClassedMLWAM/"
    # See the user manual for a listing of all supported raster formats.
    tile_extension = ".tif" # Here I've used an ArcGIS ASCII raster format as input.
    raster_data_dir = "F:/MLWAM_Production/ThreeClassedMosaic/"
    mosaic_extension = ".tif" # The output mosaic is being saved here as a GeoTIFF.
    mosaic_method = "nn" # "nn" = nearest neighbour; "bilinear" = bilinear; "cc" = cubic convolution
    delete_source_tiles = False
    fill_nodata_gaps = False

    ########################
    # Set up WhiteboxTools #
    ########################
    wbt = WhiteboxTools()
    wbt.work_dir = raster_data_dir # set working directory
    wbt.verbose = False # Make it so that Whitebox doesn't output every progress update
    if not os.path.exists(raster_data_dir):
        os.makedirs(raster_data_dir)

    ##############################################################
    # Mosaic raster tiles; this is done using intermediate steps #
    ##############################################################
    processed_files = []
    num_mosaiced = 1
    flag = True
    round = 1
    while flag:
        # This will mosaic a maximum of 50 tiles together; these sub-files
        # will subsequently be merged. Mosaicing many hundreds of tiles
        # together at one time is otherwise too computationally intensive.
        # Depending on your system resources and the tile sizes, you may have to
        # adjust this number.
        file_names = find_files(source_data_dir, tile_extension, processed_files, 50)
        if len(file_names) > 1:
            in_files = ""
            for i in range(len(file_names)):
                if i < len(file_names)-1:
                    in_files += f"{file_names[i]};"
                else:
                    in_files += f"{file_names[i]}"

                processed_files.append(file_names[i])
                num_mosaiced += 1

            out_file = raster_data_dir + f"mosaic{round}{mosaic_extension}"
            wbt.mosaic(inputs=in_files, output=out_file, method=mosaic_method)
            print(f"Processing mosaic {round}; num. files = {num_mosaiced}")

            if delete_source_tiles:
                for i in range(len(file_names)):
                    os.remove(source_data_dir + file_names[i])

        else:
            flag = False

        round += 1

    wbt.verbose = True
    mosaic_file = raster_data_dir + f"final_mosaic{mosaic_extension}"
    file_names = find_mosaic_files(raster_data_dir, mosaic_extension)
    if len(file_names) > 1:
        in_files = ""
        for i in range(len(file_names)):
            if i < len(file_names)-1:
                in_files += f"{file_names[i]};"
            else:
                in_files += f"{file_names[i]}"

            num_mosaiced += 1


        wbt.mosaic(inputs=in_files, output=mosaic_file, method=mosaic_method)

        # now clean up the intermediate mosaics; you'll want to delete them.
        for i in range(len(file_names)):
            os.remove(raster_data_dir + file_names[i])



    ##############################################
    # Would you like to fill in the NoData gaps? #
    ##############################################
    if fill_nodata_gaps:
        dem_nodata_filled = raster_data_dir + f"DEM_gaps_filled{mosaic_extension}"
        wbt.fill_missing_data(mosaic_file, dem_nodata_filled, filter=101)

    print("Done!")

def find_files(input_dir, extension, processed_files, max_num=10):
    files = os.listdir(input_dir)
    file_names = []
    for f in files:
        if f.endswith(extension) and f not in processed_files:
            if len(file_names) < max_num:
                file_names.append(f)
            else:
                break

    return file_names

def find_mosaic_files(input_dir, mosaic_extension):
    files = os.listdir(input_dir)
    file_names = []
    for f in files:
        if "mosaic" in f and f.endswith(mosaic_extension):
            file_names.append(f)

    return file_names

main()
