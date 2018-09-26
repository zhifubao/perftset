# coding:utf-8

import sys,os


class Ans:
    """ansible配置
    """
    ip = ''
    port = ''
    def set(self, ip, port):
        self.ip = ip
        self.port = port

    def setIp(self, ip):
        self.ip = ip

    def getIp(self):
        return self.ip


    def setPort(self, port):
        self.port = port

    def getPort(self):
        return self.port
