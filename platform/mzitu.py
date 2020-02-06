#-*-coding:utf-8-*-

import sys
import Web_mod

#http://www.mzitu.com/100202

page_headers = {
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding' : 'gzip, deflate',
	'Accept-Language' : 'zh-CN,zh;q=0.8',
	'Cache-Control' : 'max-age=0',
	'Connection' : 'keep-alive',
	'DNT' : '1',
	'Host' : 'www.mzitu.com',
	'Referer' : 'http://www.mzitu.com/best/',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
}

pic_headers = {
	'Host': 'i.meizitu.net',
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
	'DNT': '1',
	'Referer': 'http://www.mzitu.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
}

Title_rules = 'body > div.main > div > h2'
Img_rules = 'body > div.main > div > div.main-image > p > a > img'
Next_page_rules = 'body > div.main > div > div.pagenavi > a'

def LoadConfName():
	return "mzitu"

def LoadConfPageHeaders():
	return page_headers

def LoadConfPicHeaders():
	return pic_headers

def LoadConTitleRules():
	return Title_rules

def LoadConImgRules():
	return Img_rules

def GetNextPage(Curr_Soup, current_url):
	channel = Curr_Soup.select(Next_page_rules)

	a1 = channel[-1].get('href')
	a2 = channel[-2].get('href')
	
	a2 = a2[0: a2.rfind('/')]

	if (a1.find(a2) != -1):
		return a1
	else:
		return None

def GetEncoding():
	return 'utf-8'

def GetSavePath():
	save_path = sys.path[0] + '\\mzitu'
	return save_path

def LoadConfDoc():
	return  'mzitu.com web splider'

def Init():
	Web_mod.NewWeb(LoadConfName, LoadConfPageHeaders, LoadConfPicHeaders, LoadConTitleRules, LoadConImgRules, GetNextPage, GetEncoding, GetSavePath, LoadConfDoc)
