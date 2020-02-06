#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import sys
from web_splider import *
import Web_mod

def InitList():
	ErrorFlag = True
	filepath = sys.path[0] + '\platform'
	if not filepath in sys.path:
		sys.path.append(filepath)
	
	ModuleList = []
	for root, dirs, files in os.walk(filepath):
		for name in files:
			if name.endswith(".py") or name.endswith(".pyc"):
				list = os.path.splitext(name)
				name = list[0]
				ModuleList.append(name)
	
	for module in ModuleList:
		if not module in sys.modules:
			mod = __import__(module)
			try:
				ret = mod.Init()
				if ret == False:
					ErrorFlag = False
			except:
				pass
	return  ErrorFlag

def Analytical_url(url):
	print url

def help():
	pass



if __name__ == "__main__":
	InitList()
	#for su_list in Web_mod.Web_Mod_List:
	#	print 'Support: %s' % (su_list)
	WP = Web_Splider()
	while True:
		input_url = raw_input("\nPlease input web page:\n")
		if input_url == "exit":
			exit()
		if input_url == "help":
			help()
			continue
		#Analytical_url(input_url)
		WP.Get_Web_Pic(input_url)

