#!/usr/bin/env python

"""This script is designed to iterate over a given directory
    and change names of the files to specification"""

import os, argparse, threading
from os import rename

class DynamicFileRenamer(threading.Thread):
    
    def __init__(self, file_dir, str_pattern, replace_with, verbose):
        threading.Thread.__init__(self)
        self.file_dir = file_dir
        self.str_pattern = str_pattern
        self.replace_with = replace_with
        self.verbose = verbose
        
    def run(self):
        if self.verbose:
            print 'Examining: |{0}| for match |{1}|'.format(self.file_dir, self.str_pattern)
        for file_name in os.listdir(self.file_dir):
            if self.str_pattern in file_name:
                if self.verbose:
                    print '---'
                    print 'Found match with |{0}|'.format(file_name)
                newFile = file_name.replace(self.str_pattern, self.replace_with)
                rename(file_name, newFile)
                if self.verbose:
                    print 'Now named |{0}|'.format(newFile)
                    print '---'
            else:
                if self.verbose:
                    print '|{0}| does not match pattern,'.format(file_name)
        
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser("This script is designed to iterate over a given directory and change names of the files to specification")
    parser.add_argument('-d', '--directory', dest='file_dir', default=os.getcwd())
    parser.add_argument('-p', '--pattern', dest='str_pattern', required=True)
    parser.add_argument('-r', '--replacement', dest='replace_with', required=True)
    parser.add_argument('-v', '--verbose', dest='verbose', default=False, action='store_true')
    args = parser.parse_args()
    renamer = DynamicFileRenamer(args.file_dir,args.str_pattern,args.replace_with,args.verbose)
    threadLock = threading.Lock()
    renamer.start()
    renamer.join()
    
    