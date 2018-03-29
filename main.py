#!/usr/bin/env python2.7

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
        self.title = title
        self.discrip = discrip
        self.date = tasktime

class daytask():
    def __init__(self):
        self.daytime = datetime.now()
        self.tasks = []
    def addtask(self,newtask):
        self.tasks = self.tasks + newtask
    def show(self):
        # @todo: formatting of tasks printing
        for item in self.tasks:
            print item.title
            print item.discrip
            print '-----------'
    def add(self,title,discrip='',tasktime = datetime.now()):
        self.addtask(task(title,discrip,tasktime))

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