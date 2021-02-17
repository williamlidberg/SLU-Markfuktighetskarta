#Original script by Kim Lindgren, adapted by William Lidberg

import os
import threading
import subprocess

#global parameters

maxThreads = 63
activeThreads = 0

#Set file directory to where your DEM files are stored. This script will make a raster stack for each file in this folder.
file_directory = 'E:/MLWAM_TEMP/Student'
#Demosites
#file_directory = 'E:/MLWAM_TEMP/Demofiles'
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

        subprocess.call(['C:/Program Files/ArcGIS/Pro/bin/Python/envs/arcgispro-py3/pythonw.exe', self.script, self.input], stdout=open('log.txt', 'a'), stderr=open('log_err.txt', 'a'))

        activeThreads -= 1 #Måste vara sista raden och komma efter att kommandot är slutkört.

infiles = os.listdir(file_directory)

for f in infiles:
    if f.endswith(".tif"):
        print('Running for file {0}'.format(f))
        worker = workerThread(f, 'Slave_CompositeBands.py').start()

    while activeThreads >= maxThreads:
        pass
