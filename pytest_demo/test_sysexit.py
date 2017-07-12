# coding=utf-8
"""
Created on 2017-06-13

@Filename: test_sysexit
@Author: Gui


"""
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
