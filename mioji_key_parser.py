#!/usr/bin/env python
#coding=utf-8

import utils
import re
import sys
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')



key_parser = {
        '@mioji_key_flightno_0_mioji@':'mioji_key_flightno_0_parser',
        '@mioji_key_flightno_1_mioji@':'mioji_key_flightno_1_parser',
        '@mioji_key_price_0_mioji@':'mioji_key_price_0_parser',
        '@mioji_key_price_1_mioji@':'mioji_key_price_1_parser',
        '@mioji_key_copy_0_mioji@':'@mioji_key_copy_0_parser',
        '@mioji_key_copy_1_mioji@':'@mioji_key_copy_1_parser'
    }


def loadModel(config_file = './conf.ini',mode='config'):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)  
    #read price_pattern
    price_pattern=[]
    price_pattern_file = cf.get('basic','price_pattern_file')
    price_pattern=re_price_pattern(price_pattern_file)
    return price_pattern


special_char = ['(',')','{','}','$','#','+','*','?','.','^','<','!',':']

mioji_price = re.compile(r'(@price@)',re.S)
mioji_price_replace = '(.*?)'



def re_price_pattern(filename):
    price_pattern=[]
    for line in open(filename):
        if line.strip() == '':
            continue
        print "input is "+"\t"+line
        for char in special_char:
            line=line.replace(char, '\\'+char)

        #step 2 提取mioji_price，并将 mioji_price 对应的位置替换为固定的字符串
        find = mioji_price.findall(line)
        for f in find:
            line = line.replace(f, mioji_price_replace)

        price_pat= re.compile(r'%s'%line,re.S)
        print "output is "+"\t"+line
        price_pattern.append(price_pat)

    return price_pattern



#read flightno
def mioji_key_flightno_0_parser(key_str,pat_instance,key_index):
    # input. 提取出航班号。    
    #elements = key_pattern.findall(key_str)[0]
    pat_instance.flightno[key_index] = key_str
   # pat_instance.flight_index[pat_instance.flight.flightno2index[elements]] = 1
    return True

#output flightno
def mioji_key_flightno_1_parser(pat_instance,key_index):
    # output. 直接输出航班号。
    flight_no = pat_instance.flightno[key_index]
    return flight_no


# read price
def mioji_key_price_0_parser(key_str,pat_instance,key_index):
    pat_instance.same[key_index]=key_str
    return True



#output  price
def mioji_key_price_1_parser(pat_instance,key_index):
    price=pat_instance.same[key_index]
    return price


if __name__ == '__main__':

    price_pattern=loadModel()

    #for i in price_pattern:
    #    print i


