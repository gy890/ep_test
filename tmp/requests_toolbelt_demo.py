# coding=utf-8
"""
Created on 2017-07-14

@Filename: requests_toolbelt_demo
@Author: Gui


"""
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

multipart_data = MultipartEncoder(
    fields={
            # a file upload field
            'file1': ('file.py', open(r'..\files\笔记.xls', 'rb'), 'text/plain'),
            'file2': ('file.py', open(r'..\files\a.html', 'rb'), 'text/plain'),
            # plain text fields
            'action': 'storeFile',
           }
    )

# response = requests.post('http://httpbin.org/post', data=multipart_data,
#                   headers={'Content-Type': multipart_data.content_type})

response = requests.post('http://192.168.30.101:10200', data=multipart_data,
                  headers={'Content-Type': multipart_data.content_type})
print(multipart_data.content_type)
print(response.content)