---
layout: default

date: 2010-7-28

title: Google的HTTPS搜索服务遭DNS污染

categories: 国家局域网研究所

---





# Google的HTTPS搜索服务遭DNS污染



yimings



像风一样自由





1楼 大 中 小 发表于 2010-7-28 14:19  只看该作者



Google的HTTPS搜索服务遭DNS污染



Google的HTTPS搜索服务遭DNS污染  

  

作者：龙威廉 (williamlong) 阅读原文  

  

<共1张照片>  

  

阅读更多  

Google上个月把Https搜索转到另外一个域名encrypted.google.com下面，所有的https搜索都会自动重定向，Google称这个操作是为了方便美国学校和企业过滤新的域名，但我当时我就知道，这个域名危险了。  

整整一个月后的今天，终于还是等到了这一天，虽然对于没做任何设置的中国用户，Google默认会把https搜索重定向到谷歌香港的http搜索，尽量避免中国用户使用HTTPS搜索，但这一天终于还是来了，Google的HTTPS加密搜索服务器域名

encrypted.google.com 被DNS污染而无法访问。  

  

关于判断DNS污染的文章可以参看此文，我们在命令行下通过这样一条命令 nslookup encrypted.google.com

144.223.234.234，即可判断该域名是否被污染，由于144.223.234.234不存在，理应没有任何返回。但我们却得到了一个错误的IP：93.46.8.89。可见

encrypted.google.com 这个域名已经被DNS污染了。  

  

解决的方法有三个：  

  

1、使用各种SSH加密代理，在加密代理里进行远程DNS解析，或者使用VPN上网。  

  

2、修改hosts文件，Windows系统中Hosts文件的优先级高于DNS服务器，操作系统在访问某个域名时，会先检测HOSTS文件，然后再查询DNS服务器。可以在hosts添加受到污染的DNS地址来解决DNS污染和DNS劫持，目前可用的encrypted.google.com的IP有66.249.89.104和209.85.225.104。  

  

3、通过一些软件编程处理，可以直接忽略返回结果是虚假IP地址的数据包，直接解决DNS污染的问题。这类软件可参见这里和这里。  

  

最后，我谴责这种通过DNS污染干扰用户上网的流氓手段。  

  

  

评论《Google的HTTPS搜索服务遭DNS污染》的内容...  

  

  







  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



yimings



像风一样自由





2楼 大 中 小 发表于 2010-7-28 14:21  只看该作者



这一天终于来到了！马勒戈壁的！  

  

  







  

imus



升斗小民





3楼 大 中 小 发表于 2010-7-29 09:05  只看该作者



现在月光自称龙威廉了？  

  

  







  

kronos1980



ziwu





4楼 大 中 小 发表于 2010-7-29 16:38  只看该作者



修改hosts合肥失效  

  

  







  

核子力量



Twitter.com/hzpower





5楼 大 中 小 发表于 2010-7-29 16:46  只看该作者



autoproxy新列表里已经加入encrypted.google.com了  

  

  







  

chiceren





6楼 大 中 小 发表于 2010-7-30 21:30  只看该作者



OK了，，天呀，终于搞定了~  

  

  







  

s7lx





7楼 大 中 小 发表于 2010-8-7 14:28  只看该作者



https://www.google.com/webhp?hl=zh-cn  

  

  





  

清水洗尘





8楼 大 中 小 发表于 2010-8-7 14:42  只看该作者



很正常，现在校园网内，很多G服务都不能享用。。。  

  

  





  

prince20





9楼 大 中 小 发表于 2010-8-7 22:56  只看该作者



校园网就是一个杯具....  

  

  





  

flooower





10楼 大 中 小 发表于 2010-8-7 23:17  只看该作者



这个强大！！



引用:



> 原帖由 s7lx 于 2010-8-7 14:28 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  https://www.google.com/webhp?hl=zh-cn  

  

  





  





















    







    













