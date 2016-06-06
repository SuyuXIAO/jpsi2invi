#!/usr/bin/env python
"""
Check PBS jobs 
"""

__author__ = "SHI Xin <shixin@ihep.ac.cn>"
__copyright__ = "Copyright (c) SHI Xin"
__created__ = "[2016-06-02 Thu 09:42]" 

import sys
import os


def usage():
    sys.stdout.write('''
NAME
    chk_pbsjobs.py 

SYNOPSIS

    ./chk_pbsjobs.py  input_dir num_files

    ./chk_pbsjobs.py  $HOME/bes/jpsi2invi/v0.1/run/data 321 

AUTHOR 
    SHI Xin <shixin@ihep.ac.cn> 

DATE
    June 2016 
\n''')

    
def main():
    args = sys.argv[1:]
    if len(args) < 2:
        return usage()
    
    src = args[0]
    num = args[1]
    sys.stdout.write('Scanning %s...\n' %src)

    file_list = []
    total_size = 0 
    for root, dirs, files in os.walk(src):
        for f in files:
            file_list.append(int(f.split('-')[-1].split('.')[0]))
            total_size = total_size + os.path.getsize(os.path.join(root,f))

    sys.stdout.write('Found %s files, with total size %s.\n' %(
        len(file_list), convert_size_to_str(total_size)))

    
def convert_size_to_str(size):
    c_1GB = 1024*1024*1024
    factor = float(size)/c_1GB
    size_str = '%.1fGB' %factor
    return size_str


if __name__ == '__main__':
    main()
