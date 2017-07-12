# coding=utf-8
"""
Created on 2017-06-13

@Filename: test_class
@Author: Gui


"""
import allure


class TestClass(object):
    @allure.step('aaaaaaaaa')
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'Hello'
        assert hasattr(x, 'check')
