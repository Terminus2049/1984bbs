---
layout: default

date: 2010-8-8

title: gappproxy用不了了

categories: 国家局域网研究所

---





# gappproxy用不了了 请问为何？？？



wr6888





1楼 大 中 小 发表于 2010-8-8 10:48  只看该作者



gappproxy用不了了 请问为何？？？



我在学校机房弄的    按照步骤一步步来   弄完后确实能上推特了   但回到宿舍用我自己的电脑后确一直上不了   总是显示405错误   请问这是为啥呢  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



cnhalien





2楼 大 中 小 发表于 2010-8-8 13:14  只看该作者



昨晚弄了几次都不行，不知道为什么  

  

  





  

gzlxd



Twitter/@gzlxd





3楼 大 中 小 发表于 2010-8-8 14:24  只看该作者



可以用的,  

  

1, 检查你自己的帐户名有没有在 fetchserver文件夹目录下的app.yaml里,如没有,用写字板编辑器打开,添加进去.  

  

2, 用sdupload上传fetchserver 到服务器, 运行-CMD -文件夹路径如:  D:  cd sdupload update

fetchserver ,把你的邮件,密码输进去稍等片刻就有一个提示了  

3,打开GAppProxy目录下的GUI文件,里面的链接复制到浏览器可以查看GP工作是否正常  

  

其实设置也不复杂,先把127.0.0.1 8000端口设置好  

  

  





  

wr6888





4楼 大 中 小 发表于 2010-8-8 17:02  只看该作者



引用:



> 原帖由 gzlxd 于 2010-8-8 14:24 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  可以用的,  

>  

>  1, 检查你自己的帐户名有没有在 fetchserver文件夹目录下的app.yaml里,如没有,用写字板编辑器打开,添加进去.  

>  

>  2, 用sdupload上传fetchserver 到服务器, 运行-CMD -文件夹路径如:  D:  cd sdupload up ...



我测试过我的fetchserver已经在运行了   这不就证明我的fetchserver已经能用了吗

但是填好127.0.0.1:8000的代理后就是上不去网   什么网页都打不开....我怀疑是不是换了电脑就不行了？  

  

  





  

gzlxd



Twitter/@gzlxd





5楼 大 中 小 发表于 2010-8-9 01:24  只看该作者



DNS是否改了？本地连接理修改DNS吧，或你用火狐试一下，我火狐，IE，chrome都能用  

  

  





  

fans



木有头衔





6楼 大 中 小 发表于 2010-8-9 11:37  只看该作者



貌似没看到说启动了本地客户端···  

  

  





  

wr6888





7楼 大 中 小 发表于 2010-8-13 10:54  只看该作者



引用:



> 原帖由 fans 于 2010-8-9 11:37 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  貌似没看到说启动了本地客户端···



启动了客户端gui.exe嘛   userfetchserver那一栏现在不管填谁的地址都上不了...原来在机房还能用的啊  

  

  





  

wr6888





8楼 大 中 小 发表于 2010-8-13 11:01  只看该作者



引用:



> 原帖由 gzlxd 于 2010-8-9 01:24 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  DNS是否改了？本地连接理修改DNS吧，或你用火狐试一下，我火狐，IE，chrome都能用



机房跟宿舍的DNS地址都是学校的啊    都一样啊    我用火狐试过了    现在的情况是   我在机房就能翻墙   但在宿舍就不行了...  

  

  





  





















    







    













