# -*- coding: utf-8 -*-
import requests

# 原URL: http://httpbin.org/ 利用gunicorn搬到本机
#
URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print('>>>>Response Headers:')
    print(response.headers)
    print('>>>>Response body:')
    print(response.text)


def use_params_requests():
    # 构建请求参数
    params = {'param1': 'hello', 'params2': 'world'}

    # 发送请求
    response = requests.get(URL_GET, params=params)
    # 处理响应
    print('>>>>Response Headers:')
    print(response.headers)
    print(">>>>Status Code:")
    print(response.status_code)
    print('>>>>Response body:')
    print(response.text)

if __name__ == '__main__':
    print("Use simple requests: ")
    use_simple_requests()
    use_params_requests()
