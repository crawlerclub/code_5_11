#!/usr/bin/python
#coding=utf-8
import re
import sys
import ConfigParser
import pattern_parser

reload(sys)
sys.setdefaultencoding('utf-8')
'''
def quchong(filename):
    with open(filename) as f:
        for i in set(f.readlines()):
            print i
'''

st="退票1500人民币\每次"
pa=re.compile(r'(\d+.*)',re.S)

find=pa.findall(st)

print find
for i in find:
	print i

#if __name__ == '__main__':
#    quchong('123.txt')  


