#-*-coding:utf-8-*-

import sys
import Web_mod

#start_url="http://yxpjw.vip/xiurenwang/2017/0807/3715.html"
#start_url="http://yxpjw.vip/luyilu/2017/0818/3761.html"

page_headers_old = {
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding' : 'gzip, deflate',
	'Accept-Language' : 'zh-CN,zh;q=0.8',
	'Cache-Control' : 'no-cache',
	'Connection' : 'keep-alive',
	'DNT' : '1',
	'Host' : 'yxpjw.me',
	'Pragma' : 'no-cache',
	'Referer' : 'http://yxpjw.me/xiurenwang/2017/0818/3759.html',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
}

page_headers = {
	'Host': 'www.mmjpg.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'DNT': '1',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
}

pic_headers = {
	'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	'DNT': '1',
	'Host': 'images.zhaofulipic.com:8818',
	'Referer': 'http://yxpjw.me/xiurenwang/2017/0807/3715.html',
	'Pragma': 'no-cache',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
}

Title_rules = 'body > section > div > div > header > h1'
Img_rules = 'body > section > div > div > article > p > img'
Next_page_rules = 'li.next-page > a'

def LoadConfName():
	return "yxpjw"

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
	if (len(channel) == 0):
		return None
	new_page = channel[0].get('href')
	next_url = current_url[0:current_url.rfind('/', 1) + 1] + new_page
	return next_url

def GetEncoding():
	return 'gb2312'

def GetSavePath():
	save_path = sys.path[0] + '\\yxpjw'
	return save_path

def LoadConfDoc():
	return  'yxpjw.vip web splider'

def Init():
	Web_mod.NewWeb(LoadConfName, LoadConfPageHeaders, LoadConfPicHeaders, LoadConTitleRules, LoadConImgRules, GetNextPage, GetEncoding, GetSavePath, LoadConfDoc)
