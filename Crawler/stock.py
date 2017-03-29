#爬取每日上深股市，股票代码爬取于东方财经网，股情爬于百度
from bs4 import BeautifulSoup
import requests
import re

#百度股票页面的编码是uff-8
def get_html_text(url, code="utf-8"):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ""

#东方财经网股票代码网页的编码是GB2312
def get_stock_list(lst, stouck_url):
	html = get_html_text(stouck_url, "GB2312")
	soup = BeautifulSoup(html, "html.parser")
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
			continue

def get_stock_info(lst, stock_info_url, file_path):
	count = 0
	for stock in lst:
		url = stock_info_url + stock + ".html"
		html = get_html_text(url)
		try:
			if html =="":
				continue
			info_dict = {}
			soup = BeautifulSoup(html, "html.parser")
			stock_info = soup.find('div', attrs = {'class' : 'stock-bets'})

			name = stock_info.find_all(attrs = {'class' : 'bets-name'})[0]
			info_dict.update({'股票名称' : name.text.split()[0]})

			key_list = stock_info.find_all('dt')
			value_list = stock_info.find_all('dd')

			for i in range(len(key_list)):
				key = key_list[i].text
				value = value_list[i].text
				info_dict[key] = value

			with open(file_path, 'a', encoding = 'utf-8') as f:
				f.write(str(info_dict) + '\n')
				count += 1
				print("\r当前进度{:.2f}%".format(count * 100 / len(lst)), end="")
		except:
			count += 1
			print("\r当前进度{:.2f}%".format(count * 100 / len(lst)), end="")
			continue

def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	save_path = '/Users/liangjiahao/Desktop/stock.txt'
	lst = []
	get_stock_list(lst, stock_list_url)
	get_stock_info(lst, stock_info_url, save_path)

main()