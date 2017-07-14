# coding=utf-8
"""
Created on 2017-07-12

@Filename: http_client
@Author: Gui


"""
import requests
import json
import os
import mimetypes


def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0] or 'application/octet-stream'


class EPClient(object):
    def __init__(self, url):
        self.url = url

    def post(self, data):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json'}
        res = requests.post(self.url, data=json.dumps(data), headers=headers)
        return res

    def post_with_cookie(self, data, cookie):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json',
            'cookie': cookie}
        res = requests.post(self.url, data=json.dumps(data), headers=headers)
        return res

    def post_with_xSessionId(self, data, cookie):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json',
            'x-session-id': cookie}
        res = requests.post(self.url, data=json.dumps(data), headers=headers)
        return res

    def post_with_file(self, data, file):
        files = {'fileupload': (os.path.basename(file), open(file, 'rb'), 'Content-Type: %s' % get_content_type(file))}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',}
        res = requests.post(self.url, data=data, files=files, headers=headers)
        return res

    def post_with_files(self, data, files_path):
        multiple_files = []
        for k, fp in enumerate(files_path, 1):
            file = (str(k), (os.path.basename(fp), open(fp, 'rb'), 'Content-Type: %s' % get_content_type(fp)))
            multiple_files.append(file)
        print(multiple_files)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',}
        res = requests.post(self.url, data=data, files=multiple_files, headers=headers)
        return res

