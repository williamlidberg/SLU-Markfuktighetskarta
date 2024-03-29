#Script by john Lindsey, William Lidberg, Kim Lindgren and Anneli Ågren
from __future__ import print_function
import threading
import time
import os
import sys

sys.path.insert(1, r'C:\William_Program\WhiteboxTools_win_amd64\WBT') #This is where whitebox tools is stored.
from whitebox_tools import WhiteboxTools

wb_dir = os.path.dirname('C:/William_Program/WhiteboxTools_win_amd64/WBT/')
wbt = WhiteboxTools()
wbt.set_whitebox_dir(wb_dir)


rootdirr = 'D:/MLWAM_Production/temp/testdirr/'
#rootdirr = 'D:/MLWAM_Production/Rasters/clipped/'
maxThreads = 63 #For parallel processing change this number to the number of cores of your machine.

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
        global rootdirr


        wbt = WhiteboxTools()
        wbt.set_whitebox_dir(wb_dir)

        #Arguments for elevation
        inputfile = os.path.join(root,file)
        args1 = ['--input=' + inputfile, '--new_value=' + '-32768']


        try:
            wbt.run_tool('ModifyNoDataValue', args1, callback)
            print('running for file ' + inputfile)
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        #################################
        ##### end here #####
        #################################

        activeThreads -= 1


for root,dirs,files in os.walk(rootdirr):
    for file in files:
        if file.endswith('.tif'):
            worker = workerThread(file).start()
        while activeThreads >=maxThreads:
            pass


input('Script complete enter to close')
