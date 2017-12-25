# coding=utf-8
"""
Created on 2017-12-25

@Filename: b
@Author: Gui


"""

import time
from gol_demo import log_config

logger = log_config.global_logger


def timeit(func):
    def wrapped(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = '%.3f' % (t2 - t1)
        logger.debug('{} costs {} s.'.format(func.__name__, t))
        return result

    return wrapped
