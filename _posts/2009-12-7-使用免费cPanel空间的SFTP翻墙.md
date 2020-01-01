---
layout: default

date: 2009-12-7

title: 使用免费cPanel空间的SFTP翻墙

categories: 国家局域网研究所

---





# 使用免费cPanel空间的SFTP翻墙 [图文教程]



本主题由 库存袈裟 于 2009-12-22 16:01 分类 库存袈裟



@bruceku 想象力比知识更重要。





1楼 大 中 小 发表于 2009-12-7 11:58  只看该作者



使用免费cPanel空间的SFTP翻墙 [图文教程]



1.前往FreeWebSpace寻找cPanel的免费空间  

FreeWebSpace论坛Free hosting offers 板块：  

http://www.freewebspace.net/forums/forumdisplay.php?f=32  

  

注意事项：  

1.注意分清cPanel/iPanel/LayeredPanel/VistaPanel/DirectAdmin，本教程仅对部分cPanel空间有效  

2.并非所有cPanel都支持SSH转发，需测试  

3.尽量不要在发帖得空间（post4host/P4H/P2H）这类免费空间上消耗太多时间  

4.申请到的空间除了用来翻墙外不要闲置，放个twitter api或者wordpress吧。  

twitter api下载地址：  

乌鸦嘴 http://btchina.bos.ru/ssh/tw.zip  

kwestion http://code.google.com/p/kwestion/  

  

  

下面以某免费空间申请过程简单讲解  

  

2.选择免费空间  

  

找到免费空间后，前往申请界面，一般cPanel空间即时申请有WHCMS/iPanel两种，步骤与填写内容基本相似，下面我们以WHCMS例：  

  

Shopping Cart  

![](http://btchina.bos.ru/ssh/00.jpg)  

  

3.选择域名  

  

![](http://btchina.bos.ru/ssh/01.jpg)  

  

这一步WHCMS和iPanel的区别：WHCMS此步输入的域名（无论是顶级域名还是二级域名）将成为后面登录用的CP用户名，而iPanel则在最后一步自行选择用户名。  

  

4.附件选项  

  

![](http://btchina.bos.ru/ssh/02.jpg)  

  

基本上没啥可选，往往此步都是收费项目  

  

5.购物车  

  

![](http://btchina.bos.ru/ssh/03.jpg)  

  

确认无误，checkout  

  

6.完善注册信息  

  

![](http://btchina.bos.ru/ssh/04.jpg)  

切记：根据实际网络接入所属地域填写，若通过北京网通申请而填写华盛顿的地址，管理员审查时会根据IP地址判定为欺诈驳回申请。具体到街道门牌号可不如实。  

  

![](http://btchina.bos.ru/ssh/05.jpg)  

  

7.前往邮箱收信  

  

![](http://btchina.bos.ru/ssh/06.jpg)  

  

这一步WHCMS和iPanel的区别：WHCMS此步多数不会收到一封带有激活链接的邮件，而iPanel则会收到一封带有激活链接的邮件，以防SPAM。但无论WHCMS还是iPanel都有可能等待管理员人工才能开通。所以第六步中的信息真实性格外重要。  

  

有人工审核的空间，此步将不能即时收到第三封邮件，审核通过后方可收到。  

  

8.账户信息邮件  

  

![](http://btchina.bos.ru/ssh/07.jpg)  

  

9.登录cPanel  

  

![](http://btchina.bos.ru/ssh/08.jpg)  

  

![](http://btchina.bos.ru/ssh/09.jpg)  

  

左侧展开后  

![](http://btchina.bos.ru/ssh/10.jpg)  

  

点击FTP Accounts  

![](http://btchina.bos.ru/ssh/12.jpg)  

  

点击Configure FTP Client  

![](http://btchina.bos.ru/ssh/13.jpg)  

  

修改密码  

![](http://btchina.bos.ru/ssh/11.jpg)  

  

  

下面的步骤与下载软件请参考  

https://1984bbs.com/viewthread.php?tid=38397  

  

10.运行MyEnTunnel并填写如下信息  

![](http://btchina.bos.ru/ssh/14.jpg)  

  

确认指纹警告  

![](http://btchina.bos.ru/ssh/15.jpg)  

  

  

==========================================  

1984BBS原创教程  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



lynnstar





2楼 大 中 小 发表于 2009-12-7 12:44  只看该作者



mark  

  

  





  

rex5652





3楼 大 中 小 发表于 2009-12-7 13:10  只看该作者



支持支持！已经有了SSH了…呵呵  

  

  





  

imus



升斗小民





4楼 大 中 小 发表于 2009-12-7 13:11  只看该作者



记号.  

  

  







  

magicbully





5楼 大 中 小 发表于 2009-12-7 13:14  只看该作者



看看。袈裟辛苦了。  

  

  





  

法不阿Quei



我活在世上，无非是想明白些道理，看见些有趣的事情。





6楼 大 中 小 发表于 2009-12-7 13:18  只看该作者



TOR VPN PUFF 和门界什么的都用了 就差这个了  

  

  





  

jkgtw





7楼 大 中 小 发表于 2009-12-7 13:22  只看该作者



太棒了！做个记号～  

  

  





  

scorpion



斯德哥尔摩症患者





8楼 大 中 小 发表于 2009-12-7 13:23  只看该作者



做个记号，有备无患。  

  

  





  

savagekw





9楼 大 中 小 发表于 2009-12-7 13:52  只看该作者



袈裟兄果然凶猛  

  

  





  

核子力量



Twitter.com/hzpower





10楼 大 中 小 发表于 2009-12-7 13:59  只看该作者



这个目前来看是最好的，小众，分散  

  

另求指点，myentunnel面板里面的“启用压缩”选项是干什么的，勾上之后有效果吗  

还有“启用慢速轮询“”动态socks“都是什么意思，麻烦高人解释一下，多谢  

  

  







  

m3g4





11楼 大 中 小 发表于 2009-12-7 14:09  只看该作者



刚在推特上看到北风发了，被RT了很多次  

  

  





  

huntou





12楼 大 中 小 发表于 2009-12-7 14:17  只看该作者



遭党国记恨的东西  

  

  





  

Phillip



路边社特邀围观群众





13楼 大 中 小 发表于 2009-12-7 14:25  只看该作者



哈哈



现在翻墙的方式已经发展到分散化去和中心化, 更加隐蔽. 封锁难度越来越大了.  

  

  





  

psuidt



我的血是热的





14楼 大 中 小 发表于 2009-12-7 14:37  只看该作者



奇怪,我注册登录后,在左侧，没有找到Shared Ip Addres  

  

  





  

偶佯疯



我是个读书人





15楼 大 中 小 发表于 2009-12-7 14:40  只看该作者



哈哈，成功翻过  

  

  







  

open5235





16楼 大 中 小 发表于 2009-12-7 14:41  只看该作者



收藏先，再来看  

  

  





  

ericrazy



民工丙





17楼 大 中 小 发表于 2009-12-7 14:42  只看该作者



正在试验中  

  

  





  

Dean_H



火星人





18楼 大 中 小 发表于 2009-12-7 14:48  只看该作者



这就去自己的空间试试。  

  

  





  

穆木





19楼 大 中 小 发表于 2009-12-7 14:51  只看该作者



好，学习一下，马上实践。  

  

  





  

ilili



该用户已被删除





20楼 大 中 小 发表于 2009-12-7 14:55  只看该作者



已經用上了,很好用,可以忘了輪子那些軟體了  

  

  





  

iwanderer



leslie





21楼 大 中 小 发表于 2009-12-7 14:56  只看该作者



两个注册连接还有效吗？我这怎么都404NOT FOUND了  

  

  





  

heran168





22楼 大 中 小 发表于 2009-12-7 14:59  只看该作者



回复 14楼 psuidt 的话题



不知道怎么登陆cPanel后台，没有找到Shared Ip Addres。请哪位师兄指点。  

  

  





  

ericrazy



民工丙





23楼 大 中 小 发表于 2009-12-7 15:06  只看该作者



试了几个注册到后面都是要钱的啊？  还是我英语太烂了 找错地方了  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





24楼 大 中 小 发表于 2009-12-7 15:10  只看该作者



引用:



> 原帖由 ericrazy 于 2009-12-7 15:06 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  试了几个注册到后面都是要钱的啊？  还是我英语太烂了 找错地方了



引用:



> 原帖由 iwanderer 于 2009-12-7 14:56 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  两个注册连接还有效吗？我这怎么都404NOT FOUND了



试试这个  

http://hostaider.com/tht/order/  

  

  





  

orange0422



orange0422





25楼 大 中 小 发表于 2009-12-7 15:12  只看该作者



我两个带cPanel功能的国外空间0fees.net和byteact.com。可是都找不到Shared Ip Address在哪，楼主能不能放两张截图  

  

  







  

木羊犬





26楼 大 中 小 发表于 2009-12-7 15:13  只看该作者



在byethost.com 注册的，可是登入http://cpanel.byethost14.com后在control panel下没有看见Shared

Ip Address这个选项，有成功的提点下啊，最好有图解，看的明明白白。  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





27楼 大 中 小 发表于 2009-12-7 15:14  只看该作者



回复 26楼 木羊犬 的话题



byethost是vista panel  

经常会有鸡贼的主机商拿免费的vista panel写成control panel企图冒充cPanel，鱼目混珠。  

  

  





  

iwanderer



leslie





28楼 大 中 小 发表于 2009-12-7 15:15  只看该作者



还是不行。。  

看来是我这里电信的问题了。。  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





29楼 大 中 小 发表于 2009-12-7 15:20  只看该作者



找不到 cPanel免费空间？来这里



http://www.freewebhostingtalk.com/forumdisplay.php?f=3  

  

http://www.freewebspace.net/forums/forumdisplay.php?f=32  

  

http://www.hostbidder.com/forumdisplay.php?&f=14  

  

技巧：  

1\. 确认是cPanel空间，control panel 不等于cPanel  

2\. 无视post2host  

3\. 不要在乎空间与流量，SSH流量很少会被记入总流量  

4\. 节省资源每个免费空间最多申请一个可用的，留点子弹给别人  

  

  





  

orange0422



orange0422





30楼 大 中 小 发表于 2009-12-7 15:31  只看该作者



回复 27楼 库存袈裟 的话题



果然我那两个都是vistapanel...在http://hostaider.com/tht/order/成功了，可翻墙，速度50K/s左右，目前用puff能有200K/S，这个作为备用翻墙手段...感谢楼主  

  

  







  

yuishy



保尔





31楼 大 中 小 发表于 2009-12-7 15:45  只看该作者



回复 24楼 库存袈裟 的话题



得到了IP地址和SFTP端口，怎么使用  

ssh -qTfnN -D 7070 username@sshserver.com  

这类命令呢？  

  

  







  

bressanon84





32楼 大 中 小 发表于 2009-12-7 15:47  只看该作者



不错不错，收藏之  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





33楼 大 中 小 发表于 2009-12-7 15:54  只看该作者



引用:



> 原帖由 yuishy 于 2009-12-7 15:45 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  得到了IP地址和SFTP端口，怎么使用  

>  ssh -qTfnN -D 7070 username@sshserver.com  

>  这类命令呢？



https://dl.getdropbox.com/u/873345/howto/windows+firefox.html  

  

  





  

orange0422



orange0422





34楼 大 中 小 发表于 2009-12-7 15:59  只看该作者



另外请问楼主如何能把网页架设到dropbox的空间上？  

  

  







  

srainlx





35楼 大 中 小 发表于 2009-12-7 16:04  只看该作者



这应该属于人民战争的范畴了吧，嘿嘿 MARK一个！  

  

  





  

kidywd





36楼 大 中 小 发表于 2009-12-7 16:11  只看该作者



奇怪,我注册登录后,在左侧，没有找到Shared Ip Addres  

  

  





  

鞋带么



谦谦君子 温润如玉 我TMD 还需努力





37楼 大 中 小 发表于 2009-12-7 16:24  只看该作者



记号，收藏备用。  

  

  





  

chenshu





38楼 大 中 小 发表于 2009-12-7 16:28  只看该作者



收啊  

  

回去再试  

  

  





  

ericrazy



民工丙





39楼 大 中 小 发表于 2009-12-7 16:31  只看该作者



回复 30楼 orange0422 的话题



现在用上puff了 谢谢orange0422  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





40楼 大 中 小 发表于 2009-12-7 16:42  只看该作者



引用:



> 原帖由 psuidt 于 2009-12-7 14:37 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  奇怪,我注册登录后,在左侧，没有找到Shared Ip Addres



引用:



> 原帖由 kidywd 于 2009-12-7 16:11 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  奇怪,我注册登录后,在左侧，没有找到Shared Ip Addres



http://www.freewebspace.net/free/AdvSearchR/1/22  和 http://www.free-

webhosts.com/search-webhosts.php?SA=cPanel  

为免费空间资讯网站并不提供免费空间，请在这两处寻找合适的空间并前往注册、申请。  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





41楼 大 中 小 发表于 2009-12-7 16:44  只看该作者



引用:



> 原帖由 orange0422 于 2009-12-7 15:59 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  另外请问楼主如何能把网页架设到dropbox的空间上？



将网页文件存储至Public文件夹即可。  

  

  





  

主席下一小兵



https://twitter.com/yixiaobing





42楼 大 中 小 发表于 2009-12-7 17:04  只看该作者



我没有摸出来怎么用，主要是前面的注册账号和获取ip没有搞出来。教程对没有用过SSH的人来说有点太简化了，建议搞个详细一点的帖子。  

  

  







  

主席下一小兵



https://twitter.com/yixiaobing





43楼 大 中 小 发表于 2009-12-7 17:05  只看该作者



恩，还有后面的上传空间什么的，对于没干过这些的人来说有点困难，最好有个示意图。  

  

  







  

youttiao



微博PM





44楼 大 中 小 发表于 2009-12-7 17:36  只看该作者



hostaider经常掉线啊，不知道怎么回事  

  

  







  

Phillip



路边社特邀围观群众





45楼 大 中 小 发表于 2009-12-7 17:42  只看该作者



回复 40楼 库存袈裟 的话题



我在hostaider 注冊了, 但為啥2082端口登錄進不去? 用戶名密碼都正確. 是不是被墻了?  

我去掉端口直接輸入地址, 是一片空白, 但翻墻可以看到默認示例的Index頁面. 如果這樣的話是不是不能用這個翻墻了?  

  

  





  

Phillip



路边社特邀围观群众





46楼 大 中 小 发表于 2009-12-7 17:56  只看该作者



回复 44楼 youttiao 的话题



你能登錄你的cpanel嗎? 我的一直登陸不了  

  

  





  

farfatfay





47楼 大 中 小 发表于 2009-12-7 19:24  只看该作者



我用的hostaider的那个,myentunnel小锁已经绿色了,按照win+firefox那篇设置的,还是没法翻墙,不知是什么原因?  

  

  





  

wodeid





48楼 大 中 小 发表于 2009-12-7 19:30  只看该作者



非常感谢  

  

  





  

uinstriv





49楼 大 中 小 发表于 2009-12-7 19:44  只看该作者



喜欢SSH  

  

  





  

马蜂





50楼 大 中 小 发表于 2009-12-7 21:21  只看该作者



两眼一抹黑～



我对英文完全不懂，但是这么好的机会不趁机申请一个就会后悔莫及！  

有请技术控同学帮忙申请一个，顺便搭一个奶瓶腿，本人愿意用适当银钱作为酬谢。  

求好心人帮忙申请一个私人专用ssh，站内消息联系。  

  

这里有搭建奶瓶腿教程：http://zou.lu/diy-your-twitter-clients/  

  

[ 本帖最后由 马蜂 于 2009-12-7 21:22 编辑 ]  

  

  





  



 266 123456››





















    







    













