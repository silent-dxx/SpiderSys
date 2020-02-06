#-*-coding:utf-8-*-

import sys

Web_Mod_List = {
}

class WebPlatform():
	def __init__(self, web_name):
		self.FuncList = Web_Mod_List[web_name]

	def get_page_headers(self):
		return self.FuncList[0]()

	def get_pic_headers(self):
		return self.FuncList[1]()

	def get_title_rules(self):
		return self.FuncList[2]()
	
	def get_img_rules(self):
		return self.FuncList[3]()

	def get_next_page(self, args0, args1):
		return self.FuncList[4](args0, args1)

	def get_curr_encoding(self):
		return self.FuncList[5]()

	def get_save_path(self):
		return self.FuncList[6]()

	def get_doc(self):
		return self.FuncList[7]()

def GetWebPlatform(web_name):
	if web_name not in Web_Mod_List.keys():
		return None
	web = WebPlatform(web_name = web_name)
	return web


def NewWeb(web_name, page_headers, pic_headers, title_rules, img_rules, next_page, curr_encoding, save_path, doc):
	web_name = web_name()
	if web_name in Web_Mod_List.keys():
		string = "%s already exists" % (web_name)
		print string
		return False

	Web_Mod_List[web_name] = []
	Web_Mod_List[web_name].append(page_headers)
	Web_Mod_List[web_name].append(pic_headers)
	Web_Mod_List[web_name].append(title_rules)
	Web_Mod_List[web_name].append(img_rules)
	Web_Mod_List[web_name].append(next_page)
	Web_Mod_List[web_name].append(curr_encoding)
	Web_Mod_List[web_name].append(save_path)
	Web_Mod_List[web_name].append(doc)	
	#print 'NewWeb %s is ok!!\n' % (web_name)
	return True
