#-*-coding:utf-8-*-

import sys
import Web_mod

#https://www.meitulu.com/item/4845.html

page_headers = {
	'Host':'www.meitulu.com',
	'Connection':'keep-alive',
	'Cache-Control':'max-age=0',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'DNT':'1',
	'Referer':'https://www.meitulu.com/',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8',
}

pic_headers = {
	'Host': 'mtl.ttsqgs.com',
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
	'DNT': '1',
	'Referer': 'https://www.meitulu.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
}

Title_rules = 'body > div.width > div.weizhi > h1'
Img_rules = 'body > div.content > center > img'
Next_page_rules = 'body > center > div#pages > a'
Next_page2_rules = 'body > center > div#pages > span'

def LoadConfName():
	return "meitulu"

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

	# get all number
	list_index = []
	for list in channel[1:-1]:
		list_index.append(int(list.get_text()))

	# get span values
	channel2 = Curr_Soup.select(Next_page2_rules)
	if (len(channel2) == 0):
		return None
	span_nu = int(channel2[0].get_text())

	# cmp end
	if (span_nu == (max(list_index) + 1)):
		return None

	new_page = channel[-1].get('href')
	next_url = current_url[0:current_url.find('/', 8) + 1] + new_page[1:]
	print next_url
	return next_url

def GetEncoding():
	return 'utf-8'

def GetSavePath():
	save_path = sys.path[0] + '\\meitulu'
	return save_path

def LoadConfDoc():
	return  'meitulu.com web splider'

def Init():
	Web_mod.NewWeb(LoadConfName, LoadConfPageHeaders, LoadConfPicHeaders, LoadConTitleRules, LoadConImgRules, GetNextPage, GetEncoding, GetSavePath, LoadConfDoc)
