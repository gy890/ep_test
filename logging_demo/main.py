# coding=utf-8
"""
Created on 2017-12-19

@Filename: main
@Author: Gui


"""
import os
import time
import logging.config
import timeit


@timeit.timeit
def func1():
    time.sleep(1)


@timeit.timeit
def func2():
    time.sleep(2)


if __name__ == '__main__':
    if os.path.exists('mylog.log'):
        os.remove('mylog.log')
    logging.config.fileConfig('logging.conf', defaults={'logfilename': 'mylog.log'})
    logger = logging.getLogger('sLogger')
    print('1', logger)
    logger.info('Start at {}'.format(time.asctime()))
    func1()
    func2()
    logger.info('End at {}'.format(time.asctime()))