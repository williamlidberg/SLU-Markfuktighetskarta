#Script by john Lindsey, William Lidberg, Kim Lindgren and Anneli Ågren
from __future__ import print_function
import threading
import time
import os
import sys

sys.path.insert(1, r'C:\Fast_GIS\WBT') #This is where whitebox tools is stored.
from whitebox_tools import WhiteboxTools

wb_dir = os.path.dirname('C:/Fast_GIS/WBT/')
wbt = WhiteboxTools()
wbt.set_whitebox_dir(wb_dir)



#Inputs for extracting hydrological features
DEM = 'S:/10mTWI/Clip10mDEM/'
VectorStreams = 'Z:/Sverige/PreProcessing/clip_streams/'
VectorRoads = 'Z:/Sverige/PreProcessing/clip_road_rail/'
##Outputs##
BurnRoads = 'S:/10mTWI/BurnStreamsAcrossRoads/'
BREACHED = 'S:/10mTWI/Breached10mDEM/'
DINFFLOWACC = 'S:/10mTWI/DinfFlowacc10m/'
SLOPE = 'S:/10mTWI/Slope10m/'
TWI = 'S:/10mTWI/WetnessIndex10m/'

maxThreads = 1 #For parallel processing change this number to the number of cores of your machine. Each file in the input folder will be run on a seperate thread.

activeThreads = 0 #Don't change this.
def callback(out_str):
    ''' Create a custom callback to process the text coming out of the tool.
    If a callback is not provided, it will simply print the output stream.
    A custom callback allows for processing of the output stream.
    '''
    try:
        if not hasattr(callback, 'prev_line_progress'):
            callback.prev_line_progress = False
        if "%" in out_str:
            str_array = out_str.split(" ")
            label = out_str.replace(str_array[len(str_array) - 1], "").strip()
            progress = int(
                str_array[len(str_array) - 1].replace("%", "").strip())
            if callback.prev_line_progress:
                print('{0} {1}%'.format(label, progress), end="\r")
            else:
                callback.prev_line_progress = True
                print(out_str)
        elif "error" in out_str.lower():
            print("ERROR: {}".format(out_str))
            callback.prev_line_progress = False
        elif "elapsed time (excluding i/o):" in out_str.lower():
            elapsed_time = ''.join(
                ele for ele in out_str if ele.isdigit() or ele == '.')
            units = out_str.lower().replace("elapsed time (excluding i/o):",
                                            "").replace(elapsed_time, "").strip()
            print("Elapsed time: {0}{1}".format(elapsed_time, units))
            callback.prev_line_progress = False
        else:
            if callback.prev_line_progress:
                print('\n{0}'.format(out_str))
                callback.prev_line_progress = False
            else:
                print(out_str)

    except:
        print(out_str)

class workerThread(threading.Thread):
    def __init__(self, indata):
        threading.Thread.__init__(self)
        self.file = indata

    def run(self):
        global activeThreads
        activeThreads += 1

        #################################
        ##### Start here #####
        #################################

        global wb_dir
        global DEM
        global VectorStreams
        global VectorRoads
        global BurnRoads
        global BREACHED
        global DINFFLOWACC
        global SLOPE
        global TWI


        wbt = WhiteboxTools()
        wbt.set_whitebox_dir(wb_dir)
        #BurnStreamsAtRoads
        inputdem = DEM + self.file
        streams = VectorStreams + self.file.replace('.tif','.shp')
        roads = VectorRoads + self.file.replace('.tif','.shp')
        burnstreamsatroads = BurnRoads + self.file
        args1 = ['--dem=' + inputdem, '--streams=' + streams, '--roads=' + roads, '--output=' + burnstreamsatroads, '--width=5.0']
        #breachdepressions
        #use original DEM instead of roadburned in areas where no roads exist
        burnstreamsatroads = DEM + self.file
        #burnstreamsatroads = BurnRoads + self.file
        breachout = BREACHED + self.file
        args2 = ['--input=' + burnstreamsatroads, '--output=' + breachout]

        #Dinf flowacc for TWI
        DINFFlowaccout = DINFFLOWACC + self.file
        args3 = ['--dem=' + breachout, '--output=' + DINFFlowaccout, '--out_type=sca']

        #Slope Degree
        inputdem = DEM + self.file
        slopedegrees = SLOPE + self.file
        args4 = ['--dem=' + inputdem, '--output=' + slopedegrees]

        #Topographic wetness Index
        twi = TWI + self.file
        args5 = ['--sca=' + DINFFlowaccout, '--slope=' + slopedegrees, '--output=' + twi]

        try:
            #wbt.run_tool('BurnStreamsAtRoads', args1, callback)
            wbt.run_tool('BreachDepressions', args2, callback)
            wbt.run_tool('DInfFlowAccumulation', args3, callback)
            #wbt.run_tool('Slope', args4, callback)
            wbt.run_tool('WetnessIndex', args5, callback)
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        #################################
        ##### end here #####
        #################################

        activeThreads -= 1

infiles = os.listdir(DEM)
outfiles = os.listdir(TWI)

for inputfile in infiles:
    if inputfile.endswith('.tif') and inputfile not in outfiles:
        worker = workerThread(inputfile).start()


    while activeThreads >= maxThreads:
        pass

print('10mTWI done')
input('Script complete enter to close')
