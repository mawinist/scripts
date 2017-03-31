#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import paramiko
import logging
import time
# define log config
logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename='mylog.log')
logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.DEBUG)
# Сообщение отладочное
logging.debug('This is a debug message')
# Сообщение информационное
logging.info('This is an info message')
# Сообщение предупреждение
logging.warning('This is a warning')
# Сообщение ошибки
logging.error('This is an error message')
# Сообщение критическое
logging.critical('FATAL!!!')

# open files
log = open('loop.log', 'a')
f = open('ip.csv')
# start the loop
for line in f.readlines():
    localtime = time.asctime(time.localtime(time.time()))
    ip = line   # set ip_address
    log.write(localtime + "\n" + "Now usg-40 is: " + ip + "\n")   # write on log the address
    username = 'admin'
    password = 'ak47McOOl'
    try:
        ssh = paramiko.SSHClient()  # start SSH client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # yes on ssh key
        ssh.connect(ip, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
        ssh_new = ssh.invoke_shell()
        output = ssh_new.recv(65535)# ukazat` kakoy terminal, nugno dlya print

        ssh_new.send("configure terminal\n")
        time.sleep(.5)
        output = ssh_new.recv(65535)
        print(ip, output)

        ssh_new.send("cnm-agent activate\n")
        ssh_new.send("cnm-agent manager https://192.168.215.210:7547/CAPFWYOO06\n")
        ssh_new.send("cnm-agent periodic-inform activate\n")
        ssh_new.send("cnm-agent periodic-inform interval 900\n")
        ssh_new.send("write\n")
        time.sleep(.5)
        output = ssh_new.recv(65535)# ukazat` kakoy terminal, nugno dlya print
        print(ip)
        print(output)
        log.write("All done on this device!\n")
        log.write("_____________________________________________\n")

    except:
        log.write("Error connected: " + ip + "_____________________________________________\n")

f.close()
log.close()

