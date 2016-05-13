#!/usr/bin/python
#coding=utf-8

import re
import sys
import ConfigParser
from   collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf-8')

online_info = {
            'total_price':10000,
            'currency':'CNY',
            'flights':2,
            'order_time':['2016','05','01','12','36'],
            'dept_time_by_flight':[['2016','10','1','12','00'],['2016','10','2','21','33']],
            'price_by_flight':[6500,3500],
            'info_by_flight':[('MU231','PEK','BAK','北京','巴库'),('MU214','BAK','PVG','巴库','巴黎')]
            }

class Price():
	def __init__(self):

		self.name_eng_dic={}   #存放 货币缩写与汇率
		self.name_dic={}       #存放 货币与汇率
		self.name_tup=[]       #存放货币的列表， 里面是三元组
		self.name=[]           #存放 货币的列表
		self.name_eng=[]       #存放货币缩写的列表

def loadModel(config_file = './conf.ini',mode='config'):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)  
    #read exchange
    exchange_file=cf.get('basic','exchange')
    money=re_price(exchange_file)
    return money

def re_price(filename):
	money=Price()
	for line in open(filename):
		if line.strip() == '':
			continue
		name, name_eng , Exrate = line.strip().split('\t')
		if name in money.name:
			pass
		else:
			money.name.append(name)
		if name_eng in money.name_eng:
			pass
		else:
			money.name_eng.append(name_eng)
		money.name_dic[name]=Exrate
		money.name_eng_dic[name_eng]=Exrate
		money.name_tup.append(tuple((name,name_eng,Exrate)))	
	return money




price1=re.compile(r'(\d+(?:,)\d+(?:.)\d+)',re.S)    #1,600.00   1,600
price2=re.compile(r'(\d+(?:.)\d+)',re.S)            #1600.00
price3=re.compile(r'(\d+)',re.S)                    #1600


price4=re.compile(r'(\d+)%',re.S)                   #80%
price5= re.compile(r'(起飞前:(?:：))(.*)(起飞后:(?:：))(.*)',re.S)


#online="aa"
def read_content(filename,online,money):
	with open(filename) as f:
		for line in f.readlines():
			if line.strip()=='':
				continue
			price_content(line, online, money)


def juge_price(pat_str):

	find=price1.findall(pat_str)
	if len(find)!=0:
		return find[0].replace(',','')
	find=price2.findall(pat_str)
	if len(find)!=0:
		return find[0]
	find=price3.findall(pat_str) 
	if len(find)!=0:
		return find[0]
	else:
		return 0

def  each_content(pat_str, online, money,flag):
	for i in money.name:
		if pat_str.find(i)!=-1:
			num=juge_price(pat_str)
			if num:
				print (float(num)*float(money.name_dic[i]),'CNY')
				return flag
	for i in money.name_eng:
		if pat_str.find(i)!=-1:
			num=juge_price(pat_str)
			if num:
				print (float(num)*float(money.name_eng_dic[i]),'CNY')
				return flag
	num=juge_price(pat_str)
	if num:
		print(float(num),'CNY')
		return flag
	flag=0
	print "无法识别"+"\t"+pat_str
	return flag
	

def percent_content(find, online, money, data_time, flag):
	for i in find[0]:
		tmp=price4.findall(i)
		if len(tmp)!=0:
			print (float(tmp[0])/100 ,"%")
		else:
			print i
		return flag




def price_content(pat_str, online, money):
	# read money
	name=money.name
	name_eng=money.name_eng
	name_dic=money.name_dic
	name_eng_dic=money.name_eng_dic

	print "input is "+"\t"+pat_str
	#path=['单程','全程']

	#判断 "每次" 关键字是否存在
	each="每次"
	if each in pat_str:
		flag=1
		flag1=each_content(pat_str,online_info,money,flag)
		if flag1==1:
			return
	

	# 识别带有百分号的 句子
	find=price5.findall(pat_str)
	if len(find)!=0:
		flag=1
		flag1=percent_content(find, online,money, data_time,flag)
		if flag1==1:
			return


	#判断是否有货币 存在
	for  i in name:
		if pat_str.find(i)!=-1:
			num=juge_price(pat_str)
			if num:
				print (float(num)*float(name_dic[i]) ,'CNY')
				return
			else:
				print "无法识别"+ "\t"+pat_str
				return

			

	#判断是否有货币缩写存在
	for i  in money.name_eng:
		if pat_str.find(i)!= -1:
			num=juge_price(pat_str)
			if num:
				print (float(num)*float(money.name_eng_dic[i]),'CNY')
				return
			else:
				print "无法识别"+"\t"+pat_str
				return


	print " 无法识别 "+"\t"+pat_str
	

if __name__ == "__main__":
	money=loadModel()
	#for i in money.name:
	#	print i
	#price_content(pat_str, online, money)
	read_content('pricetest.txt',online_info, money)