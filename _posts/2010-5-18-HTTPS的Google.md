---
layout: default

date: 2010-5-18

title: HTTPS的Google

categories: 国家局域网研究所

---





# HTTPS的Google Docs被墙，这到底是GFW的什么技术？（呼叫技术帝）



C.C.





1楼 大 中 小 发表于 2010-5-18 15:33  只看该作者



HTTPS的Google Docs被墙，这到底是GFW的什么技术？（呼叫技术帝）



墙内https的google docs是访问不到的，http可以，但是有关键词审查了  

  

想问下这是什么技术  

  

除了DNS劫持，IP过滤，关键词过滤，GFW还可以废掉指定的SSL证书了？  

  

很好奇具体怎么做到的，求科普  

  

今后推出的google https搜索很可能遭到类似的毒手  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



szdos





2楼 大 中 小 发表于 2010-5-18 15:40  只看该作者



只是根据证书特征RST  

  

  





  

偶佯疯



我是个读书人





3楼 大 中 小 发表于 2010-5-18 16:20  只看该作者



https的docs有时候可以打开有时候打不开，不知道是什么原因  

  

  







  

GFW





4楼 大 中 小 发表于 2010-5-18 17:22  只看该作者



IP+Port  

  

  





  

tisyang





5楼 大 中 小 发表于 2010-5-18 20:28  只看该作者



可能是直接封的IP  

  

  





  

houman





6楼 大 中 小 发表于 2010-5-18 23:06  只看该作者



也许是多个关键字，关键就是https和docs之类的，然后http是正常访问的，被关键字过滤是通过gfw的正常情况……  

  

  







  

qsIHSIN



具杯则看倒





7楼 大 中 小 发表于 2010-5-20 15:45  只看该作者



截图看一下？  

  

  





  

Danniez



A Hacker Like A Joker





8楼 大 中 小 发表于 2010-5-20 16:03  只看该作者



ip+端口  

  

  





  

OpenBL





9楼 大 中 小 发表于 2010-5-21 11:01  只看该作者



封ip的443端口  

  

  





  

electroun



於民國67年不幸出生在大陸淪陷區的中華民國國民;光復之後要把☭字烙在所有五毛腦門上.以上





10楼 大 中 小 发表于 2010-5-21 11:40  只看该作者



引用:



> 原帖由 OpenBL 于 2010-5-21 11:01 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  封ip的443端口



局域網內重新設定端口映射可以突破嗎?  

  

  





  





















    







    













