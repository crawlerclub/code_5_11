#!/usr/bin/python

#coding=utf-8
import sys
import random
import os
sys.setdefaultencoding('utf-8')

'''
def split_file(filename):
	
	with open(filename) as f:
		for i,j in enumerate(f.readlines()):
			if j.strip() =='':
				continue
			if  i%4==0:
				f1=open('new/new1.txt','a')
				f1.write(j)
				f1.close()
			elif i%4 ==1:
				f2=open('new/new2.txt','a')
				f2.write(j+'\n')
				f2.close()
			elif  i%4==2:
				f1=open('new/new3.txt','a')
				f1.write(j+'\n')
				f1.close()
			elif i%4==3:
				f1=open('new/new4.txt','a')
				f1.write(j+'\n')
				f1.close()



split_file('kopu_test.txt')
'''

def buckets(filename, buckname, separator, classcolumn):
	#put the data in 10 buckets
	numberofbuckets = 10
	data={}
	#first read in the data and divide by category
	with open (filename) as f:
		lines = f.readlines()

	for line in lines:
		if separator != '\t':
			line = line.replace(separator, '\t')
			
		