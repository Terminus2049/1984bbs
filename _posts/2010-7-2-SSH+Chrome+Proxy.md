---
layout: default

date: 2010-7-2

title: SSH+Chrome+Proxy

categories: 国家局域网研究所

---





# SSH+Chrome+Proxy Switchy!翻墙教程



free1989



@photobluer





1楼 大 中 小 发表于 2010-7-2 14:13  只看该作者



SSH+Chrome+Proxy Switchy!翻墙教程



文章部分内容图片引自：https://1984bbs.com/viewthread.php?tid=38397  

  

请安装以下软件:  

Chrome:www.google.com/chrome  

MyEnTunnel:http://twiapp.alwaysdata.net/myt.rar  

  

===MyEntunnel设置及运行===  

1.运行MyEntunnel  

并填写SSH服务器地址，用户名，密码；根据下图配置选项。  

![](http://i.imgur.com/jBZEu.png)  

  

2.点击Save保存，点击Connect连接  

![](http://i37.tinypic.com/14kwifl.png)  

  

3.等待连接成功（中间可能会出席一个对话框，点击Yes）  

![](http://imgur.com/Nic9W.png)  

  

4.等待小红锁转绿（小黄锁说明正在连接）  

![](http://i45.tinypic.com/e5jp6o.jpg)→![](http://i49.tinypic.com/4h82rt.jpg)→![](http://i46.tinypic.com/2edny9j.jpg)  

===Proxy Switchy!安装及设置===  

  

1.打开Chrome，安装Proxy Switchy!  

![](http://i45.tinypic.com/nycxas.jpg)  

  

   Proxy Switchy!安装地址：  

   https://chrome.google.com/extens ... blemipncjj?hl=zh-cn  

  

   对英文头疼的请安装Proxy Switchy!中文汉化版：  

   https://chrome.google.com/extens ... gipbdpomke?hl=zh-cn  

  

  （以下内容以Proxy Switchy!英文版示范）  

  

2.安装后Chrome工具栏右上角出现一个地球图标  

![](http://i50.tinypic.com/20mkbk.jpg)  

  

3.在地球图标上单击右键，选择“选项”：  

![](http://i47.tinypic.com/110htg7.jpg)  

  

4.打开了Proxy Switchy!的设置页  

![](http://i50.tinypic.com/mkkxfc.jpg)  

  

5.Proxy Profiles选项卡按照下图设置，Profile Name建议填写SSH，一目了然（当然可以起别的名字）  

![](http://i50.tinypic.com/121qrn8.jpg)  

点击Save,保存。  

  

6.切换至Network选项卡。把Proxy for VPN/Dial-up勾上，Connection选择宽带链接的名称（名字一定要英文，中文的话会不正常）  

![](http://i48.tinypic.com/nq7img.jpg)  

  

===至此基本设置完成，下面介绍如何访问被封锁的网站===  

  

1.Proxy Switchy!和AutoProxy类似，有3种模式。  

![](http://i48.tinypic.com/2d9ahip.jpg)  

   Direct Connection:即直接连接，就是不用代理  

   SSH:这个就是刚才创建的Profile。选择这项是整体使用代理，即使访问国内网站也去国外的服务器兜一圈。  

   Auto Switch Mode:此模式是根据Rules来选择访问的网站是否使用代理。下面着重讲解此模式。  

  

2.在Auto Switch Mode下访问一个被封的网站（这里选择foursquare做示范）.提示“此网页无法访问。”  

![](http://i45.tinypic.com/2hq6yi9.jpg)  

  

3.左键单击Proxy Switchy!的地球图标，选择New Rule  

![](http://i49.tinypic.com/1zg5l6t.jpg)  

  

4.Proxy Profile一定要选择"SSH"，Rule Name建议填写网站的名称  

![](http://i50.tinypic.com/s4q55g.jpg)  

  

5.再刷新下页面，foursquare打开了 : )  

![](http://i47.tinypic.com/2eo8d52.jpg)  

  

[ 本帖最后由 free1989 于 2010-7-2 14:59 编辑 ]  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



free1989



@photobluer





2楼 大 中 小 发表于 2010-7-2 14:14  只看该作者



Proxy Switchy!中的Switch Rules可自行添加修改规则。  

格式如图：  

![](http://i49.tinypic.com/k0lt7l.jpg)  

  

[ 本帖最后由 free1989 于 2010-7-2 14:29 编辑 ]  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





3楼 大 中 小 发表于 2010-7-2 14:26  只看该作者



已加入本版精华  

  

  





  

man-eleven



☭校叛徒、基本上冲锋在后、共产主义的坚定不信任者;运动控(喜欢巨大无比万人欢呼沸腾的场面比如足球赛)、热爱自由、容易怀旧伤感、会办事不会说话，俺们村最有文化的人，没有之一





4楼 大 中 小 发表于 2010-7-2 14:37  只看该作者



刚换Google chrome，这个就来了，简直与袈裟举案齐眉  

  

  





  

hurri



在那荒茫美丽马勒戈壁有一群草泥马，他们活泼又聪明，他们调皮又灵敏，他们由自在生活在那草泥马戈壁，他们顽强勇敢克服艰苦环境。





5楼 大 中 小 发表于 2010-7-2 19:21  只看该作者



关键是：SSH服务器地址，用户名，密码  

  

  





  

DaemonEye



不河蟹的围观团团员





6楼 大 中 小 发表于 2010-7-2 19:28  只看该作者



我记得是可以加入pac 而不用自己写规则 浪费时间造存在的轮子的吧  

  

  





  

核子力量



Twitter.com/hzpower





7楼 大 中 小 发表于 2010-7-2 19:38  只看该作者



不用自己手动添加的，太麻烦了，用autoproxy的pac就可以  

地址：http://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt  

把AutoProxy Compatible List的勾挑上，reload every先选最短的15分钟，等第一次更新之后可以选成间隔长一些的  

proxy profile选用代理的配置  

已经用一段时间了，感觉还行  

  

![](https://yopic.us/images/chrome.jpg)  

  

具体参见：  

http://autoproxy.org/zh-CN/node/73  

进入 Switch Rules 选项卡，设置 gfwlist 的 URL 为 http://autoproxy-

gfwlist.googlecode.com/svn/trunk/gfwlist.txt  。记得要勾选 "AutoProxy Compatible

List"，以及一定要将 "Reload Every" 设为 15 Minutes，这是由于目前的 Switchy

还不是十分成熟，第一次必须使用这个选项才能正确载入列表。你可以点击 "Error Log" 来查看有没有出错，没有出错再修改为更长的时间。  

  

  







  

gzlxd



Twitter/@gzlxd





8楼 大 中 小 发表于 2010-7-2 20:52  只看该作者



不错，谢谢  

  

  





  

free1989



@photobluer





9楼 大 中 小 发表于 2010-7-2 23:05  只看该作者



引用:



> 原帖由 核子力量 于 2010-7-2 19:38 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  不用自己手动添加的，太麻烦了，用autoproxy的pac就可以  

>  地址：http://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt  

>  把AutoProxy Compatible List的勾挑上，reload every先选最短的15分钟，等第一次更 ...



这个我试过很多次了，都不成功。。。所以没有写上。  

  

  





  

didiaowang





10楼 大 中 小 发表于 2010-7-3 11:37  只看该作者



Connection选择宽带链接的名称（名字一定要英文，中文的话会不正常）  

这个，默认只有一个选项是宽带连接，咋办？  

  

  





  

didiaowang





11楼 大 中 小 发表于 2010-7-3 11:46  只看该作者



引用:



> 原帖由 didiaowang 于 2010-7-3 11:37 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  Connection选择宽带链接的名称（名字一定要英文，中文的话会不正常）  

>  这个，默认只有一个选项是宽带连接，咋办？



已解决，我脑残了~  

  

  





  

icefireboy1



还是本人最纯情





12楼 大 中 小 发表于 2010-7-3 20:27  只看该作者



原帖由 didiaowang 于 2010-7-3 11:37 发表  

Connection选择宽带链接的名称（名字一定要英文，中文的话会不正常）  

这个，默认只有一个选项是宽带连接，咋办？  

已解决，我脑残了~=  

\--------------------------------------------  

求如何解决，我脑残中  

  

  





  

free1989



@photobluer





13楼 大 中 小 发表于 2010-7-3 20:48  只看该作者



引用:



> 原帖由 icefireboy1 于 2010-7-3 20:27 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  原帖由 didiaowang 于 2010-7-3 11:37 发表  

>  Connection选择宽带链接的名称（名字一定要英文，中文的话会不正常）  

>  这个，默认只有一个选项是宽带连接，咋办？  

>  已解决，我脑残了~=  

>  \----------------------------- ...



网络链接里面修改名字。  

  

  





  

scorpion



斯德哥尔摩症患者





14楼 大 中 小 发表于 2010-7-10 21:50  只看该作者



为什么我按照楼主的方法还是无法登陆foursquare,twitter这些网站呢，每一步都是正确的，不会是SSH帐号的问题吧，但已经显示绿色连接上了。  

  

  





  

scorpion



斯德哥尔摩症患者





15楼 大 中 小 发表于 2010-7-10 22:00  只看该作者



可以了，忘记了在Auto switch mode 前面打勾了。  

太谢谢楼主了。  

畅游网络真是愉快呀。  

  

  





  

xgj2008





16楼 大 中 小 发表于 2010-7-13 17:25  只看该作者



谢谢楼主了  

  

  





  

mafanpk





17楼 大 中 小 发表于 2010-7-19 15:04  只看该作者



马克  

  

  





  

cheo2ng



十七 @cheo2ng





18楼 大 中 小 发表于 2010-7-19 16:24  只看该作者



访问Facebook页面错乱，图片不能加载，加https访问就没事，这是怎么回事呢？我觉得是有个地址没有加入rule list.  

我用这个用了很久了，上youtube twitter都没事，就是facebook出问题。  

  

[ 本帖最后由 cheo2ng 于 2010-7-19 16:27 编辑 ]  

  

  





  

invincibility





19楼 大 中 小 发表于 2010-7-19 18:04  只看该作者



look look  

  

  





  

free1989



@photobluer





20楼 大 中 小 发表于 2010-7-26 00:10  只看该作者



引用:



> 原帖由 cheo2ng 于 2010-7-19 16:24 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  访问Facebook页面错乱，图片不能加载，加https访问就没事，这是怎么回事呢？我觉得是有个地址没有加入rule list.  

>  我用这个用了很久了，上youtube twitter都没事，就是facebook出问题。



因为css文件是在另一个地址上：  

http://static.ak.fbcdn.net  

  

  





  

cheo2ng



十七 @cheo2ng





21楼 大 中 小 发表于 2010-7-30 14:46  只看该作者



回复 20楼 free1989 的话题



问题已解决，thx  

  

  





  

chenjin





22楼 大 中 小 发表于 2010-8-21 12:00  只看该作者



请教，我的switchy 里面的Rule没用，无论上什么网站都是走的代理，这个是什么原因？  

  

  





  

chenjin





23楼 大 中 小 发表于 2010-8-21 12:03  只看该作者



回复 22楼 chenjin 的话题



日，脑残了，是我设置的问题。照着教程来是没问题的。  

  

  





  

bugu1212





24楼 大 中 小 发表于 2010-8-28 02:46  只看该作者



我照著步驟來的   鎖也變綠了    步驟相同    名稱也是英文的，就是不成功   上不了youtube   也不能上facebook

不過foursquare到可以   爲什麽啊  

  

[ 本帖最后由 bugu1212 于 2010-8-28 02:56 编辑 ]  

  

  





  

大力夯





25楼 大 中 小 发表于 2010-9-6 10:50  只看该作者



楼主很伟大  

  

  





  

韩非





26楼 大 中 小 发表于 2010-9-6 12:12  只看该作者



长知识！谢谢  

  

  





  

新陳代謝





27楼 大 中 小 发表于 2010-9-7 21:28  只看该作者



引用:



> 原帖由 didiaowang 于 2010-7-3 11:46 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  

>  已解决，我脑残了~



请问咋解决的？  

  

  







  

free1989



@photobluer





28楼 大 中 小 发表于 2010-9-8 00:38  只看该作者



引用:



> 原帖由 bugu1212 于 2010-8-28 02:46 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  我照著步驟來的   鎖也變綠了    步驟相同    名稱也是英文的，就是不成功   上不了youtube   也不能上facebook

> 不過foursquare到可以   爲什麽啊



按照2楼添加规则啊。我建议浏览墙外的网站干脆就切换到SSH，不用Auto Switch模式。浏览在墙内的网站再切换回"Direct Connection"。  

  

平时我都懒得添加规则了，毕竟大部分网站的css，js地址都不一样，一个一个添加太麻烦了。  

  

[ 本帖最后由 free1989 于 2010-9-8 00:39 编辑 ]  

  

  





  

cpkk



司法独立、媒体透明





29楼 大 中 小 发表于 2010-9-9 15:56  只看该作者



看不到图片 郁闷中  

  

  





  

吴辽的人



吴辽的路边围观群众





30楼 大 中 小 发表于 2010-9-14 00:27  只看该作者



不行额。。。我是无线加路由器上网。。。那个NETWORK怎么改？？  

  

[ 本帖最后由 吴辽的人 于 2010-9-14 01:38 编辑 ]  

  

  





  

libertin2046



民主自由小兵





31楼 大 中 小 发表于 2010-9-14 15:51  只看该作者



chrom  那么多妙用阿  我以为就 FIREFOX 强悍而以  学习中~~~  

  

  





  

cibe





32楼 大 中 小 发表于 2010-9-21 00:17  只看该作者



我靠啊。终于成功了。  

  

  





  

sbb_x





33楼 大 中 小 发表于 2010-9-21 15:43  只看该作者



支持个，用tunnelier更好些~  

  

  





  

和谐牌河蟹



和谐社会吃河蟹 @HOY_05





34楼 大 中 小 发表于 2010-9-23 12:12  只看该作者



这个类似于FF+TOR+PROXY,还有手动添加。最好能设置成自动添加，另外我用chrome+tor+swi...的时候，它不能自动辨别国内和国外的网站，导致我出现IE+自由门之类的，无法正常访问国内网站，另外这个碰到国外网站的时候，还不如IE+自由门，自动辨别出去，还有自己添加规则，可以说，继承了上述的缺点，却没有保留它们的优点。  

  

  





  





















    







    













