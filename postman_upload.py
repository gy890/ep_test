# coding=utf-8
"""
Created on 2017-07-12

@Filename: postman_upload
@Author: Gui


"""
import requests

url = "http://192.168.30.102:10200/"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"\"; filename=\"Capture001.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"action\"\r\n\r\nstoreFile\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "f84157f5-1027-3c98-e537-06c64d38de2c"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)