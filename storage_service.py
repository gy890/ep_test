# coding=utf-8
"""
Created on 2017-07-12

@Filename: storage_service
@Author: Gui


"""
import os
import mimetypes
from utils.epClient import EPClient


def get_content_type(filepath):
    return mimetypes.guess_type(filepath)[0] or 'application/octet-stream'


def encode_multipart_formdata(filepath):
    boundary = 'EportsHttpTest'
    crlf = '\r\n'
    l = ['--' + boundary, 'Content-Disposition: form-data; name=" "; filename="%s"' % (os.path.basename(filepath)),
         'Content-Type: %s' % get_content_type(filepath), '', '', open((file), 'rb').read(),
         '--' + boundary, 'Content-Disposition: form-data; name="action"', '', 'storeFile', '--' + boundary + '--']
    data = crlf.join(l)

    content_type = 'multipart/form-data; boundary=%s' % boundary
    return content_type, data

if __name__ == '__main__':
    storage_service = EPClient('http://192.168.30.101:10200')
    file = r'.\files\Capture001.png'
    f = open((file), 'rb').read()
    print(f)
    content_type, body = encode_multipart_formdata(file)
    r = storage_service.post_with_file(body, content_type)
    print(r.status_code)
    print(r.text)

