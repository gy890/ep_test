# coding=utf-8
"""
Created on 2017-07-11

@Filename: ep_ssh
@Author: Gui


"""
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.30.101', 22, 'epadmin', '!QAZ2wsx')
# stdin, stdout, stderr = ssh.exec_command('ls')
# for line in stdout:
#     print('... ' + line.strip('\n'))
# print(ssh.exec_command('pwd'))
print(ssh.get_host_keys())
ssh.close()
