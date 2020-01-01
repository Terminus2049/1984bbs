---
layout: default

date: 2010-9-3

title: 求帮助，求指点~GAPPPROXY

categories: 国家局域网研究所

---





# 求帮助，求指点~GAPPPROXY



thanksoar





1楼 大 中 小 发表于 2010-9-3 20:00  只看该作者



求帮助，求指点~GAPPPROXY



GAPPPROXY用了有一年多了，因为在学校里就这个好使~但是最近不知为何不管用了（无论是在校园网还是其他网）。测试自己建的fetchserver，http://onlinangel.appspot.com/fetch.py

结果是该页无法显示，但是我开自由门翻墙后，再次测试，便能成功打开，显示其正在运行。。。  

  

求解释。求解决办法。。谢谢  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



Aragorn



三俗份子





2楼 大 中 小 发表于 2010-9-3 20:12  只看该作者



换个dns试试看  

  

  





  

thanksoar





3楼 大 中 小 发表于 2010-9-3 20:15  只看该作者



回复 2楼 Aragorn 的话题



学校里可以使用的DNS就一个啊。。家里的话DNS未填。。而且DNS一直未变，突然就不能使用了  

  

  





  

zzug





4楼 大 中 小 发表于 2010-9-3 20:26  只看该作者



1、设置代理为 www.google.com:80 试试 （在proxy.conf中加一行 local_proxy = www.google.com:80）  

2、试试在host文件里加一行 72.14.203.141  onlinangel.appspot.com  

  

[ 本帖最后由 zzug 于 2010-9-3 20:38 编辑 ]  

  

  





  

thanksoar





5楼 大 中 小 发表于 2010-9-3 20:47  只看该作者



回复 4楼 zzug 的话题



按您所给的方法：  

1在FIRE FOX下，键入任何网站都会转入GOOGLE。然后突然失效，关闭FF任然无效。  

  

2过一会再次打开FF，重复1中的情况  

  

  





  

zzug





6楼 大 中 小 发表于 2010-9-3 21:04  只看该作者



回复 5楼 thanksoar 的话题



那就不知道了，我这测试你那个帐号正常（1和2分开试试，不要一起用）  

  

  





  

thanksoar





7楼 大 中 小 发表于 2010-9-3 21:22  只看该作者



回复 6楼 zzug 的话题



握手，感谢！按您所给的2中的方法修改后GAPPPROXY可以正常使用了~敢问问题究竟出在哪？  

  

  





  

zzug





8楼 大 中 小 发表于 2010-9-3 21:23  只看该作者



回复 7楼 thanksoar 的话题



DNS  

  

  





  

thanksoar





9楼 大 中 小 发表于 2010-9-3 21:26  只看该作者



谢谢你耐心的帮助~  

  

  





  

zzug





10楼 大 中 小 发表于 2010-9-3 22:02  只看该作者



回复 9楼 thanksoar 的话题



不客气  

  

  





  





















    







    













