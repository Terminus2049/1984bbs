---
layout: default

date: 2010-7-15

title: AutoProxy使用求助

categories: 国家局域网研究所

---





# AutoProxy使用求助



……





1楼 大 中 小 发表于 2010-7-15 15:22  只看该作者



AutoProxy使用求助



在小组福利中得到SSH一个  

firefox SSH AutoProxy  

使用起来相当顺畅  

不过  

问题出现了  

维基百科并没有自动代理使用SSH连接  

而是走常规路线  

图片没有 速度很慢  

使用全局模式后 才采用SSH路线连接  

于是修改AutoProxy 规则  

增加规则：将http://zh.wikipedia.org 直接写入规则 然后应用 确定  

无任何作用…  

求助各位 如何将维基作为需代理网站 列入AutoProxyoxy 规则  

![](http://i27.tinypic.com/2qsbera.jpg)  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



库存袈裟



@bruceku 想象力比知识更重要。





2楼 大 中 小 发表于 2010-7-15 15:27  只看该作者



添加：



复制内容到剪贴板



代码:



`wikipedia.org  

wikimedia.org  

`



到规则中  

  

  





  

……





3楼 大 中 小 发表于 2010-7-15 15:38  只看该作者



回复 2楼 库存袈裟 的话题



好了好了…  

LS…谢啦……  

  

[ 本帖最后由 …… 于 2010-7-15 15:48 编辑 ]  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





4楼 大 中 小 发表于 2010-7-15 15:48  只看该作者



还有 wikimedia.org  

  

  





  

……





5楼 大 中 小 发表于 2010-7-15 15:49  只看该作者



恩恩恩…搞定了%……  

  

  





  

核子力量



Twitter.com/hzpower





6楼 大 中 小 发表于 2010-7-15 15:54  只看该作者



你的id可真行，就几个点  

  

  







  

shawnyeung





7楼 大 中 小 发表于 2010-7-20 18:15  只看该作者



引用:



> 原帖由 …… 于 2010-7-15 15:22 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  在小组福利中得到SSH一个  

>  firefox SSH AutoProxy  

>  使用起来相当顺畅  

>  不过  

>  问题出现了  

>  维基百科并没有自动代理使用SSH连接  

>  而是走常规路线  

>  图片没有 速度很慢  

>  使用全局模式后 才采用SSH路线连接  

>  于是修改Aut ...



后面应该加个通配符 "/*"  

  

  





  





















    







    













