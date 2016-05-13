#!/usr/bin/env python
#coding=utf-8

import utils
import re
import sys
import ConfigParser
from collections  import defaultdict
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
    price_pattern={}
    price_pattern_file = cf.get('basic','price_pattern_file')
    price_pattern=re_price_pattern(price_pattern_file)
    return price_pattern


special_char = ['(',')','{','}','$','#','+','*','?','.','^','<','!',':']

copy = re.compile(r'(@copy@)',re.S)
copy_replace = '(.*?)'

mioji_key_pat = re.compile(r'(@mioji_key_(?:.){5,20}_\d_mioji@)',re.S)
mioji_key_replace = '(\d+.*)'

def parser(pat_str):
    for char in special_char:
        pat_str = pat_str.replace(char,'\\'+char)

    #pat_str = pat_str.replace('[','(?:').replace(']',')')

    copy_find=copy.findall(pat_str)
    for i in copy_find:
        pat_str = pat_str.replace(i, copy_replace)

    keys=[]
    key_find=mioji_key_pat.findall(pat_str)
    for i in key_find:
        key_name,key_index = utils.parse_key_name_index(f.strip())
        keys.append((key_name,key_index))
        pat_str = pat_str.replace(i,mioji_key_replace)

    re_pat = re.compile(r'%s'%pat_str,re.S)
    return re_pat,keys,pat_str






def  price_parser(line,patterns):
    pat_type, pat_str=line.split('\t')
    
    if pat_type=='single':
        re_pat, re_pat_str=parser(pat_str)
        patterns[pat_type].append(re_pat)

    elif pat_type == 'double':
        re_pat, re_pat_str=parser(pat_str)
        patterns[pat_type].append(re_pat)

    elif pat_type == 'nouse':
        re_pat, re_pat_str = parser(pat_str)
        patterns[pat_type]=parser(re_pat)

    elif pat_type == 'used':
        re_pat, re_pat_str = parser(pat_str)
        patterns[pat_type].append(re_pat)
    
    else:
        pass
    
    return True




def re_price_pattern(filename):
    price_pattern=defaultdict(list)

    for line in open(filename):
        if line.strip() == '':
            continue
        print "input is "+"\t"+line
        price_parser(line.strip(), price_pattern)

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
    if key_str == '':
        pat_instance.same[key_index]="以航空公司规定为准"
    else:
        pat_instance.same[key_index]=key_str
        #print key_str
    return True



#output  price
def mioji_key_price_1_parser(pat_instance,key_index):
    price=pat_instance.same[key_index]
    return price


if __name__ == '__main__':

    price_pattern=loadModel()

    #for i in price_pattern:
    #    print i


