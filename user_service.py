# coding=utf-8
"""
Created on 2017-07-12

@Filename: user_service
@Author: Gui


"""
from utils.epClient import EPClient


if __name__ == '__main__':
    order_service = EPClient('http://192.168.30.101:10100')
    payload = {
        "action": "login",
        "request": {
            "password": "password",
            "username": "gui.yun@e-ports.com"
        }
    }
    res = order_service.post(payload)
    print(res.status_code)
