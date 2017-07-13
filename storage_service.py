# coding=utf-8
"""
Created on 2017-07-12

@Filename: storage_service
@Author: Gui


"""
import os
from utils.epClient import EPClient


if __name__ == '__main__':
    storage_service = EPClient('http://192.168.30.101:10200')
    file = r'.\files\test.png'
    payload = {'action': 'storeFile'}
    r = storage_service.post_with_file(payload, file)
    print(r.status_code)
    print(r.text)

    file1 = r'.\files\test.png'
    file2 = r'.\files\a.html'
    files = [os.path.abspath(file1), os.path.abspath(file2)]
    print(files)
    r = storage_service.post_with_files(payload, files)
    print(r.status_code)
    print(r.text)
