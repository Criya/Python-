# -*- coding: utf-8 -*-
import urllib2
import urllib

# 原URL: http://httpbin.org/ 利用gunicorn搬到本机
# 
URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'


def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print'>>>>Response Headers:'
    print response.info()
    print'>>>>Response body:'
    print ''.join([line for line in response.readlines()])


def use_params_urllib2():
	# 构建请求参数
	params = urllib.urlencode({'param1': 'hello', 'params2': 'world'})
	print 'Request params:'
	print params
	# 发送请求
	response = urllib2.urlopen('?'.join([URL_GET, params]))
	# 处理响应
	print '>>>>Response Headers:'
	print response.info()
	print '>>>>Status Code:'
	print response.getcode()
	print'>>>>Response body:'
	print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    print 'Use simple urllib2:'
    use_simple_urllib2()
    use_params_urllib2()
