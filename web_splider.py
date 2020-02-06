##!/usr/bin/env python
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
from urlparse import *
import requests
import httplib2
import zlib
import re
import os
import sys
import Web_mod

class Web_Splider:
	def __init__(self):
		self.get_pic_total   = 0
		self.page_headers    = {}
		self.pic_headers     = {}
		self.Img_rules       = ''
		self.Title_rules     = ''
		self.get_next_page   = None
		self.curr_encoding   = ''
		self.save_path       = ''

	def Download_Picture(self, url, dl_directory):
		#print self.pic_headers
		web_data = requests.get(url, headers=self.pic_headers, allow_redirects=False)

		if web_data.status_code != 200:
			print 'GET: %d, Stop Download %s' % (web_data.status_code, url)
			return False

		self.get_pic_total += 1
		Save_File_Path = dl_directory + '\\%03d_' % (self.get_pic_total) + url.split('/')[-1]

		#print Save_File_Path + '\n'
		#with open(Save_File_Path, 'wb') as code:
		#	code.write(web_data.content)
		print 'Save_File_Path: %s' % (Save_File_Path)
		pic_file = open(Save_File_Path, 'wb')
		for chunk in web_data.iter_content(chunk_size=512):
			if chunk:
				pic_file.write(chunk)
		print 'Save File Ok\n'
		return True

	def Get_Curr_Soup(self, url, headers):
		web_data = requests.get(url, headers=headers)
		web_data.encoding = self.curr_encoding
		soup = BeautifulSoup(web_data.text, 'lxml')
		return soup

	# 新建文件夹的命名规则(Windows 系统)
	def Directory_naming_rules(self, title):
		filtering = '/\\:*?"<>|'
		for c in filtering:
			title = title.replace(c, '')
		return title

	def Get_Save_Path(self, Curr_Soup, SetPath=None):
		Save_Path = ''
		channel = Curr_Soup.select(self.Title_rules)
		print channel
		for list in channel:
			if list != None:
				title = list.get_text()
				if title == None:
					continue
				else:
					break

		if title == None:
			print 'Get Web Page Title failed!'
		else:
			title = self.Directory_naming_rules(title)

		if not (SetPath is None):
			if SetPath[-1] == '\\':
				SetPath = SetPath[:-1]
			if not os.path.exists(SetPath):
				os.mkdir(SetPath)
			Save_Path = SetPath + '\\' + title
		else:
			Save_Path = sys.path[0] + '\\' + title

		print '\nSave_Path: %s\n' % Save_Path
		if not os.path.exists(Save_Path):
			os.mkdir(Save_Path)
		return Save_Path

	def Get_one_page(self, Curr_Soup, Save_Path):
		channel = Curr_Soup.select(self.Img_rules)
		for list in channel:
			if list != None:
				pic_src = list.get('src')
				if pic_src == None:
					continue
				print pic_src
				self.Download_Picture(pic_src, Save_Path)

	def Add_readme_file(self, Save_Path, url):
		file_object = open(Save_Path + '\\redeme.txt', 'w')
		file_object.write('web site: %s' % url)
		file_object.close()

	def Get_Next_Page(self, Curr_Soup, current_url):
		next_url = self.get_next_page(Curr_Soup, current_url)
		return next_url

	def Analytical_url(self, url):
		r = urlparse(url)  # Get Web HOST address
		host = r.netloc
		host = host.replace('www.', '')
		web = Web_mod.GetWebPlatform(host[0:host.rfind('.', 1)])
		if web == None:
			print 'Not support %s web-site!' % (r.netloc)
			return False

		self.page_headers  = web.get_page_headers()
		self.pic_headers   = web.get_pic_headers()
		self.Title_rules   = web.get_title_rules()
		self.Img_rules     = web.get_img_rules()
		self.get_next_page = web.get_next_page
		self.curr_encoding = web.get_curr_encoding()
		self.save_path     = web.get_save_path()
		return True

	def Get_Web_Pic(self, url):
		current_url = url
		page_cnt = 0;

		if self.Analytical_url(url) == False:
			print 'Analytical url is failed'
			return None

		Curr_Soup = self.Get_Curr_Soup(current_url, self.page_headers)

		Save_Path = self.Get_Save_Path(Curr_Soup, self.save_path)

		self.Add_readme_file(Save_Path, current_url)

		while True:
			page_cnt += 1;
			print 'Get %d page' % page_cnt

			self.Get_one_page(Curr_Soup, Save_Path)
			self.pic_headers['Referer'] = current_url

			current_url = self.Get_Next_Page(Curr_Soup, current_url)
			print "Get Next Page %s\n" % (current_url)

			if current_url == None:
				break
			Curr_Soup = self.Get_Curr_Soup(current_url, self.page_headers)

		self.get_pic_total = 0

