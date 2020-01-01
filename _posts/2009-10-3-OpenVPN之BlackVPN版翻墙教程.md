---
layout: default

date: 2009-10-3

title: OpenVPN之BlackVPN版翻墙教程

categories: 国家局域网研究所

---





# OpenVPN之BlackVPN版翻墙教程



WJ87



无产阶级煽动家





1楼 大 中 小 发表于 2009-10-3 17:04  只看该作者



OpenVPN之BlackVPN版翻墙教程



作者：GFW Blog  

非常感谢热心网友赐稿！热烈欢迎大家向我们投稿，投稿信箱地址：chinagfwblog(at)gmail.com。  

  

BlackVPN概述  

  

参考http://www.liuhanyu.com/2009/09/blackvpn/  

  

免费VPN,  

注册简单无须邮箱（需要邀请码，邀请码到处都有），  

支持ssl链接（测试可以登录twitter,facebook等），  

速度还行比tor快，  

使用OpenVPN软件（等这个提供商挂了再找个别提供商的而不用换软件。）  

  

BlackVPN提供三个通道，nl,uk,usa，目前测试nl可用。  

  

说明书（English）  

https://www.blackvpn.com/support/windows/openvpn/  

  

  

软件：  

  

1.OpenVPN软件  

http://openvpn.se/download.html  

  

这个 Installation Package (Both 32-bit and 64-bit TAP driver  

included):openvpn-2.0.9-gui-1.0.3-install.exe  

  

2.BlackVPN的配置文件包 blackvpn_windows.zip  

  

下载：  

http://www.blackvpn.com/content/uploads/blackvpn_windows.zip  

  

  

中文使用手册  

  

1.注册（注册完毕会自动分配用户名和密码）  

  

https://www.blackvpn.com/  

  

InviteCode 为邀请码，目前可用的有 LastChance ，可搜索之。  

Email First Name  Last Name 可以随便填写  

country貌似随便选也没问题。  

注册完毕，会分配一个信息框内有帐户密码信息，务必保存好。  

  

例:  

Welcome to blackVPN.  

Here is your login information, SAVE IT!!  

It wont be emailed to you or displayed again.  

  

（用户名）username/login: u******  

（密码）password: *******  

  

PPTP Servers  

NL Server: vpn.blackvpn.nl  

USA Server: vpn.blackvpn.com  

UK Server: vpn.blackvpn.co.uk  

OpenVPN  

Go to Getting Started or our Support section for installation instructions.  

  

Thank you for signing up with blackVPN!  

  

\-----------------  

  

  

2.安装软件  

双击 openvpn-2.0.9-gui-1.0.3-install.exe ，一路下一步，直到安装完毕。  

  

3.配置文件，把第二个下载的 blackvpn_windows.zip  

，解压缩。把里面的全部文件（一个文件夹ssl，和三个配置文件）复制到安装盘一般为c盘下 c:\Program  

Files\OpenVPN\config\  下。  

  

\-----------------  

安装完毕，在右下角状态栏会出现一个 OpenVPN图标（类似红色拨号连接带个小地球）。  

  

在图标上，右击，出现一串菜单，选第一个blackvpn_nl（第二和第三个测试时连不上）,有个向右箭头会自动展开，单击connet(连接)，出现一个对话框需要你输入帐户名和密码，输入，单击ok。  

  

连接成功后，带小地球的图标会变绿。测试一下ip为RIPE。  

  

  

Enjoy!  

  

  

版权不要，演绎随便。  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



happybabe





2楼 大 中 小 发表于 2009-10-3 19:56  只看该作者



我感觉pptp方式比较方便  

  

  





  

小猪熊





3楼 大 中 小 发表于 2009-10-5 00:25  只看该作者



最喜欢这种不用下载软件就能使用的VPN了  真是好呀  谢谢LZ的推荐

另外还有，三个Server里只有vpn.blackvpn.nl能用，其它的全部失效  

  

  









  

BlackDream





4楼 大 中 小 发表于 2009-10-5 11:36  只看该作者



恩，离封杀不远了  

  

  





  

dada



不明真相群众





5楼 大 中 小 发表于 2009-10-5 18:08  只看该作者



这个很好，已经用了，但真正的菜鸟还是看不懂上面的说明。  

  

  





  

阳光不锈



医生的职责不是救人，而是少杀人…以为自己是风，结果遍体鳞伤才发现，原来自己是草！





6楼 大 中 小 发表于 2009-10-6 18:19  只看该作者



邀请码搜到的都不能用啊?请给个  

  

  





  

水煮肉汤





7楼 大 中 小 发表于 2009-10-6 23:04  只看该作者



回复 6楼 阳光不锈 的话题



LastChance  

  

  





  

winterwind





8楼 大 中 小 发表于 2009-10-6 23:37  只看该作者



回复 7楼 水煮肉汤 的话题



还是不能用。  

  

  





  

虎躯一震



我了个去





9楼 大 中 小 发表于 2009-10-7 23:53  只看该作者



引用:



> 原帖由 winterwind 于 2009-10-6 23:37 发表

> ![](http://1984bbs.com/images/common/back.gif)  

>  还是不能用。



可以用，前提是你要把其他需要填的地方填好，否则页面会一直提示邀请码有问题（即使邀请码LastChance是对的）  

  

  





  

小猪依人



一小撮





10楼 大 中 小 发表于 2009-10-9 16:53  只看该作者



邀请码不能用。。谁还能给个。  

  

  





  





















    







    













