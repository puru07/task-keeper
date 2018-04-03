#!/usr/bin/env python3

# @brief this module contains various Important Structure
# @author: Puru Rastogi
# @email: pururastogi@gmail.com

import os
import time
import sys
import argparse
from datetime import datetime

def setup():
    dir_name = 'taskkeeper'
    if not os.path.isdir(os.exapnduser('~/'+ dir_name)):
        os.path.mkdir(os.expanduser('~/' + dir_name))

class task():
    def __init__(self,title ,discrip='',tasktime = datetime.now()):
        self.title = title.lower()
        self.discrip = discrip
        self.date = tasktime

class record():
    def __init__(self):
        self.data = {}
    
    def __getitem__(self,key):
        if key in self.data:
            return self.data[key]
        else :
            return []

    def __setitem__(self,key,value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def show(self):
        # @todo: formatting of tasks printing
        od = sorted(self.data)
        for item in od:
            print(item[0])
            print("-------")
            for rdata in item[1] :
                if rdata is str:
                    print(rdata)
                else rdata.show()

class daytask(record):
    def __init__(self):
        self.instime = datetime.now()
    def addtask(self,newtask):
        self.data[newtask.title] = newtask.discrip

    def add(self,title,discrip='',tasktime = datetime.now()):
        self.addtask(task(title,discrip,tasktime))

class month():
    def __init__():
        self.instime = datetime.now()
        self.monthtask = record()
        self.perdaytask = record()
    
    def add(self,newtask):
        if type(newtask) is daytask:
            self.adddaytask(newtask)
        else:
            self.addtask(newtask)
    
    def addtask(self, newtask):
        'task for the whole month'
        self.monthtask[newtask.title] = newtask
    
    def adddaytask(self, daytask):
        'task for each day'
        self.perdaytask[daytask.instime.day] = daytask

    def show(self):
        # whole month tasks
        self.monthtask.show()








# class almanac():
#     def __init__(self):
#         self.record = {}
#     def adddaytask(self, newdaytask):
#         dayofmonth = newdaytask.daytime.day
#         month = newdaytask.daytime.month
#         year = newdaytask.daytime.year

#         if not year in self.record[year]:
#             self.record[year] = []
#         if not month in 
if __name__=='__main__':
    sys.exit()