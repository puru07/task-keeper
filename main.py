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

class daytask(record):
    def __init__(self):
        self.instime = datetime.now()
        self.data ={}
    def addtask(self,newtask):
        self[newtask.title] = newtask

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
        print("==============")
        self.perdaytask.show()



# if __name__=='__main__':
#     parser = argparse.ArgumentParser(prog='task_keeper',usage='%(prog)s mode ')