---
layout: default

date: 2010-3-19

title: 使用Tunnelier为SSH加速

categories: 国家局域网研究所

---





# 使用Tunnelier为SSH加速



shanyun





1楼 大 中 小 发表于 2010-3-19 17:26  只看该作者



使用Tunnelier为SSH加速



首先声明，我是转载的文章，感谢原文作者的奉献，Lenmore Blog » 建议用Tunnelier代替MyEnTunnel翻墙  

  

MyEnTunnel实际上是plink的

gui前端而已，可以避免记忆复杂的命令行，还可以安全的保存密码。很多人用MyEnTunnel做为windows下的ssh客户端翻墙。  

  

但是有个问题，通过MyEnTunnel或者plink下载或者看视频速度很慢，最高不超过35KB/s。  

  

我尝试修改sshd的配置，给openssh-server打补丁(参考一,参考二)，优化TCP参数，都无济于事。然后在本地的Linux虚拟机上运行ssh -D

…命令，发现速度飞快，没有任何限制了。原来问题在客户端，可能是plink or putty做了什么限制吧。  

  

推荐Tunnelier，另一款ssh客户端，对个人用户免费。下载地址：http://www.bitvise.com/tunnelier-download  

  

软件设置比较简单：  

Login选项卡，输入ssh服务器的登录信息。  

Options选项卡，On Login部分把几个勾都去掉，只是翻墙的话用不上。  

Services选项卡，SOCKS/HTTP Proxy Forwarding部分 Enabled，修改本地监听端口。  

然后Save Profile As另存配置  

  

Tips:  

可以从命令行运行 Tunnelier：tunnelier -profile=profilename.tlp -loginOnStartup  

可以把上面的命令做成快捷方式放到启动里面  

  

\--------------------------------------------------------------------------------------------------------------------------------  

  

经过试用，速度和以前使用MyEnTunnel来说，绝对是质的飞跃，看YouTube一点都不卡，看720的YouTube缓冲也非常快速，几乎不卡。  

  

最后想问下使用SSH的同学，你们的服务器ping指一般在多少，我的在196左右徘徊，这个速度快吗?6元/月的，反正对我来说足够用了，更多消息请参看http://ratoo.tk/bitvise-

tunnelier-tutorial  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



核子力量



Twitter.com/hzpower





2楼 大 中 小 发表于 2010-3-19 17:30  只看该作者



前两天twitter上好多人在说 ，小众软件也推荐了  

  

  







  

抑扬



小组男客服（Twitter @yiang_）





3楼 大 中 小 发表于 2010-3-19 19:04  只看该作者



在库库的指导下设置成功，内牛满面  

  

  





  

freewushi



东厂、真理部、GFW、宫刑部爱好者，经常在不和谐的地方出没，围观群众一个





4楼 大 中 小 发表于 2010-3-19 19:51  只看该作者



本地机ping 代理服务器是170ms，代理服务器ping google.com才2.7ms..感觉还不错  

  

  





  

ciscoxp





5楼 大 中 小 发表于 2010-3-19 19:58  只看该作者



试了一下，果然快多了。谢谢楼主！  

  

  





  

isonomy





6楼 大 中 小 发表于 2010-3-19 21:28  只看该作者



确实不错  

  

  





  

萧易寒





7楼 大 中 小 发表于 2010-3-19 22:06  只看该作者



楼主的ssh端口号是4位以上的吧？  

貌似MyEntunnel对高端口号的SSH有bug  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





8楼 大 中 小 发表于 2010-3-19 22:15  只看该作者



回复 1楼 shanyun 的话题



196ms很快了 我的PR机房ping 210-240ms也是西海岸  

  

  





  

alexander982



肆零贰壹号组员//道貌岸然的知心大哥//伪爱情专家//傻*英雄主义者//一个烤鸭的传说





9楼 大 中 小 发表于 2010-3-19 22:46  只看该作者



速度确实快了些



怎样使用多个配置？  

  

盼高手汉化  

  

[ 本帖最后由 alexander982 于 2010-3-19 22:48 编辑 ]  

  

  





  

shanyun





10楼 大 中 小 发表于 2010-3-19 22:49  只看该作者



引用:



> 原帖由 萧易寒 于 2010-3-19 22:06 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  楼主的ssh端口号是4位以上的吧？  

>  貌似MyEntunnel对高端口号的SSH有bug



我的服务器开放了4个端口，我用的是22端口。淘宝买的，才22个人在使用，6元一月，很不错。  

  

  





  

shanyun





11楼 大 中 小 发表于 2010-3-19 22:50  只看该作者



引用:



> 原帖由 alexander982 于 2010-3-19 22:46 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  怎样使用多个配置？  

>  

>  盼高手汉化



傻瓜软件，不用汉化了吧，设置很简单的，就是功能比MyT多，所以就觉得有点难度，其实光使用代理的话，很多功能都用不上的。  

  

  





  

alexander982



肆零贰壹号组员//道貌岸然的知心大哥//伪爱情专家//傻*英雄主义者//一个烤鸭的传说





12楼 大 中 小 发表于 2010-3-19 23:19  只看该作者



上次裟组提供的8条demo，刚才验证了一下只有四条能有了。  

  

服务器地址：207.182.151.19  

用户名：demobye  

密码：password  

端口： 27015  

  

服务器地址：206.212.253.54  

用户名：demo  

密码：input-button  

端口： 5205  

  

服务器地址：204.124.181.194  

用户名：cpdemo  

密码：demopass  

端口： 22  

  

服务器地址：67.228.94.72  

用户名：demoweb  

密码：zaq1xsw2  

端口： 7277  

  

  





  

zzug





13楼 大 中 小 发表于 2010-3-20 08:37  只看该作者



给大家说个好消息，plink最新开发版解决了速度慢的这个问题，使用最新开发板的myentunnel速度和tunnelier一样快了，大家可以继续使用myentunnel而不必忍受tnnelier了，详情请看http://igfw.tk/archives/166  

  

  





  

核子力量



Twitter.com/hzpower





14楼 大 中 小 发表于 2010-3-20 22:40  只看该作者



Bitvise Tunnelier 官方推荐便携版(绿色版)下载地址：http://tp.vbap.com.au/download （需翻墙）  

在小众软件找到的  

  

  







  

8th.gua





15楼 大 中 小 发表于 2010-3-21 01:54  只看该作者



测试完毕：  

在此处下载plink dev版：http://tartarus.org/~simon/putty-snapshots/x86/plink.exe  

下载完后，将此文件替换MyEnTunnel安装文件夹里的plink.exe  

然后照常运行MyEnTunnel  

  

youtube视频速度明显提高  

  

[ 本帖最后由 8th.gua 于 2010-3-21 01:56 编辑 ]  

  

  





  

萧易寒





16楼 大 中 小 发表于 2010-3-21 16:09  只看该作者



回复 15楼 8th.gua 的话题



putty和plink停止开发好多年了，最后的版本就是0.60beta  

哪来的dev版？  

  

  





  

lzk800





17楼 大 中 小 发表于 2010-3-21 16:11  只看该作者



嗯 plink换成dev版就ok了  

  

  





  

zzug





18楼 大 中 小 发表于 2010-3-21 18:57  只看该作者



引用:



> 原帖由 萧易寒 于 2010-3-21 16:09 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  putty和plink停止开发好多年了，最后的版本就是0.60beta  

>  哪来的dev版？



你仔细看看 http://putty.very.rulez.org/download.html 这个页面然后下载比较下就明白了！  

  

  





  

萧易寒





19楼 大 中 小 发表于 2010-3-21 20:33  只看该作者



回复 18楼 zzug 的话题



看到了，  

试过了，不好意思原来是我搞错了  

测试了一下，plink 0.6 beta在高端口下下载会断线，低端口不会  

plink 0.6 dev很正常，不会断线，网速感觉也有提升  

谢谢  

  

  





  





















    







    













