#!/usr/bin/env python

"""Test some basic operations in dynamic_renamer.py"""

import dynamic_renamer, os, unittest, shutil, threading

class DynamicFileRenamerTest(unittest.TestCase):
    
    def __init__(self, test_name):
        unittest.TestCase.__init__(self, test_name)
        self.test_dir = os.path.join(os.getcwd(), 'test_directory')

    def setUp(self):
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        names = ['random','other','important','useless'];
        extensions = ['.txt','.doc','.zip']
        for name in names:
            for extension in extensions:
                joined = '{0}{1}'.format(name,extension)
                open(os.path.join(self.test_dir, joined), 'a').close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def run_renamer(self, renamer):
        threadLock = threading.Lock()
        renamer.start()
        renamer.join()

    def test_remove_docs(self):
        renamer = dynamic_renamer.DynamicFileRenamer(self.test_dir,'.doc', None, '', True)
        self.run_renamer(renamer)
        for file_name in os.listdir(self.test_dir):
            if '.doc' in file_name:
                self.fail('There should be no more .doc files')

    def test_change_pattern(self):
        renamer = dynamic_renamer.DynamicFileRenamer(self.test_dir, None, '(.*?).doc', 'document.\\1', True)
        self.run_renamer(renamer)
        changed = []
        for file_name in os.listdir(self.test_dir):
            if 'document.' in file_name:
                changed.append(file_name)
        if len(changed) is not 4:
            self.fail('There should be exactly 4 files with the prefix document.')


if __name__ == '__main__':
    unittest.main()
