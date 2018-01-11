# coding=utf-8
"""
Created on 2018-01-10

@Filename: basicConfig_demo
@Author: Gui


"""
import logging

logging.basicConfig(level=logging.DEBUG,
                    # format='%(asctime)s - %(levelname)s - %(message)s',
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='test.log',
                    # filemode='w',
                    )
logging.info('test')
