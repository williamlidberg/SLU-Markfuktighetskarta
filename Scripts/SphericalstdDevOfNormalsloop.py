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

DEM = 'D:/Slope/dems/'
STDV = 'D:/Slope/stdv/'
#rootdirr = 'D:/MLWAM_Production/Rasters/clipped/'



start = time.time()
for file in os.listdir(DEM):
    if file.endswith('.tif'):
        try:
            demfile = DEM + file
            STDVoutput = STDV + file
            args = ['--dem=' + demfile, '--output=' + STDVoutput, '--height=2', '--res_factor=2']
            wbt.run_tool('VisibilityIndex', args, callback)
        except:
            print('Unexpected error:', sys.exc_info()[0])

print('It took', time.time()-start, 'seconds.')
input('Script complete enter to close')
