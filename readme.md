#自动监控上报


性能监控：nmon atop
分发监控脚本：ansible
收集监控数据：ansible
分析excel汇总数据
发送邮件


ansible
1：管理节点生成SSH-KEY

#ssh-keygen
成功后在~/.ssh/路径下将生成ssh密钥文件：id_rsa及id_rsa.pub

 

2：添加目标节点的SSH认证信息

#ssh-copy-id root@目标节点IP
这里root是在目标节点上登录的用户，@符号后面接目标节点IP即可，之后会提示输入目标节点root用户密码，输入即可。

添加认证信息后，目标节点主机的~/.ssh/目录下将会出现一个authorized_keys文件，里面包含了ansible管理节点的公钥信息，可以检查一下是否存在。

3：在确定目标主机的SSH认证信息都已正确添加且目标主机的~/.ssh/目录都存在管理节点的公钥信息后，再执行之前出错的ansible ping指令：

#ansible -m ping all

---------------------

本文来自 qq_33324608 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/qq_33324608/article/details/54407108?utm_source=copy 
