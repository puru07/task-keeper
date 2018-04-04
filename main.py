#!/usr/bin/env python3

# @brief this module contains various Important Structure
# @author: Puru Rastogi
# @email: pururastogi@gmail.com

import os
import time
import sys
import argparse
from datetime import datetime
from taskmodule import *
import pickle

def setup():
    dir_name = 'taskkeeper'
    if not os.path.isdir(os.exapnduser('~/'+ dir_name)):
        os.path.mkdir(os.expanduser('~/' + dir_name))

class almanac():
    def __init__(self,yeartask=None):
        self.records = record()
        if not yeartask is None:
            self.add(yeartask)


class datamng():
    def __init__(self, name=None):
        self.name = 'alamanac.pkl'
        if not name is None:
            self.name = name + '.pkl'
    def save(self, data):
        with open(self.name, 'wb') as dataobj:
            pickle.dump(data, dataobj)

    def restore(self):
        with open(self.name,'rb') as dataobj:
            return pickle.load(dataobj)

def main():
    dmanage = datamng()
    p = [123,984]
    dmanage.save(p)

if __name__=='__main__':
    parser = argparse.ArgumentParser(prog='task_keeper',usage='%(prog)s action [data]')

