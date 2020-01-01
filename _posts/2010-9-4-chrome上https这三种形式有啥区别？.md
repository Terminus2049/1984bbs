---
layout: default

date: 2010-9-4

title: chrome上https这三种形式有啥区别？

categories: 国家局域网研究所

---





# chrome上https这三种形式有啥区别？



didiaowang





1楼 大 中 小 发表于 2010-9-4 22:29  只看该作者



chrome上https这三种形式有啥区别？



![](http://i54.tinypic.com/2116lnr.jpg)  

![](http://i54.tinypic.com/5wgft1.jpg)  

![](http://i54.tinypic.com/33nhk4o.jpg)  

经常显示这三种，代表啥意思？谁给科普下，thanks~  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



linyan431



自建twitter API ｜ https://www.kuailewang.info/twitter





2楼 大 中 小 发表于 2010-9-4 22:33  只看该作者



第一个没看到过 可能是加密无效吧  

  

第二个是数据加密通讯 但是安全证书无效 可能是因为证书过期 或者是域名不符合  

  

第三个是正常的https通讯状态 数据加密 证书也和域名吻合  

  

  





  

man-eleven



☭校叛徒、基本上冲锋在后、共产主义的坚定不信任者;运动控(喜欢巨大无比万人欢呼沸腾的场面比如足球赛)、热爱自由、容易怀旧伤感、会办事不会说话，俺们村最有文化的人，没有之一





3楼 大 中 小 发表于 2010-9-17 23:17  只看该作者



这三种情况今天集体出现了，呼叫袈裟吧  

  

  





  

didiaowang





4楼 大 中 小 发表于 2010-9-17 23:40  只看该作者



![](http://i56.tinypic.com/2zr49ia.jpg)  

红叉  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





5楼 大 中 小 发表于 2010-9-17 23:41  只看该作者



被NS劫持数次，有人在爆小组的菊  

  

  





  

didiaowang





6楼 大 中 小 发表于 2010-9-17 23:42  只看该作者



![](http://i54.tinypic.com/2w5iyl5.jpg)  

绿锁  

  

  





  

didiaowang





7楼 大 中 小 发表于 2010-9-17 23:43  只看该作者



那个骷髅头我暂时没找到网页，你点一下锁那个位置就会出来这个提示框。  

  

  





  

lehui99





8楼 大 中 小 发表于 2010-9-17 23:45  只看该作者



1\. 红叉：加密页面中包含非加密元素，但不足以影响加密页面中的内容（比如非加密元素为图片）  

2\. 骷髅：加密页面中包含非加密元素，可能会影响加密页面中的内容（比如非加密元素为CSS或JavaScript）  

3\. 删除线：SSL加密证书无效（可能为页面中的SSL加密证书无效，也有可能是页面中元素的SSL加密证书无效）  

4\. 绿色锁：SSL证书正常，页面中没有包含非加密元素  

有可能2种情况同时出现，比如删除线+骷髅。  

  

[ 本帖最后由 lehui99 于 2010-9-17 23:46 编辑 ]  

  

  







  

free1989



@photobluer





9楼 大 中 小 发表于 2010-9-17 23:50  只看该作者



Google员工的答复，供参考



http://www.google.com/support/fo ... 362d42&hl=zh-CN  

  

  





  

didiaowang





10楼 大 中 小 发表于 2010-9-18 00:09  只看该作者



![](http://i52.tinypic.com/2ef0sax.jpg)  

骷髅头+斜杠  

  

  





  





















    







    













