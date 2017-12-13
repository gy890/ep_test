# coding=utf-8
'''
Created on 2017-04-24

@Filename: login
@Author: Gui


'''
import requests
import json

import logging
import contextlib
from http.client import HTTPConnection


def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger('requests.packages.urllib3')
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def debug_requests_off():
    '''Switches off logging of the requests module, might be some side-effects'''
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger('requests.packages.urllib3')
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    '''Use with 'with'!'''
    debug_requests_on()
    yield
    debug_requests_off()


debug_requests_off()


def login():
    payload = {
        "action": "login",
        "request": {
            "password": "password",
            "username": "gui.yun@e-ports.com"
        }
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'}

    r = requests.post('http://192.168.30.102:10100', data=json.dumps(payload), headers=headers)
    # print('type(r): {}'.format(type(r)))
    # print('request headers: {}'.format(r.request.headers))
    # print('content-type: {}'.format(r.headers['content-type']))
    print('status_code: {}'.format(r.status_code))
    # print('response headers: {}'.format(r.headers))
    # print('elapsed {} s'.format(r.elapsed))
    # print('encoding: {}'.format(r.encoding))
    # print('response json: {}'.format(r.json()))
    # print(type(r.json()))
    print(type(r.text), r.text)
    # print(type(r.content), r.content)


def find_acount_by_id():
    payload = {"action": "findAccountById",
               "request.id": "58491f3190fc6203a58499a2"}
    print(payload)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'content-type': 'application/json',
        'x-session-id': 'ivMGauOp%b0YyMH0L@tFclg6YMborr@hCZxYjW0AkA3#j#ilHiDuwODXwVkX#cBx'}
    r = requests.post('http://192.168.30.101:10100', data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

login()
# find_acount_by_id()
