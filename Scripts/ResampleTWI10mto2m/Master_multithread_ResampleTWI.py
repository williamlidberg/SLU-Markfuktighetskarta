#Original script by Kim Lindgren, adapted by William Lidberg

import os
import threading
import subprocess

#global parameters

maxThreads = 60
activeThreads = 0

#Inut files
file_directory = 'S:/10mTWI/WetnessIndex10m'
#output files of subprocess
outputdirectory = 'S:/10mTWI/ResampledTWI'

class workerThread(threading.Thread):
    def __init__(self, indata, script):
        threading.Thread.__init__(self)
        self.input = indata
        self.script = script

    def changeActiveThreads(self, nr):
        global activeThreads
        activeThreads += nr

    def run(self):
        global activeThreads #Måste vara första raden.
        activeThreads += 1 #Måste komma innan du börjar köra det tunga kommandot.

        subprocess.call(['C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/python.exe', self.script, self.input], stdout=open('log.txt', 'a'), stderr=open('log_err.txt', 'a'))

        activeThreads -= 1 #Måste vara sista raden och komma efter att kommandot är slutkört.

infiles = os.listdir(file_directory)
outfiles = os.listdir(outputdirectory)

for f1 in infiles:
    if f1.endswith('.tif') and f1 not in outfiles:
        print('Running for file {0}'.format(f1))
        worker = workerThread(f1, 'Slave_ResampleTWI.py').start()

    while activeThreads >= maxThreads:
        pass

input('Script complete enter to close')
