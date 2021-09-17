#Script by john Lindsey, William Lidberg, Kim Lindgren and Patryk Waraksa
from __future__ import print_function
import threading
import time
import os
import sys
#Patryk added this line so we can run the scripts outside of the WBT folder. Just specify here whitebox tools is stored.
sys.path.insert(1, r'C:\Programs_william\WBT') #the "r" infront means string litteral and means that you can have \ in the path instead of /.
from whitebox_tools import WhiteboxTools

wb_dir = os.path.dirname('C:/Programs_william/WBT/')

#inputs
DEMS = 'V:/WAMBAFB/WAMBAFTOOLS/DEMs/'
IMPOUNDMENTINDEX = 'V:/WAMBAFB/WAMBAFTOOLS/ImpoundmentIndex/'


maxThreads = 1

activeThreads = 0
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
        global DEMS
        global IMPOUNDMENTINDEX



        wbt = WhiteboxTools()
        wbt.set_whitebox_dir(wb_dir)

        #Impiundment size index
        originaldems = DEMS + self.file
        impoutput = VectorRoads + self.file
        type = 'depth' #'volume', and 'area'
        damlength = '5' #Max number of cells. use the largest roads in the catchment as guide. no burning will be done once you are past the roads.
        args = ['--dem=' + originaldems, '--output=' + impoutput , '--out_type=' + type , '--damlength=' + damlength]

        try:
            wbt.run_tool('ImpoundmentSizeIndex', args1, callback)

        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        #################################
        ##### end here #####
        #################################

        activeThreads -= 1

for inputfile in os.listdir(DEMS):
    if inputfile.endswith('.dep'):
        worker = workerThread(inputfile).start()

    while activeThreads >= maxThreads:
        pass
