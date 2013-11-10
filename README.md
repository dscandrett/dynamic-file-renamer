Dynamic File Renamer
====================

A small python script designed to help bulk renaming of files. There are a lot of other ways of doing this, obviously, but this one has some nice options, a clear command-line interface, and is nicely customizable.

### How to use
```
usage: This script is designed to iterate over a given directory and change names of the files to specification
       [-h] (-n NEEDLE_STR | -r REGEX_STR) [-d FILE_DIR] [-s SUBSTITUTION_STR]
       [-v]

optional arguments:
  -h, --help            show this help message and exit
  -n NEEDLE_STR, --needle NEEDLE_STR
                        The string to match. This does not use regular
                        expressions. To change a file extension, for example,
                        you might pass |-n .jpg|
  -r REGEX_STR, --regex REGEX_STR
                        The regex string to match. This is a regular
                        expression, and cannot be used with the -n flag
  -d FILE_DIR, --directory FILE_DIR
                        The directory to look through. Default is the current
                        working directory.
  -s SUBSTITUTION_STR, --substitution SUBSTITUTION_STR
                        The substitution string. Default is to remove the
                        matched string |empty string|. If the regex option is
                        used, this will be a regex replacement. Note the empty
                        default is mostly useless if the regex matches the
                        entire string.
  -v, --verbose
```

Here is an example using the regex option and the verbose flag (-v):
```
python dynamic_renamer.py -d ~/Desktop/test_dir/ -r '(.*?).doc' -v -s 'document.\1'
Examining: |/Users/doug/Desktop/test_dir/| for regex pattern |(.*?).doc|
|file1.txt| does not match pattern
|file2.txt| does not match pattern
|file3.txt| does not match pattern
|file4.txt| does not match pattern
---
Match found |nonsense.doc|
Now named |document.nonsense|
---
```

### License

The MIT License (MIT)

Copyright (c) 2013 Doug Scandrett

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
