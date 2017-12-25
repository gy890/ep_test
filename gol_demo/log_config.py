# coding=utf-8
"""
Created on 2017-12-25

@Filename: a
@Author: Gui


"""
import os
import logging.config

if os.path.exists('mylog.log'):
    os.remove('mylog.log')
logging.config.fileConfig('logging.conf', defaults={'logfilename': 'mylog.log'})
logging.config.fileConfig('logging.conf', defaults={'logfilename': 'mylog.log'})
logger = logging.getLogger('sLogger')

global global_logger
global_logger = logger
