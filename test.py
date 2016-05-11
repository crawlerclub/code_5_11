#!/usr/bin/python
#coding=utf-8
import re
import sys
import ConfigParser
import pattern_parser

reload(sys)
sys.setdefaultencoding('utf-8')

'''
def loadModel(config_file = './conf.ini',mode='config'):

    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    srcs = cf.get('basic','sources').strip().split(' ')  
    patterns = {}
    src='kopu'
    patterns[src] = pattern_parser.parse_patterns(cf.get(src,'source'),cf.get(src,'pattern'),cf.get(src,'type'))   
    return patterns

all_patterns = loadModel()

#print "--------------------"
#print all_patterns


line="@mioji_key_flightno_0_0_mioji@:退票@mioji_any_0_200_mioji@,改签:[起飞前:|]@mioji_key_price_0_0_mioji@误机" 
re_pat,mioji_keys,pat_str=pattern_parser.re_parse(line)

print pat_str
print mioji_keys
text="AF1767:退票:不允许退票,改签:起飞前:120.00欧元, 起飞后:120.00欧元,误机:退票误机不允许退票，改期误机不允许退票。AF382:退票:不允许退票,改签:起飞前:120.00欧元, 起飞后:120.00欧元,误机:退票误机不允许退票，改期误机不允许退票。以上信息仅供参考，准确退改信息请咨询客服。改期和退票额外收取100元服务费。境外系统出票，报销凭证仅提供境外invoice报销"
spliter = '。'
strs = text.strip().split(spliter)  
#print strs


for s in strs:
    if s.strip() == '':
        continue
    s += spliter
    print "hello"+"\t"+s

#text="AF1767:退票:不允许退票,改签:起飞前:120.00欧元, 起飞后:120.00欧元,误机:退票误机不允许退票，改期误机不允许退票。"


    try :
        finds=re_pat.findall(s)
        #print "-----"
       # print len(finds)
        for i in finds:
           # print "-------"
           # print len(i)
            for j in i:
                print j
                #print "12"
    
    except Exception, e:
        print "hello"
        print str(e)


'''
def all_pattern_test(rf):
    
    for line in open(rf):
        #print "asdfsf"
        if line.strip() == '': 
            continue
        print line
        
print "hello"
pattern=re.compile(r'\| (\d+) \| (\d+) \|')
numset=set()
all='''
| 29266795 | 533 |
| 29370116 | 533 |
| 29467495 | 533 |
| 29500404 | 533 |
| 29500622 | 533 |
| 29515964 | 530 |
| 29516015 | 530 |
| 29520954 | 530 |
| 29520960 | 530 |
| 29525346 | 530 |
| 29525351 | 530 |
| 29525365 | 530 |
'''
matches=pattern.findall(all)
for did,dt in matches:
  numset.add(did)
print numset
print len(numset)
print "fuck"
#if __name__ == '__main__':
   
#    rf='kopu_test.txt'
   # print "hel"
#    all_pattern_test(rf)
