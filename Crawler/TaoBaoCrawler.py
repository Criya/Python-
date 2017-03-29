#爬取淘宝输入商品的价格信息
import re
import requests

def get_html_text(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
		response.encoding = response.apparent_encoding
		return response.text
	except:
		return "error"

def parase_page(info_list, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			info_list.append([price, title])
	except:
		return "error"

def print_list(info_list):
	module = "{:4}\t{:8}\t{:16}"
	print(module.format("序号", "价格", "商品名称"))
	count = 0
	for i in info_list:
		count += 1
		print(module.format(count, i[0], i[1]))

def main():
	print("主人，请输入你想搜索的物品名：")
	goods = input()
	depth = 1
	start_url = 'https://s.taobao.com/search?q=' + goods
	info_list = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(i * 44)
			html = get_html_text(url)
			parase_page(info_list, html)
		except:
			continue
	print_list(info_list)

main()