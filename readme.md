#自动监控上报


性能监控：nmon atop
分发监控脚本：ansible
收集监控数据：ansible
分析excel汇总数据
发送邮件


ansible配置

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

4：配置ssh，配置完key后，需要在sshd_config文件中开启key认证
$ vim /etc/ssh/sshd_config
PubkeyAuthentication yes  //将该项改为yes 

5：修改完成后，通过/etc/init.d/sshd restart 重启ssh服务重新加载配置。如果想要禁用密码认证，更改如下项：

$ vim /etc/ssh/sshd_config
UsePAM yes
为
UserPAM no
之后添加托管服务器ip至ansible配置中

vim /etc/ansible/hosts
修改如下图所示：

[servers]
10.107.105.81 ansible_ssh_user=asherli  ansible_sudo_pass='123'
10.107.105.137 ansible_ssh_user=asherli  ansible_sudo_pass='123'
10.107.105.141 ansible_ssh_user=asherli  ansible_sudo_pass='123'
