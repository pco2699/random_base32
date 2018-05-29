#!/usr/bin/env python
# coding: utf-8

"""
Base32に沿ったランダムな文字列を出力するスクリプト
"""
__author__  = "pco2699 <aenkun@gmail.com>"
__version__ = "1.00"
__date__    = "14 May 2018"

import random
import string
from time import sleep

def main():
    n = 16
    while(True):
        try:
            random_str = ''.join([random.choice(string.ascii_uppercase + '234567') for i in range(n)])
            print(random_str)
            sleep(1)
        except KeyboardInterrupt:
            exit(0)

if __name__ == '__main__':
    main()