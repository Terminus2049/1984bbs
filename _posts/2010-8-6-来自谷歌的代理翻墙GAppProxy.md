---
layout: default

date: 2010-8-6

title: 来自谷歌的代理翻墙GAppProxy

categories: 国家局域网研究所

---





# 来自谷歌的代理翻墙GAppProxy



Zipurmouth





1楼 大 中 小 发表于 2010-8-6 14:51  只看该作者



来自谷歌的代理翻墙GAppProxy



一、GAppProxy 是什么？  

GAppProxy 是基于  Google app engine，为教育网用户提供一个免费的国际代理。由于借助了 Google

强大的服务器，所有也适用于公网的代理。  

  

二、Google app engine 是什么？  

Google app engine 是 Google 提供的一个在线应用程序平台，支持 Python。简单的说是在 Google app engine

上面直接运行用 Python 写的程序，由 Google app engine 提供网络空间和带宽。  

  

三、用 GAppProxy 能干什么？  

如果你在教育网，你可以把 GAppProxy 当作一个国际代理服务器，类似 搜狗浏览器的教育网加速。  

  

如果你在公网，正常情况下用不到 GAppProxy，首先你要有GAE的账号 也就是谷歌工程师了  

![](http://www.imgplace.com/viewimg153/428/41t66ygap8.jpg)  

![](http://www.imgplace.com/viewimg153/2716/27t66ygap9.jpg)  

![](http://www.imgplace.com/viewimg153/5351/30t66ygap10.jpg)  

  

  

填写 Application Identifier (输入你想要的应用程序地址，相应会得到一个 yourname.appspot.com

的域名，记住这个。) 和 Application Title (标题，随意啦)以及勾选同意服务条款，点 Save 即完成创建。  

  

![](http://www.imgplace.com/viewimg153/1989/19t66ygap12.jpg)  

  

下载  GappProxy 和  fetchServer  

  

把fetchserver解压到F盘(随你喜欢）  

  

把GAPPPROXY也放在里面  

  

然后打开写字板，电脑自带的，用写字板打开fetchserver文件下的app.yaml  

  

注意 一定要用写字板打开 用记事本是乱码！  

  

接下来是第二部分  

  

把your_application_nameApplication Identifier，yourname.appspot.com 中的 yourname。

比如我申请的就是hackissb  

![](http://www.imgplace.com/viewimg153/911/26t66ygap22.jpg)  

  

  

接下来呢 网上的大部分都是下载GPE 和PY 上传 这样太麻烦了 我们要用  

  

到的是谷歌自带的上传工具  SDUpload 点击就可以直接下载了。  

  

然后我们把它解压到F盘里面（取决于你的GAppProxy放在那里）  

  

接下来就是要用DOS命令上传了。  

  

我们打开cmd 然后输入F：  

  

然后我们输入 SDUpload update fetchserver  

  

就会要我们输入账号和密码 你输入完账号后输入密码会没有反应 其实是输入进去了！  

![](http://www.imgplace.com/viewimg153/3153/47t66ygap32.jpg)  

![](http://www.imgplace.com/viewimg153/4194/52t66ygap52.jpg)  

  

  

  

  

测试 fetchserver：打开浏览器，进入  

Copy code  

http://yourname.appspot.com/fetch.py  

如果得到下面的页面，证明安装成功。  

![](http://www.imgplace.com/viewimg153/8082/66t66ygap62.jpg)  

  

  

接下来就是最后一部分 我们打开放在fetchServer的GAppProxy的gui.exe  

  

勾上第二个 然后在后面输入  

Copy code  

http://yourname.appspot.com/fetch.py  

![](http://www.imgplace.com/viewimg571/2088/15t66ygap62.jpg)  

  

  

  

最后我们点击status 然后 打开IE设置代理链接为127.0.0.1 8000  

![](http://www.imgplace.com/viewimg571/8606/23t66ygap71.jpg)  

  

  

我们测试一下IP  

  

  

  

最后 我们就可以开始代理了 ！ 测试一下 我们打开youtube  

  

![](http://www.imgplace.com/viewimg571/5418/91t66ygap112.jpg)  

  

成功了！！  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



Zipurmouth





2楼 大 中 小 发表于 2010-8-6 14:52  只看该作者



shit 图挂了。。  

  

  





  

和谐牌河蟹



和谐社会吃河蟹 @HOY_05





3楼 大 中 小 发表于 2010-8-6 15:34  只看该作者



看不到图。  

  

  





  

fantamine





4楼 大 中 小 发表于 2010-8-6 15:45  只看该作者



图挂了  

  

  





  

tzhtmk





5楼 大 中 小 发表于 2010-8-6 16:17  只看该作者



看不见图  

  

  





  

Zipurmouth





6楼 大 中 小 发表于 2010-8-6 17:01  只看该作者



第一次发贴，用的那个imgplace 不知怎么没传上去，对不住大家了。~  

  

  





  

路边社特约记者



心中有佛看谁都像佛,心中有狗屎看谁都像狗屎,可是后来我发现我看谁都像BL...





7楼 大 中 小 发表于 2010-8-7 10:30  只看该作者



有点老了....  以前我也发过一次     我的bearproxy.appspot.com  

  

  







  

luugoo



拖延心理学：向与生俱来的行为顽症宣战】https://1984bbs.com/viewthread.php?tid=60185





8楼 大 中 小 发表于 2010-8-7 17:25  只看该作者



引用:



> 原帖由 路边社特约记者 于 2010-8-7 10:30 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  有点老了....  以前我也发过一次     我的bearproxy.appspot.com



介个代理很和谐很有爱...  

  

  





  





















    







    













