# coding=utf-8
"""
Created on 2017-07-12

@Filename: http_client
@Author: Gui


"""
import requests
import json


class EPClient(object):
    def __init__(self, url):
        self.url = url

    def post(self, data):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json'}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        return r

    def post_with_cookie(self, data, cookie):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json',
            'cookie': cookie}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        return r

    def post_with_xSessionId(self, data, cookie):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json',
            'x-session-id': cookie}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        return r

    def post_with_file(self, data, content_type):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': content_type}
        r = requests.post(self.url, data=data, headers=headers)
        return r

