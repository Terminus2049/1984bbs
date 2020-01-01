---
layout: default

date: 2009-9-27

title: UltraVPN

categories: 国家局域网研究所

---





# UltraVPN 中国补丁



gmbert





1楼 大 中 小 发表于 2009-9-27 22:54  只看该作者



UltraVPN 中国补丁



http://www.ultravpn.fr/forum/index.php?topic=195.0  

  

把这个配置文件拷贝并覆盖 Program Files\UltraVPN\config\ 原来的那个  

通过测试了  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



txj1984





2楼 大 中 小 发表于 2009-9-27 23:01  只看该作者



真的假的，这么牛叉？  

  

  









  

txj1984





3楼 大 中 小 发表于 2009-9-27 23:01  只看该作者



我怀疑其动机，第一，为什么在这个时期，他没有被阻断  

第二，为什么没阻断反而出补丁呢？是不是他和TG有合作关系？  

  

  









  

alexander982



肆零贰壹号组员//道貌岸然的知心大哥//伪爱情专家//傻*英雄主义者//一个烤鸭的传说





4楼 大 中 小 发表于 2009-9-27 23:10  只看该作者



怎么下载？  

  

  





  

gmbert





5楼 大 中 小 发表于 2009-9-27 23:11  只看该作者



帖子右边有个 client.ovpn的链接符号，点击下载  

  

  





  

小猪依人



一小撮





6楼 大 中 小 发表于 2009-9-27 23:32  只看该作者



我怎么找不到下载的地儿?  

  

  





  

702781



路逢剑客须呈剑。不是诗人不献诗





7楼 大 中 小 发表于 2009-9-28 06:07  只看该作者



那个config原始网站反而没有了？！谁能提供一个？  

  

  





  

北国游子



真诚、坦荡，狂热、执着，无怨无悔、嫉恶如仇





8楼 大 中 小 发表于 2009-9-28 12:37  只看该作者



是不是要登录了才能看到下载链接？  

  

  







  

北国游子



真诚、坦荡，狂热、执着，无怨无悔、嫉恶如仇





9楼 大 中 小 发表于 2009-9-28 13:31  只看该作者



哪位已经下载到client.ovpn的朋友，用记事本把这个文件打开，把文本内容复制在这里？  

  

  







  

nustbobo



不明真相的群众，目睹俯卧撑、躲猫猫、撞墙死、临时工等一系列怪





10楼 大 中 小 发表于 2009-9-28 13:34  只看该作者



引用:



> 原帖由 txj1984 于 2009-9-27 23:01 发表

> ![](http://1984bbs.com/images/common/back.gif)  

>  我怀疑其动机，第一，为什么在这个时期，他没有被阻断  

>  第二，为什么没阻断反而出补丁呢？是不是他和TG有合作关系？



有些人不用TG出手，自己就能把自己吓死。  

  

  





  

702781



路逢剑客须呈剑。不是诗人不献诗





11楼 大 中 小 发表于 2009-9-28 15:03  只看该作者



引用:



> 原帖由 北国游子 于 2009-9-28 13:31 发表 ![](http://1984bbs.com/images/common/back.gif)  

>  哪位已经下载到client.ovpn的朋友，用记事本把这个文件打开，把文本内容复制在这里？



我终于下载到了，原来需要注册，connect连接中，stealth还没弄，应你要求把配置内容贴出来，就是加了2个ip来暂时抵抗域名劫持  

  

  

  

client  

  

dev tun  

  

proto udp  

  

hand-window 15  

  

remote-random  

  

#remote servers443.ultravpn.fr 443  

#remote servers24.ultravpn.fr 24  

#remote servers21.ultravpn.fr 21  

#remote servers54.ultravpn.fr 54  

#remote servers24.ultravpn.net 24  

#remote servers443.ultravpn.net 443  

remote 76.73.3.162 443  

remote 87.98.164.142 443  

  

  

resolv-retry infinite  

  

nobind  

  

  

# Try to preserve some state across restarts.  

persist-key  

persist-tun  

  

  

ca ca.crt  

  

  

# Enable compression on the VPN link.  

# Don't enable this unless it is also  

# enabled in the server config file.  

comp-lzo  

  

# Set log file verbosity.  

verb 3  

  

auth-user-pass  

  

  





  

北国游子



真诚、坦荡，狂热、执着，无怨无悔、嫉恶如仇





12楼 大 中 小 发表于 2009-9-28 16:14  只看该作者



谢谢楼上！  

  

  







  

北国游子



真诚、坦荡，狂热、执着，无怨无悔、嫉恶如仇





13楼 大 中 小 发表于 2009-9-28 16:33  只看该作者



仍然不能连接  

  

  







  

WJ87



无产阶级煽动家





14楼 大 中 小 发表于 2009-9-28 16:39  只看该作者



等测试结果  

  

  





  

cfsalex



真理,即使被践踏在地,也会站起来:上帝永恒的岁月属于他;但谬误一旦受伤,便会就地打滚,然后在其崇拜者中间咽气





15楼 大 中 小 发表于 2009-9-29 17:55  只看该作者



mark  

  

  





  

蚊驱





16楼 大 中 小 发表于 2009-9-29 23:34  只看该作者



可用，ultravpn已恢复，谢谢。  

  

  





  

Phillip



路边社特邀围观群众





17楼 大 中 小 发表于 2009-9-30 00:07  只看该作者



client  

  

dev tun  

  

proto udp  

  

hand-window 15  

  

remote-random  

  

#remote servers443.ultravpn.fr 443  

#remote servers24.ultravpn.fr 24  

#remote servers21.ultravpn.fr 21  

#remote servers54.ultravpn.fr 54  

#remote servers24.ultravpn.net 24  

#remote servers443.ultravpn.net 443  

remote 76.73.3.162 443  

remote 87.98.164.142 443  

  

  

resolv-retry infinite  

  

nobind  

  

  

# Try to preserve some state across restarts.  

persist-key  

persist-tun  

  

  

ca ca.crt  

  

  

# Enable compression on the VPN link.  

# Don't enable this unless it is also  

# enabled in the server config file.  

comp-lzo  

  

# Set log file verbosity.  

verb 3  

  

auth-user-pass  

  

  





  

adhome





18楼 大 中 小 发表于 2009-9-30 08:22  只看该作者



还是不能  

  

  





  

蚊驱





19楼 大 中 小 发表于 2009-9-30 17:49  只看该作者



一天就失效了，是否还有新的补丁？  

  

  





  





















    







    













