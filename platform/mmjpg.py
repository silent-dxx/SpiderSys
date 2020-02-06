#-*-coding:utf-8-*-

import sys
import Web_mod

#http://www.mmjpg.com/mm/1081

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
	'Host': 'img.mmjpg.com',
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
	'DNT': '1',
	'Referer': 'http://www.mmjpg.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
}

Title_rules = 'body > div > div > h2'
Img_rules = 'body > div > div > div.content > a > img'
Next_page_rules = 'body > div > div > div.page > a.next'

def LoadConfName():
	return "mmjpg"

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
	
	if (len(channel) != 0):
		key_wrold = channel[0].get_text()
		#print key_wrold
		if (key_wrold != '下一张'.decode('utf-8')):
			return None
	else:
		return None

	new_page = channel[0].get('href')
	next_url = current_url[0:current_url.find('/', 8) + 1] + new_page
	return next_url

def GetEncoding():
	return 'utf-8'

def GetSavePath():
	save_path = sys.path[0] + '\\mmjpg'
	return save_path

def LoadConfDoc():
	return  'mmjpg.com web splider'

def Init():
	Web_mod.NewWeb(LoadConfName, LoadConfPageHeaders, LoadConfPicHeaders, LoadConTitleRules, LoadConImgRules, GetNextPage, GetEncoding, GetSavePath, LoadConfDoc)
