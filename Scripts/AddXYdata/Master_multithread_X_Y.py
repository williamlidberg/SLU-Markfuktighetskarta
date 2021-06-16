#!/usr/bin/env python3

import os
import threading
import subprocess

#global parameters

maxThreads = 63
activeThreads = 0

LIST1 = 'E:/DEM/'

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

infiles = os.listdir(LIST1)

for f in infiles:
    if f.endswith(".tif"):
        print('Running for file {0}'.format(f))
        worker = workerThread(f, 'XY_Coordinates.py').start()

    while activeThreads >= maxThreads:
        pass
