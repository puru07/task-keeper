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
    def __init__(self,title ,discrip='',tasktime = None):
        self.title = title.lower()
        self.discrip = discrip
        if tasktime is None:
            tasktime = datetime.now()
        self.date = tasktime

    def show(self):
        print(self.discrip)


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
        od = sorted(self.data.items())
        for item in od:
            print(item[0])
            print("-------")
            for rdata in item[1] :
                if rdata is str:
                    print(rdata)
                else:
                    rdata.show()

class daytask():
    def __init__(self,taskortitle=None, discrip='',tasktime=None):
        self.instime = datetime.now()
        self.taskrecord =record()
        if not taskortitle is None:
            self.add(taskortitle, discrip,tasktime)

    def add(self,taskortitle, discrip='',tasktime=None):
        'generic add method'
        self.addtask(taskortitle, discrip,tasktime)

    def addtask(self,newtask, discrip='',tasktime=None):
        'add task obj'
        if type(newtask) is str:
            newtask = task(newtask,discrip,tasktime)
        self.taskrecord[newtask.title] = newtask

    def show(self):
        self.taskrecord.show()


class monthtask(daytask):
    def __init__(self,taskortitle=None, discrip='',tasktime=None):
        self.instime = datetime.now()
        self.taskrecord = record()   # single task for complete month
        self.perdaytask = record()  # tasks for each day
        
        if not taskortitle is None:
            self.add(taskortitle, discrip,tasktime)

    def add(self,taskortitle, discrip='',tasktime=None):
        'generic add method'
        if type(taskortitle) is daytask:
            self.adddaytask(taskortitle)
        else :
            self.addtask(taskortitle, discrip,tasktime)

    def adddaytask(self, newtask):
        'task for each day'
        self.perdaytask[newtask.instime.day] = newtask

    def show(self):
        # whole month tasks
        self.taskrecord.show()
        print("==============")
        # perday tasks
        self.perdaytask.show()

class  year(monthtask):
    def __init__(self,taskortitle=None, discrip='',tasktime=None):
        self.instime = datetime.now()
        self.taskrecord = record()      # single task for complete month
        self.permonthtask = record()    # tasks for each month
        
        if not taskortitle is None:
            self.add(taskortitle, discrip,tasktime)

    def add(self,taskortitle, discrip='',tasktime=None):
        'generic add month'
        if type(taskortitle) is monthtask:
            self.addmonthtask(taskortitle)
        else:
            self.addtask(taskortitle, discrip,tasktime)
    def addmonthtask(self,newtask):
        self.permonthtask[newtask.instime.month] = newtask
    
    def show(self):
        # whole year tasks
        self.taskrecord.show()
        print("==============")
        # per month tasks
        self.permonthtask.show()

# if __name__=='__main__':
#     parser = argparse.ArgumentParser(prog='task_keeper',usage='%(prog)s mode ')