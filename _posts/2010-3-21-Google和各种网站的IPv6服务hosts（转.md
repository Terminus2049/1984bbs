---
layout: default

date: 2010-3-21

title: Google和各种网站的IPv6服务hosts（转

categories: 国家局域网研究所

---





# Google和各种网站的IPv6服务hosts（转



flld





1楼 大 中 小 发表于 2010-3-21 09:32  只看该作者



Google和各种网站的IPv6服务hosts（转



笔者是使用的网络是普通家庭用ADSL，Windows7操作系统，无须任何设置添加即可使用。  

XP默认是没有安装ipv6的，所以要运行 ipv6 /install 进行安装。  

想要利用ipv6访问某个网站，就需要该网站本身拥有ipv6地址，照hosts文件内容格式添加即可。  

\-----------------------------------------------------------------------------------------  

看到好多朋友都在用puff，其实如果用ipv6就可以直接连接了，不需要什么翻墙代理。并非原创，只是看到大家似乎更新的比较辛苦。。。  

把hosts.rar中的文件放到C:\windows\system32\drivers\etc下覆盖即可。  

hosts文件内容来自 谷歌文档： Google和各种网站的IPv6服务hosts  

不过可能有些朋友连 Google Docs 也进不去。。。因此直接把完好的hosts文件打包上传了。  

嗯，看 youtube，上Twitter都很正常。  

  

我在自己机器Windows7上一直使用的很好，不过据说XP要用 ipv6 /install 后才能使用。。。  

下面是部分 hosts 内容。。。。  

#Google和各种网站的IPv6服务hosts  

#利用IPv6技术翻墙，保证Google服务可用，校园网用户使用IPv6应该不收取上网费用（至少我们学校如此）  

#最下方有各种网站的IPv6hosts列表  

#欢迎转载，请注明来源，谢谢  

#本文的发布地址：http://docs.google.com/View?id=dfkdmxnt_61d9ck9ffq  

#本文的共享链接：http://docs.google.com/Doc?docid ... OWZmcQ&hl=zh_CN  

#表格版的host列表地址：http://spreadsheets.google.com/c ... U5ycmc&hl=zh_CN  

#有新的Google地址需要添加？请在这里提交，帮助我完善此列表，谢谢～  

#欢迎穿越传阅  

#大幅更新！请往下看！所有GoogleIPv6地址变更！支持https加密！  

  

  

  

#hosts文件位置：  

#C:\Windows\System32\drivers\etc （Windows中）  

#/etc （Linux中）  

#用文本打开hosts文件，复制以下内容到hosts文件中，保存即可（hosts文件没有后缀）  

#关闭某个IPv6的转发请在那一行的最前面添加#号，启用请去除最前面#号，每行中间的#号是为了区分地址和注释，不用理睬- -  

  

  

  

# Copyright (c) 1993-2006 Microsoft Corp.  

#  

# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.  

#  

# This file contains the mappings of IP addresses to host names. Each  

# entry should be kept on an individual line. The IP address should  

# be placed in the first column followed by the corresponding host name.  

# The IP address and the host name should be separated by at least one  

# space.  

#  

# Additionally, comments (such as these) may be inserted on individual  

# lines or following the machine name denoted by a '#' symbol.  

#  

# For example:  

#  

# 102.54.94.97 rhino.acme.com # source server  

# 38.25.63.10 x.acme.com # x client host  

  

  

127.0.0.1 localhost  

::1 localhost  

  

  

  

  

  

Google网站  

  

  

  

#下列红色地址为官方给出的准确地址，可以使用正确的https加密连接  

#以下列表中地址以亚洲太平洋服务器Address (Asia-Pacific)为主（2001:4860:8004::*）  

Google.com Google.com  

2001:4860:8004::62 google.com #主页  

2001:4860:8004::c1 m.google.com #Google移动版  

2001:4860:8004::54 accounts.google.com #帐户  

2001:4860:8004::62 id.google.com #帐号登录  

2001:4860:8004::62 id.l.google.com #  

2001:4860:8004::62 gg.google.com #广告？  

2001:4860:8004::62 safebrowsing.clients.google.com #安全浏览客户端服务器  

2001:4860:8004::62 ns1.google.com #域名系统服务器ns-soa/ns  

2001:4860:8004::62 ns2.google.com #域名系统服务器ns  

2001:4860:8004::62 ns3.google.com #域名系统服务器ns  

2001:4860:8004::62 ns4.google.com #域名系统服务器ns  

2001:4860:8004::62 services.google.com #服务申请  

2001:4860:8004::62 feedproxy.google.com #Feed代理  

2001:4860:8004::d2 jmt0.google.com #未知  

2001:4860:8004::62 googlemashups.l.google.com #位置  

Google.cn 谷歌  

2401:3800:c001::2c www.google.cn #主页  

2401:3800:c001::2c g.cn #主页  

  

2401:3800:c001::2c google.cn #主页  

  

2401:3800:c001::2c ipv6cn.l.google.com  

#IPv6：ipv6.google.cn  

Google.com.tw Google台湾  

2001:4860:8004::2f www.google.com.tw #主页  

2001:4860:8004::2f picasaweb.google.com.tw #picasaweb  

  

Google.co.jp Google日本  

2a00:1450:8006::30 www.google.co.jp  

#IPv6：ipv6.google.co.jp  

完整hosts   文件打包下载：http://freakshare.net/files/r9g7 ... -----hosts.rar.html  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



123ddw



逼事球办





2楼 大 中 小 发表于 2010-4-9 16:17  只看该作者



真找这个嘞，顶起！  

  

  





  

SrAcer



党强加于人的世界观在无法理解它的人们那里最容易被接受。——《１９８４》





3楼 大 中 小 发表于 2010-4-9 20:25  只看该作者



谢谢！赞！  

  

  





  

shanyun





4楼 大 中 小 发表于 2010-4-11 12:49  只看该作者



赞一个  虽然我不用IP6  

  

  





  

isonomy





5楼 大 中 小 发表于 2010-4-11 14:57  只看该作者



试用成功  

  

  





  

神仙一溜烟



杵君





6楼 大 中 小 发表于 2010-4-11 17:25  只看该作者



如果原先能翻墙的， 再用这个会不能翻墙。  

  

  





  

askboy





7楼 大 中 小 发表于 2010-4-12 12:31  只看该作者



2001:4860:8004::62这种类似的就是ipv6地址  

是否与之前的ipv4地址一样  可以直接复制到地址栏进入    测试当前网络是否支持ipv6  

  

  





  

寂寞的影子





8楼 大 中 小 发表于 2010-4-14 18:36  只看该作者



有点技术性的文章，做下好好看看  

  

  





  

风中凌乱





9楼 大 中 小 发表于 2010-4-14 18:38  只看该作者



引用:



> 原帖由 那个谁 于 2010-4-14 12:58 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  有没有xp 装好了的？我用 ipv6 install 了之后还是不行。网上文章

> http://ipv6.jx.edu.cn/ipv6-cfgXP.htm 说还要做隧道连接，，，这个要连到哪里啊？  

>  

>  4、如果你是在IPV4网络中，你需要与IPV6网络进行隧道连 ...



直接把命令敲进去就可以了  

  

  





  

听到涛声





10楼 大 中 小 发表于 2010-4-14 22:23  只看该作者



ipv6果然是好东东，ipv4的hosts出一个封一个……  

  

  







  

babyss92548





11楼 大 中 小 发表于 2010-4-25 00:17  只看该作者



更新了吗  twitter上不去吧  

  

  





  

ottovon



@ottovonconstant





12楼 大 中 小 发表于 2010-4-25 02:03  只看该作者



留中，IPV6很快要来了~  

  

  







  





















    







    













