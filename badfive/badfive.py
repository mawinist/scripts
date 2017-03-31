#!/usr/bin/env python
## -*- coding: UTF-8 -*-
import paramiko
import time
f = open('test.txt')
log = open('test.log', 'a')
for line in f.readlines():
    localtime = time.asctime(time.localtime(time.time()))
    ip = line   # set ip_address
    username = 'admin'
    password = 'ak47McOOl'
    log.write(localtime + "\n" + "Now usg-40 is: " + ip + "\n")  # write on log the address
    try:
        ssh = paramiko.SSHClient()  # start SSH client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # yes on ssh key
        ssh.connect(ip, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)

        ssh_new = ssh.invoke_shell()
        output = ssh_new.recv(65535)
        ssh_new.send("ping 8.8.8.8 count 5\n")
        time.sleep(5.0)
        output = ssh_new.recv(65535)
        log.write(output + "\n")

        ssh_new.send("show interface cellular device-status\n")
        time.sleep(5.0)
        output = ssh_new.recv(65535)
        log.write(output + "\n")
        log.write("_____________________________________________\n")
        log.write("\n")
    except:
        log.write("Error connect")
        log.write("_____________________________________________\n")
        log.write("\n")
f.close()
log.close()


