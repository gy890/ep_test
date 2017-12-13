# coding=utf-8
"""
Created on 2017-07-13

@Filename: upload_file
@Author: Gui


"""
import requests
import mimetypes
import os


def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0] or 'application/octet-stream'


payload = {'action': 'storeFile'}
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            }

url = "http://192.168.30.102:10200/"
file1 = r'.\files\test.png'
file2 = r'.\files\a.html'
# file3 = r'.\files\Capture001.png'
file3 = r'.\files\bb.xls'
# files = {'file1': (os.path.basename(file1), open(file1, 'rb'), 'Content-Type: %s' % get_content_type(file1))}
files = [('file1', (os.path.basename(file1), open(file1, 'rb'), 'Content-Type: %s' % get_content_type(file1))),
         ('file2', (os.path.basename(file2), open(file2, 'rb'), 'Content-Type: %s' % get_content_type(file2))),
         ('file3', (os.path.basename(file3), open(file3, 'rb'), 'Content-Type: %s' % get_content_type(file3)))
         ]
response = requests.request("POST", url, data=payload, files=files, headers=headers)
r = requests.post(url, data=payload, files=files)
print(response.text)



