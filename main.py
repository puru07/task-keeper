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


def setup():
    dir_name = 'taskkeeper'
    if not os.path.isdir(os.exapnduser('~/'+ dir_name)):
        os.path.mkdir(os.expanduser('~/' + dir_name))


class almanac():
    def __init__(self,yeartask=None):
        self.records = record()
        if not yeartask is None:
            self.add(yeartask)
    def add(self):

class datamanager():
    def save(self):

    def restore(self):
     
def main():

if __name__=='__main__':
    parser = argparse.ArgumentParser(prog='task_keeper',usage='%(prog)s action [data]')

