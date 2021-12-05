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




rootdirr = 'D:/MLWAM_Production/Rasters/clipped/'
for root,dirs,files in os.walk(rootdirr):
    for file in files:
        if file.endswith('.tif'):
            try:
                inputfile = os.path.join(root,file)
                args1 = ['--input=' + inputfile, '--new_value=' + '-32768']
                wbt.run_tool('ModifyNoDataValue', args1)
                print('running for file ' + inputfile)

            except:
                print('error')

input('Script complete enter to close')
