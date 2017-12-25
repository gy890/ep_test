# coding=utf-8
"""
Created on 2017-12-25

@Filename: main
@Author: Gui


"""
import time
from gol_demo import log_config
from gol_demo import timeit


@timeit.timeit
def test():
    time.sleep(2)


logger = log_config.global_logger
logger.info('Start at {}'.format(time.asctime()))
test()
logger.info('End at {}'.format(time.asctime()))
