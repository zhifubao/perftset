#!/usr/bin/python
# coding:utf-8

import sys,os
import ConfigParser
from  script.ansible import *
import commands


def parser(cfg, ans):
    cf = ConfigParser.ConfigParser()
    cf.read(cfg)
    s = cf.sections()
    print 'section:', s

    o = cf.options("ansible")
    print 'options:', o

    ip = cf.get("ip", "ip2")
    print 'the ip is :', ip

    port = cf.get("ansible", "port")

    ans.set(ip, port)
    print 'ans port is :', ans.getPort()

def exeAns(ans):
    cmd = "ansible 10.107.105.143 -m shell -a 'pwd'"
    a,b = commands.getstatusoutput(cmd)
    print a
    print b
    print 'ans port is :', ans.getPort()



def installNmon(ans):
    cmd = "ansible 10.107.105.143 -m yum -a 'state=present name=nmon'"
    a,b = commands.getstatusoutput(cmd)
    print a
    print b

    cmd = "ansible 10.107.105.143 -m shell -a 'nmon -s1 -c60 -f -m /root/nmon'"
    a,b = commands.getstatusoutput(cmd)
    print a
    print b

    cmd = "ansible 10.107.105.143 -m fetch -a 'src=/root/VM_105_143_centos_180925_1115.nmon dest=/data1/gavinouyang/test/perftset'"
    a,b = commands.getstatusoutput(cmd)
    print a
    print b

    cmd = "ansible 10.107.105.143 -m synchronize -a 'src=/root/nmon dest=/data1/gavinouyang/test/perftset/{{inventory_hostname}}/  mode=pull'"
    a,b = commands.getstatusoutput(cmd)
    print a
    print b


if __name__ == "__main__":
#ceshi3
    ans = Ans()
    parser("./conf/config.ini", ans)
    exeAns(ans)
    installNmon(ans)
