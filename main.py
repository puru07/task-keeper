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


def setup(name=None):
    flolder_name = 'taskkeeper'
    dir_name = os.path.expanduser('~/' + flolder_name)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/almanac.pkl'
    if name is not None:
        filename = dir_name + '/' + name + '.pkl'
    return datamng(filename)


class datamng():
    def __init__(self, name):
        self.name = name

        # try to restore old data
        alm = self.restore()

        # if no data is found
        if alm is None:
            alm = almanac()
        self.almanac = alm

    def save(self):
        'save the current almanac'
        with open(self.name, 'wb') as dataobj:
            pickle.dump(self.almanac, dataobj)

    def restore(self):
        'restore any previosly saved almanac'
        if not os.path.isfile(self.name):
            return None
        with open(self.name, 'rb') as dataobj:
            return pickle.load(dataobj)


def main():
    datamng = setup()
    almanac = datamng.almanac
    # almanac.add('uasc', 'do this and that')
    # almanac.add('hb', 'do this')
    almanac.show()
    datamng.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='task_keeper',usage='%(prog)s action [data]')
    main()
