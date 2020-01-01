---
layout: default

date: 2010-3-12

title: 使用SocksCap配合SSH翻墙

categories: 国家局域网研究所

---





# 使用SocksCap配合SSH翻墙



库存袈裟



@bruceku 想象力比知识更重要。





1楼 大 中 小 发表于 2010-3-12 17:56  只看该作者



使用SocksCap配合SSH翻墙



1984BBS原创教程，欢迎转载，转载请注明出处。  

=========================  

  

适用范围：  

1.非Firefox浏览器  

2.下载软件  

3.无法设置代理的网络软件  

4.网络游戏  

  

1.准备所需软件  

MyEnTunnel http://twiapp.alwaysdata.net/myt.rar

2010.3.22优化版，使用Tunnelier的plink.exe，接入更快  

SocksCap http://www.softsea.com/review/SocksCap.html  

  

2.获得SSH帐号  

  

参阅：  

https://1984bbs.com/viewthread.php?tid=31667  

https://1984bbs.com/viewthread.php?tid=33003  

  

3.运行MyEnTunnel  

设置方法：  

  

![](http://imgur.com/jBZEu.png)  

  

点击Save保存，点击Connect连接  

  

![](http://btchina.bos.ru/ssh/15.jpg)  

确认指纹警告  

  

4.运行SocksCap  

SocksCap是绿色软件解压后运行sc32.exe  

  

等待十秒钟，点接受  

![](http://btchina.bos.ru/scv/01.jpg)  

  

点是  

![](http://btchina.bos.ru/scv/02.jpg)  

  

5.设置SocksCap  

  

![](http://btchina.bos.ru/scv/03.jpg)  

  

6.新建代理  

  

![](http://btchina.bos.ru/scv/04.jpg)  

  

![](http://btchina.bos.ru/scv/05.jpg)  

  

IE所在目录(windows XP)  

![](http://btchina.bos.ru/scv/06.jpg)  

  

选中文件  

![](http://btchina.bos.ru/scv/07.jpg)  

  

![](http://btchina.bos.ru/scv/08.jpg)  

  

  

7.测试  

  

双击控制台IE图标  

  

![](http://btchina.bos.ru/scv/09.jpg)  

  

![](http://btchina.bos.ru/scv/10.jpg)  

  

8.Fuck FGW  

  

![](http://btchina.bos.ru/scv/12.jpg)  

  

  

附：  

Firefox+MyEnTunnel+AutoProxy翻墙教程：https://1984bbs.com/viewthread.php?tid=38397  

  

  

========================  

1984BBS原创教程，欢迎转载，转载请注明出处。  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



samzhang





2楼 大 中 小 发表于 2010-3-12 18:13  只看该作者



为什么在程序里打开IE会非法?  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





3楼 大 中 小 发表于 2010-3-12 18:23  只看该作者



引用:



> 原帖由 samzhang 于 2010-3-12 18:13 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  为什么在程序里打开IE会非法?



能详尽描述下，或者提供报错截图吗？  

  

  





  

核子力量



Twitter.com/hzpower





4楼 大 中 小 发表于 2010-3-12 18:29  只看该作者



直接把ie的图标拖到SocksCap的框里就行了  

  

  







  

单手扶墙



活了几十年年，没能为党为人民做点什么，每思及此，心神不宁。





5楼 大 中 小 发表于 2010-3-12 18:54  只看该作者



书签  

  

  





  

geeker





6楼 大 中 小 发表于 2010-3-13 11:44  只看该作者



灰常牛b  

  

  





  

阳光不锈



医生的职责不是救人，而是少杀人…以为自己是风，结果遍体鳞伤才发现，原来自己是草！





7楼 大 中 小 发表于 2010-3-13 15:58  只看该作者



这个我自己很早就弄过...  

感觉不怎样...  

经常会出现SSH的断链...  

不是很稳定的...  

还是用火狐比较干脆...  

虽然整体来讲,速度不是很快  

但是稳定...  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





8楼 大 中 小 发表于 2010-3-13 16:32  只看该作者



回复 7楼 阳光不锈 的话题



呃？稳定和速度的区别，应该是和SSH服务器有关系跟用什么软件关系不大吧？  

SSH有个加密传输过程占用CPU，所以要比vpn慢，同一个vps，SSH最高下载速度70-80KB/s，VPN可达100-140KB/S  

  

  





  

庸人自擾





9楼 大 中 小 发表于 2010-3-13 16:40  只看该作者



不支持Windows7  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





10楼 大 中 小 发表于 2010-3-13 17:24  只看该作者



回复 9楼 庸人自擾 的话题



http://www.softsea.com/review/SocksCap.html  

  

  





  

核子力量



Twitter.com/hzpower





11楼 大 中 小 发表于 2010-3-13 19:29  只看该作者



回复 9楼 庸人自擾 的话题



支持win7的，我就是在win7下用的  

  

  







  

神仙一溜烟



杵君





12楼 大 中 小 发表于 2010-3-14 15:13  只看该作者



用fox感觉不错，最喜欢SSH  

  

  





  

guy84





13楼 大 中 小 发表于 2010-3-14 15:36  只看该作者



这个还是相对比较麻烦，而且速度没有保障。。。不过可能比较稳定。。。  

  

  





  

shanyun





14楼 大 中 小 发表于 2010-3-14 17:46  只看该作者



引用:



> 原帖由 阳光不锈 于 2010-3-13 15:58 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  这个我自己很早就弄过...  

>  感觉不怎样...  

>  经常会出现SSH的断链...  

>  不是很稳定的...  

>  还是用火狐比较干脆...  

>  虽然整体来讲,速度不是很快  

>  但是稳定...



+1984 这样的配置我已经够用了。很爽，很和谐，天天FUCK GFW  

  

  





  

神仙一溜烟



杵君





15楼 大 中 小 发表于 2010-3-14 18:41  只看该作者



SSH已经比洋葱好得太多了！我觉得比VPN都好。  

  

绿色轻便无广告。这简直就是linux下的精品软件才能达到的水平。  

  

  





  

luckypoem





16楼 大 中 小 发表于 2010-5-20 11:28  只看该作者



怎么我双击sockscap里的 ie图标，然后访问ip138.com,显示的是国内ip呢？  

  

  





  

houman





17楼 大 中 小 发表于 2010-5-20 13:34  只看该作者



这东西不支持windows7  

  

  







  

柴子





18楼 大 中 小 发表于 2010-5-21 18:45  只看该作者



因为IE和opera都是不支持sock5代理的  

所以我一般都是用polipo或者3p :)  

直接把sock5转成http  

另：强推3proxy  

  

http://www.3proxy.ru/  

  

  





  

太变



偏听不信





19楼 大 中 小 发表于 2010-6-19 17:00  只看该作者



Fuck FGW  

  

搞定，谢谢！  

还是张生记比较简单。  

  

  





  

太变



偏听不信





20楼 大 中 小 发表于 2010-6-19 17:01  只看该作者



引用:



> 原帖由 houman 于 2010-5-20 13:34 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  这东西不支持windows7



我的系统就是ie7的，没问题呀！  

  

  





  

man-eleven



☭校叛徒、基本上冲锋在后、共产主义的坚定不信任者;运动控(喜欢巨大无比万人欢呼沸腾的场面比如足球赛)、热爱自由、容易怀旧伤感、会办事不会说话，俺们村最有文化的人，没有之一





21楼 大 中 小 发表于 2010-6-19 17:05  只看该作者



引用:



> 原帖由 太变 于 2010-6-19 17:01 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  

>  

>  我的系统就是ie7的，没问题呀！



//笑话一枚  

  

  





  

ottovon



@ottovonconstant





22楼 大 中 小 发表于 2010-6-22 08:26  只看该作者



完全按要求操作，firefox可以，ie和chrome则不能，如何破？  

  

  







  

zhenniua





23楼 大 中 小 发表于 2010-6-22 08:36  只看该作者



那不错的教程  

  

  





  

路边社射边路



路边社社边路边社边路边路边社边路边路边社边路边路边社边路边路边社边路边路边社边路边路边社边路边路边社边路边路边社边路





24楼 大 中 小 发表于 2010-9-7 10:35  只看该作者



点击Save保存，点击Connect连接  

  

以后的图都挂了  

  

  





  

zzug





25楼 大 中 小 发表于 2010-9-7 10:45  只看该作者



不如用FreeCap功能更强大而且开源（也有中文版），教程 http://igfw.tk/archives/802/  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





26楼 大 中 小 发表于 2010-9-7 10:47  只看该作者



引用:



> 原帖由 路边社射边路 于 2010-9-7 10:35 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  点击Save保存，点击Connect连接  

>  

>  以后的图都挂了



原图床已挂，硬盘无教程备份。  

改日重写教程。抱歉。  

  

  





  

xifanliang



有事请Reply @xifanliang





27楼 大 中 小 发表于 2010-9-7 11:12  只看该作者



http://hi.baidu.com/democratleo/ ... 3f9763dcc47460.html  

不用重写，这里有。  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





28楼 大 中 小 发表于 2010-9-7 11:14  只看该作者



回复 27楼 xifanliang 的话题



转贴为何不留出处？  

  

  





  

xifanliang



有事请Reply @xifanliang





29楼 大 中 小 发表于 2010-9-7 11:29  只看该作者



额，写1984bbs?  

  

  





  

xifanliang



有事请Reply @xifanliang





30楼 大 中 小 发表于 2010-9-7 11:30  只看该作者



via 1984bbs by 库存袈裟  

这样可以伐？  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





31楼 大 中 小 发表于 2010-9-7 11:33  只看该作者



回复 30楼 xifanliang 的话题



https://1984bbs.com/viewthread.php?tid=40080  

  

  





  





















    







    













