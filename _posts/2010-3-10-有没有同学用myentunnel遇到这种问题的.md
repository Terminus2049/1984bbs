---
layout: default

date: 2010-3-10

title: 有没有同学用myentunnel遇到这种问题的

categories: 国家局域网研究所

---





# 有没有同学用myentunnel遇到这种问题的



kava



K





1楼 大 中 小 发表于 2010-3-10 23:53  只看该作者



有没有同学用myentunnel遇到这种问题的



换了几个ssh代理，发现右下角图标始终可以变绿，但无法正常工作。  

试了一下随便乱填一个密码，(肯定是错的密码，用putty试过无法登陆，是错密码）  

myentunnel竟然还能变绿。。。。status如下：  

[23:43:40 03/10] Launching executable  

[23:43:47 03/10] plink.exe: login as:  

[23:43:51 03/10] Connection is stable  

但是就是无法正常起到代理的作用。firefox里的设置应该没有错，  

myentunnel是在google出的第一个页面http://nemesis2.qx.net/pages/MyEnTunnel下载的Stable

Release 3.4.2.1 (Non-Unicode)  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



crime





2楼 大 中 小 发表于 2010-3-11 00:02  只看该作者



我的正常  

状态是  

  

[19:36:04 03/10] Launching executable  

[19:36:08 03/10] plink.exe: 用户名's password:  

[19:36:08 03/10] Sending password  

[19:36:15 03/10] Connection is stable  

  

我没看你的给的那个地址  

你确定里面有PLINK吧  

  

  





  

核子力量



Twitter.com/hzpower





3楼 大 中 小 发表于 2010-3-11 00:07  只看该作者



正常的的是  

[18:36:31 03/10] 加载plink核心中...  

[18:36:35 03/10] plink.exe: 用户名@服务器's password:  

[18:36:35 03/10] 发送密码中...  

[18:36:41 03/10] 连接已经稳定下来了  

  

我有时候也会出现锁是绿的但不管用的问题  

一般都是服务器出了问题，换个时间再连就好了  

  

[ 本帖最后由 核子力量 于 2010-3-11 00:08 编辑 ]  

  

  







  

kava



K





4楼 大 中 小 发表于 2010-3-11 00:08  只看该作者



确定是有plink的。  

那个地址好像是myentunnel官网。  

我又换了一个其它版本的试，结果还是一样，随便输个密码都能变绿.....  

是我的电脑出啥毛病了么？  

  

  





  

samzhang





5楼 大 中 小 发表于 2010-3-11 00:12  只看该作者



你把右下角退出照样能翻.  只要后台服务正常就行myentunnel-service.exe  

  

  





  

crime





6楼 大 中 小 发表于 2010-3-11 00:22  只看该作者



我有时候网速慢是这样的  

  

[19:36:04 03/10] Launching executable  

[19:36:15 03/10] Connection is stable  

[19:36:08 03/10] plink.exe: 用户名's password:  

[19:36:08 03/10] Sending password  

  

调了个头  

  

你端口什么的都设置正确了么？  

  

5L的 我的myentunnel一退出就木有myentunnel-service.exe这个后台服务了  

  

  





  

kava



K





7楼 大 中 小 发表于 2010-3-11 00:26  只看该作者



换了一台电脑，用完全一样的方法做了一遍，就可以用了  

这个。。。  

为什么刚才那台电脑试了N次都不行呢？？  

会是哪儿的问题呢？  

  

  





  

kava



K





8楼 大 中 小 发表于 2010-3-11 00:28  只看该作者



引用:



> 原帖由 crime 于 2010-3-11 00:22 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  我有时候网速慢是这样的  

>  

>  [19:36:04 03/10] Launching executable  

>  [19:36:15 03/10] Connection is stable  

>  [19:36:08 03/10] plink.exe: 用户名's password:  

>  [19:36:08 03/10] Sending password  

>  

>  调了个头  

>  

>  ...



基本可以肯定设置没错。。  

我在刚才电脑上试了2个多小时。。换台电脑两分钟就搞定了。...晕  

请各位达人帮我想想这软件是和别的什么有冲突么。。。  

  

  





  

萧易寒





9楼 大 中 小 发表于 2010-3-11 11:02  只看该作者



回复 1楼 kava 的话题



你的myentunnel和putty在同一个目录中  

putty的default设置会影响myentunnel  

  

解决方法：1、放在不同目录中  

2、default设置不要有内容  

  

  





  

shanyun





10楼 大 中 小 发表于 2010-3-11 12:00  只看该作者



我的正常  

  

  





  





















    







    













