#!/usr/bin/env python

"""This script is designed to iterate over a given directory
    and change names of the files to specification"""

import os, argparse, threading, re

class DynamicFileRenamer(threading.Thread):
    
    def __init__(self, file_dir, needle_str, regex_str, substitution_str, verbose):
        threading.Thread.__init__(self)
        self.file_dir = os.path.expanduser(file_dir)
        self.needle_str = needle_str
        self.regex_str = regex_str
        self.substitution_str = substitution_str
        self.verbose = verbose
        
    def run(self):
        if self.needle_str is not None:
            self.log_if_needed('Examining: |{0}| for match |{1}|'.format(self.file_dir, self.needle_str))
            for file_name in os.listdir(self.file_dir):
                if self.needle_str in file_name:
                    self.log_if_needed('---')
                    self.log_if_needed('Found match with |{0}|'.format(file_name))
                    new_file = file_name.replace(self.needle_str, self.substitution_str)
                    os.rename(os.path.join(self.file_dir, file_name), os.path.join(self.file_dir, new_file))
                    self.log_if_needed('Now named |{0}|'.format(new_file))
                    self.log_if_needed('---')
                else:
                    self.log_if_needed('|{0}| does not match pattern'.format(file_name))
        else:
            self.log_if_needed('Examining: |{0}| for regex pattern |{1}|'.format(self.file_dir, self.regex_str))
            for file_name in os.listdir(self.file_dir):
                if re.match(r'{0}'.format(self.regex_str),file_name):
                    self.log_if_needed('---')
                    self.log_if_needed('Match found |{0}|'.format(file_name))
                    new_file = re.sub(r'{0}'.format(self.regex_str), r'{0}'.format(self.substitution_str), file_name)
                    os.rename(os.path.join(self.file_dir, file_name), os.path.join(self.file_dir, new_file))
                    self.log_if_needed('Now named |{0}|'.format(new_file))
                    self.log_if_needed('---')
                else:
                    self.log_if_needed('|{0}| does not match pattern'.format(file_name))

    def log_if_needed(self, log_str):
        if self.verbose:
            print log_str

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser("This script is designed to iterate over a given directory and change names of the files to specification")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '--needle', dest='needle_str', default=None, help='The string to match. This does not use regular expressions. To change a file extension, for example, you might pass |-n .jpg|')
    group.add_argument('-r', '--regex', dest='regex_str', default=None, help='The regex string to match. This is a regular expression, and cannot be used with the -n flag')
    parser.add_argument('-d', '--directory', dest='file_dir', default=os.getcwd(), help='The directory to look through. Default is the current working directory.')
    parser.add_argument('-s', '--substitution', dest='substitution_str', default='', help='The substitution string. Default is to remove the matched string |empty string|. If the regex option is used, this will be a regex replacement. Note the empty default is mostly useless if the regex matches the entire string.')
    parser.add_argument('-v', '--verbose', dest='verbose', default=False, action='store_true')
    args = parser.parse_args()
    renamer = DynamicFileRenamer(args.file_dir, args.needle_str, args.regex_str, args.substitution_str, args.verbose)
    threadLock = threading.Lock()
    renamer.start()
    renamer.join()
    
    