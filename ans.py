#!/usr/bin/python
# coding:utf-8

import sys,os
import ConfigParser
import commands
import pexpect
from  script.ansible import *

#解析配置文件
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

#执行ansible命令
def exeAns(ans):
    cmd = "ansible 10.107.105.143 -m shell -a 'pwd'"
    a,b = commands.getstatusoutput(cmd)
    print a
    print b
    print 'ans port is :', ans.getPort()

#执行shell命令
def exeShell(cmd):
    a,b = commands.getstatusoutput(cmd)
    print a
    print b

#安装ansible
def installAns():
    exeShell("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
    exeShell('yum install -y ansible')

#生成ssh密钥
def generateKeygen():
    child = pexpect.spawn("ssh-keygen")
    index = child.expect(["Enter file in which to save the key", pexpect.EOF, pexpect.TIMEOUT])
    print 'installing'
    if( index == 0 ):
        print 'installing'
        child.sendline('\n')
        index = child.expect(["empty for no passphrase", "Overwrite", pexpect.EOF, pexpect.TIMEOUT])
        if( index == 0 ):
            child.sendline('\n')
            index = child.expect(["Enter same passphrase again:", pexpect.EOF, pexpect.TIMEOUT])
            if( index == 0 ):
                print 'installing'
                child.sendline('\n')
                index = child.expect(["The key's randomart image is:", pexpect.EOF, pexpect.TIMEOUT])
                if (index != 0):
                    print 'install ansible faild 4'
                print 'install ansible success'
            else:
                print 'install ansible faild 3'
                child.close(force=True)
        elif (index == 1):
            print 'already install,exit'
            child.close(force=True)
        else:
            print 'install ansible faild 2'
            child.close(force=True)
    else:
        print "install ansible faild 1"
        child.close(force=True)

#复制ssh密钥到对应ip
def copyKeygen(ip, passwd):
    child = pexpect.spawn("ssh-copy-id root@%s" % ip)
    index = child.expect(["continue connecting", 'password:', 'already exist on the remote system', pexpect.EOF, pexpect.TIMEOUT])
    print 'installing'
    if( index == 0 ):
        print 'installing'
        child.sendline('yes')
        index = child.expect(['password:', pexpect.EOF, pexpect.TIMEOUT])
        if( index == 0 ):
            child.sendline('%s' % passwd)
            index = child.expect(["you wanted were added", pexpect.EOF, pexpect.TIMEOUT])
                        if (index != 0):
                print 'add faild 4'
                child.close(force=True)
            print 'add success'
        else:
            print 'add faild 2'
            child.close(force=True)
    elif (index == 2):
        print 'Keygen already exist on the remote system'
    else:
        print "install ansible faild 1"
        child.close(force=True)

#执行ansible命令,安装nmon
def installNmon(ans, ip):
    exeShell("ansible %s -m yum -a 'state=present name=nmon'" % ip)
    exeShell("ansible %s -m shell -a 'nmon -s1 -c60 -f -m /root/nmon'" % ip)
    exeShell("ansible %s -m fetch -a 'src=/root/VM_105_143_centos_180925_1115.nmon dest=/data1/gavinouyang/test/perftset'" % ip)
    exeShell("ansible %s -m synchronize -a 'src=/root/nmon dest=/data1/gavinouyang/test/perftset/{{inventory_hostname}}/  mode=pull'" % ip)

if __name__ == "__main__":
#new一个ans对象用来存储配置
    ans = Ans()
#解析配置文件，存储到ans对象中
    parser("./conf/config.ini", ans)
#安装ansible
    installAns()
#生成密钥
    generateKeygen()
#copy密钥到对端
    copyKeygen('10.107.105.143', '')passwd
#安装nmon
    installNmon(ans, '10.107.105.143')
#启动nmon

#收集nmon数据

