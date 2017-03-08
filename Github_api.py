# -*- coding: utf-8 -*-
# User api 的试用
import json
import requests

URL = "https://api.github.com"

def build_uri(endpoing):
	return '/'.join([URL, endpoing])

def better_print(json_str):
	return json.dumps(json.loads(json_str), indent = 4)

def reques_method():
	response = requests.get(build_uri("users/Criya"))
	print(better_print(response.text))

if __name__ == '__main__':
	reques_method()