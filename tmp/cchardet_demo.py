# coding=utf-8
"""
Created on 2017-07-14

@Filename: cchardet_demo
@Author: Gui


"""
import cchardet as chardet
import os

# with open(r"..\files\Capture001.png", "rb") as f:
#     msg = f.read()
#     result = chardet.detect(msg)
#     print(result)

path = r'..\files'
# for each in os.listdir(path):
#     print(each)

print(chardet.detect(os.path.abspath(path)))