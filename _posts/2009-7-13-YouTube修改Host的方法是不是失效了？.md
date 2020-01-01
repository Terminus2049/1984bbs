---
layout: default

date: 2009-7-13

title: YouTube修改Host的方法是不是失效了？

categories: 国家局域网研究所

---





# YouTube修改Host的方法是不是失效了？



无机客





1楼 大 中 小 发表于 2009-7-13 18:20  只看该作者



YouTube修改Host的方法是不是失效了？



现在是能访问，但放不了视频。显示 An error occurred, please try again later  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



942kid





2楼 大 中 小 发表于 2009-7-13 21:47  只看该作者



貌似不好使，楼上再给细讲讲？  

  

  





  

gloried





3楼 大 中 小 发表于 2009-7-14 02:02  只看该作者



可以啊 我的还能用的说  

  

  





  

offacer





4楼 大 中 小 发表于 2009-7-14 11:31  只看该作者



googlevideo.com 被封，彻底上不了了，见这里：  

http://www.google.cn/support/for ... 48bceb&hl=zh-CN  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





5楼 大 中 小 发表于 2009-7-14 11:37  只看该作者



在开始里点击运行 然后输入：notepad C:\WINDOWS\system32\drivers\etc\hosts  

复制：



复制内容到剪贴板



代码:



`203.208.39.104 www.youtube.com  

203.208.39.104 youtube.com  

203.208.33.100 gdata.youtube.com  

203.208.39.99 upload.youtube.com  

203.208.39.99 insight.youtube.com  

203.208.39.160 help.youtube.com  

203.208.39.104 s.ytimg.com  

203.208.39.104 i1.ytimg.com  

203.208.39.104 i2.ytimg.com  

203.208.39.104 i3.ytimg.com  

203.208.39.104 i4.ytimg.com`



保存到Hosts文件最后一行，保存，重启浏览器。  

  

  





  

offacer





6楼 大 中 小 发表于 2009-7-14 11:48  只看该作者



引用:



> 原帖由 库存袈裟 于 2009-7-14 11:37 发表 ![](http://1984bbs.com/images/common/back.gif)  

>  在开始里点击运行 然后输入：notepad C:\WINDOWS\system32\drivers\etc\hosts  

>  复制：  

>  203.208.39.104 www.youtube.com  

>  203.208.39.104 youtube.com  

>  203.208.33.100 gdata.youtube.com  

>  203.208.39.99 upload.yo ...



从7.13开始已经不灵了  

  

  





  

aston





7楼 大 中 小 发表于 2009-7-14 19:06  只看该作者



对的。昨晚半夜封的。很郁闷。而且找不到替代入口。  <\-- x 2  

  

  





  

liuropot



我们是共匪。





8楼 大 中 小 发表于 2009-7-14 19:44  只看该作者



这个方法已经不可以了。GFW用了一个过滤网页CSS的办法，就是二楼要加的那个地址，非常遗憾的是这个地址只是为youtube提供样式表，CSS是一个文本文档，GFW给过滤掉了。有一个非常笨的办法，但很麻烦，把要观看的网页保存到本地，把CSS下载到本地，然后重新指定CSS的本地地址，这样是可以，但很麻烦。  

  

  





  

hikui





9楼 大 中 小 发表于 2009-7-14 21:07  只看该作者



不只是CSS被过滤，视频服务器全部被过滤了  

  

  





  

aston





10楼 大 中 小 发表于 2009-7-15 05:16  只看该作者



不只是CSS被过滤，视频服务器全部被过滤了 X2  

  

  





  

跟丫死磕





11楼 大 中 小 发表于 2009-7-15 09:35  只看该作者



我这边没有任何问题，继续有效。  

  

  





  

无机客





12楼 大 中 小 发表于 2009-7-16 09:03  只看该作者



你是在哪里啊？  

  

  





  

大人，有胸器



围观团资深AV鉴定师





13楼 大 中 小 发表于 2009-7-16 14:35  只看该作者



有没有到美帝去起诉 思科 这个贱公司  

  

  





  

glim



传说中的熊男 @glimho





14楼 大 中 小 发表于 2009-7-26 08:09  只看该作者



唉，又要用新方法了  

  

  







  

跟丫死磕





15楼 大 中 小 发表于 2009-7-26 11:56  只看该作者



继续有效。  

  

  





  

8ger



我还是低调点比较好





16楼 大 中 小 发表于 2009-7-29 19:44  只看该作者



引用:



> 原帖由 offacer 于 2009-7-14 11:31 发表

>  googlevideo.com 被封，彻底上不了了，见这里：  

>  http://www.google.cn/support/for ... 48bceb&hl=zh-CN



根据服务条款，此网页的部分内容隐藏起来了  

  

  





  

8ger



我还是低调点比较好





17楼 大 中 小 发表于 2009-7-29 19:47  只看该作者



http://v12.lscache4.c.youtube.co ... id=8d017be06ad8228b  

  

类似这样的网址被墙了  

  

  





  

8ger



我还是低调点比较好





18楼 大 中 小 发表于 2009-7-29 19:49  只看该作者



我猜是直接墙掉了含c.youtube.com的网址  

因为前面v?.lscache?数字不确定，不能改hosts啊  

  

  





  

高渐离



组内伍毛全家死光





19楼 大 中 小 发表于 2009-8-4 03:49  只看该作者



还有什么办法直接上 YOUTUBE的吗，  

肏你妈的GFW  

  

  





  

alian





20楼 大 中 小 发表于 2009-8-6 09:20  只看该作者



现在还可以用吗?  

  

  





  

crackboy





21楼 大 中 小 发表于 2009-8-25 15:35  只看该作者



引用:



> 原帖由 高渐离 于 2009-8-4 03:49 发表 ![](http://1984bbs.com/images/common/back.gif)  

>  还有什么办法直接上 YOUTUBE的吗，  

>  肏你妈的GFW



是有的，不过不能直接看，是下载，不用代理，自己摸索一下吧。  

  

[ 本帖最后由 crackboy 于 2009-8-25 15:45 编辑 ]  

  

  









  

BlackDream





22楼 大 中 小 发表于 2009-8-25 18:35  只看该作者



应该是，用vpn把！  

  

  





  





















    







    













