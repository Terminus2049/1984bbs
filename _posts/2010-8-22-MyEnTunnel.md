---
layout: default

date: 2010-8-22

title: MyEnTunnel

categories: 国家局域网研究所

---





# MyEnTunnel 使用技巧分享



本主题由 库存袈裟 于 2010-8-30 16:42 提升 charmrain



建筑民工





1楼 大 中 小 发表于 2010-8-22 21:00  只看该作者



MyEnTunnel 使用技巧分享



今天使用ssh+autoproxy+FF上网时，突然ssh账号登入不了，显示time out，更换账号后还是不行。  

请问这是否是myentunnel的问题。因为这几个月来，使用myentunnel 从未出现上述问题。  

  

显示如下  

[21:10:09 08/22] plink.exe: FATAL ERROR: Server sent disconnect message  

[21:10:09 08/22] plink.exe: type 2 (protocol error):  

[21:10:09 08/22] plink.exe: "Too many authentication failures for xxxxx"  

[21:10:09 08/22] Disconnected  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



Phillip



路边社特邀围观群众





2楼 大 中 小 发表于 2010-8-22 22:02  只看该作者



是帐号的问题.  

  

  





  

gzlxd



Twitter/@gzlxd





3楼 大 中 小 发表于 2010-8-23 17:14  只看该作者



楼上正解  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





4楼 大 中 小 发表于 2010-8-23 17:41  只看该作者



回复 1楼 charmrain 的话题



http://www.profusehost.net/ipanel/order/index.php?step=3  

试试这家的免空sftp  

方法：https://1984bbs.com/viewthread.php?tid=31667  

  

  





  

xiaolee



草泥马一匹





5楼 大 中 小 发表于 2010-8-23 17:44  只看该作者



是账号问题，不是软件问题，我经常遇到。  

  

  





  

Aragorn



三俗份子





6楼 大 中 小 发表于 2010-8-26 14:58  只看该作者



myentunnel 应该淘汰掉,推荐个更好的程序给你 Tunnelier  

  

  





  

zzug





7楼 大 中 小 发表于 2010-8-26 15:20  只看该作者



回复 6楼 Aragorn 的话题



myentunnel和Tunnelier各有各的好处，怎么能说myentunnel 应该淘汰掉呢！  

myentunnel有中文界面，设置简单明了，是专为代理制作，可以配置多个帐号，使用方便，体积小便于传播……  

我感觉对于只用ssh做代理的人来说Tunnelier唯一的优点就是他支持设置代理服务器，不过一般也没人用这个功能！  

  

[ 本帖最后由 zzug 于 2010-8-26 15:26 编辑 ]  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





8楼 大 中 小 发表于 2010-8-26 15:45  只看该作者



回复 6楼 Aragorn 的话题



已经讨论个此话题，Tunnelier是管理VPS/DS利器但用于翻墙大材小用，Tunnelier速度优与原版MyEnTunnel的原因是使用了Dev版本的plink，使用dev版本plink的MyEnTunnel代理速度和Tunnelier并无差别，且占内存更小，操作也更简易。何来淘汰之说？  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





9楼 大 中 小 发表于 2010-8-26 15:46  只看该作者



回复 6楼 Aragorn 的话题



你可以试试 MyEnTunnel 2010.3.22 优化加速版下载 http://twiapp.alwaysdata.net/myt.rar  

  

  





  

Aragorn



三俗份子





10楼 大 中 小 发表于 2010-8-26 20:11  只看该作者



引用:



> 原帖由 库存袈裟 于 2010-8-26 15:46 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  你可以试试 MyEnTunnel 2010.3.22 优化加速版下载 http://twiapp.alwaysdata.net/myt.rar



学习了,只想到Tunnelier功能的丰富性,没考虑到易用性和体积大小.  

谢谢推荐.  

  

  





  

偶佯疯



我是个读书人





11楼 大 中 小 发表于 2010-8-26 22:08  只看该作者



回复 7楼 zzug 的话题



如何配制多个账户呢？求助  

  

  







  

Aragorn



三俗份子





12楼 大 中 小 发表于 2010-8-27 01:07  只看该作者



MyEnTunnel 使用技巧分享



得"袈裟大师"提醒,并在nemesis2.qx.net获知,plink development 相比 plink release

0.60而言对大数据的传递要来得快速,更加适合视频流和大文件的传递.请参考http://nemesis2.qx.net/pages/MyEnTunnel.  

  

整理打包了截止2010.8.26为止MyEnTunnel官方网址公布的主要两个版本:  

  

1.International Unicode Development Version 3.5.2  

主要支持多国语言.默认布置了中文语言包,并附带英文语言包english_language.txt,需要英文界面支持的话,请重命名或删除language.txt,并重命名目录中的english_language.txt为language.txt.集成plink

Development r8981  

下载 http://www.box.net/shared/xjv2xv57g0  

  

2.Stable Release 3.4.2.1 最新稳定版本.  

集成plink Development r8981  

下载 http://www.box.net/shared/2kcbtyde1l  

  

3.plink2in1.rar中打包了plink Development r8981和plink Release

0.60两个版本的plink,以便随意切换版本,有需要的同学请解压覆盖plink.exe既可.  

下载 http://www.box.net/shared/ob3tb8l5ko  

  

MyEnTunnel 和PuTTY参考网址.  

http://nemesis2.qx.net/pages/MyEnTunnel  

http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html  

  

Aragorn 2010.8.26  

Twitter@Arakung  

  

[ 本帖最后由 Aragorn 于 2010-9-18 17:16 编辑 ]  

  

  





  

神仙一溜烟



杵君





13楼 大 中 小 发表于 2010-8-27 12:04  只看该作者



我觉得另一个反面慢。  

  

  





  

zzug





14楼 大 中 小 发表于 2010-8-27 12:45  只看该作者



引用:



> 原帖由 偶佯疯 于 2010-8-26 22:08 发表 ![](https://1984bbs.com/images/common/back.gif)  

>  如何配制多个账户呢？求助



你看看这个 http://ssh.daili.vc/show-7-1.html  

如果不行你下载 http://sharesend.com/exx4z 试试  

  

  





  

DaemonEye



不河蟹的围观团团员





15楼 大 中 小 发表于 2010-8-27 14:38  只看该作者



还是觉得Tunniler比较好 速度够快 效果也不错 英语不是问题 那点内存更不是问题....  

  

  





  

偶佯疯



我是个读书人





16楼 大 中 小 发表于 2010-8-27 16:15  只看该作者



回复 13楼 zzug 的话题



谢谢配置成功  

  

  







  

前列县县长



后进青年





17楼 大 中 小 发表于 2010-8-27 20:20  只看该作者



freessh.us试试这里的账号吧。  

  

  





  

xihawangzi





18楼 大 中 小 发表于 2010-8-27 22:37  只看该作者



是不是每次用myentunnel都得要输入用户名和密码啊？  

  

  





  

zzug





19楼 大 中 小 发表于 2010-8-28 08:55  只看该作者



引用:



> 原帖由 xihawangzi 于 2010-8-27 22:37 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  是不是每次用myentunnel都得要输入用户名和密码啊？



不是的myentunnel可以记住用户名和密码只需输入一次以后都不用了！  

  

  





  

xihawangzi





20楼 大 中 小 发表于 2010-8-28 12:36  只看该作者



回复 18楼 zzug 的话题



那为什么下一次打开myentunnel时，服务器名，用户名，密码都是空白的呢，每次都要重新输入啊  

  

  





  

zzug





21楼 大 中 小 发表于 2010-8-28 12:53  只看该作者



回复 19楼 xihawangzi 的话题



你没有点击保存按钮吧？  

  

  





  

极光掠天



理想：為天地立心，為生民立命，為往聖繼絕學，為萬世開太平。





22楼 大 中 小 发表于 2010-8-29 11:18  只看该作者



求助 关于MyEntunnel问题



网通的，原来是ADSL拨号，一直用着没问题，现在加了一个路由器，就出现下面的问题了  

  

[11:01:25 08/29] 加载plink核心中...  

[11:01:29 08/29] plink.exe: FATAL ERROR: Network error: Connection refused  

[11:01:29 08/29] 已断开  

  

重启了还是这个样子...没经过连接，直接上网MyEntunnel还不能识别吗？太奇怪了...  

  

==============================================================================  

今天刚发邮件了，没注意，ssh帐号关闭了...  

请小黑屋吧，麻烦大家了。  

  

[ 本帖最后由 极光掠天 于 2010-8-29 13:07 编辑 ]  

  

  





  

circle_square





23楼 大 中 小 发表于 2010-8-29 11:34  只看该作者



用路由了，本来就已经相当于设置一层代理了~~  

  

  





  

zzug





24楼 大 中 小 发表于 2010-8-29 12:04  只看该作者



回复 1楼 极光掠天 的话题



你换其他ssh帐号试试，不行换Tunnelier试试  

  

  





  

极光掠天



理想：為天地立心，為生民立命，為往聖繼絕學，為萬世開太平。





25楼 大 中 小 发表于 2010-8-29 13:08  只看该作者



回复 3楼 zzug 的话题



嗯，谢谢，原因是ssh帐号关闭了...  

  

  





  

库存袈裟



@bruceku 想象力比知识更重要。





26楼 大 中 小 发表于 2010-8-30 10:51  只看该作者



Nice!加入本版精华。  

  

  





  

核子力量



Twitter.com/hzpower





27楼 大 中 小 发表于 2010-8-30 12:03  只看该作者



很用心，辛苦了  

  

  







  

imus



升斗小民





28楼 大 中 小 发表于 2010-8-30 12:11  只看该作者



用这个软件是不是一定要有ssh账号？  

  

  







  

Aragorn



三俗份子





29楼 大 中 小 发表于 2010-8-30 14:06  只看该作者



感谢袈裟大师抬爱了.还是多亏你的提醒了  

  

  





  

Aragorn



三俗份子





30楼 大 中 小 发表于 2010-8-30 14:06  只看该作者



引用:



> 原帖由 imus 于 2010-8-30 12:11 发表

> ![](https://1984bbs.com/images/common/back.gif)  

>  用这个软件是不是一定要有ssh账号？



SSH是必须的.  

  

  





  

zzug





31楼 大 中 小 发表于 2010-8-30 16:32  只看该作者



MyEnTunnel 创建多个 SSH 账户



不知有没人遇到跟我相同的情况，MyEnTunnel

3.5.2右键点击托盘图标，“配置”一项是不可选的，而在软件主界面中也没有任何创建新“配置”的选项。但3.4.1似乎就没有这个问题。如果你只有一个SSH账户，或你用的是3.4.1稳定版，请忽略本文。  

![](http://img.ilemoned.com/myentunnel-multi-ssh-acc.jpg)  

解决方法如下：  

Win+R，输入MyEnTunnel完整路径，空一格再加个新配置，如：  



> D:\MyEnTunnel\myentunnel.exe MediaTemple  

>



（当然你也可以通过建立快捷方式并编辑之来达到相同目的，不赘述了。）  

编辑完SSH账户信息并保存后，程序目录会多出来3个配置文件。这时退出并再次运行 MyEnTunnel，“配置”一项即变为可选，也可以直接创建新账户了。  

再给个tips：MyEnTunnel的作者在主页上说了，使用dev

build的plink.exe会快很多。我换了看youtube速度果然是质的飞跃。PuTTY 官网就能下载到，自己仔细找找。  

多配置dev build的plink.exe的MyEnTunnel下载  http://sharesend.com/exx4z  

  

  





  

明月照积雪





32楼 大 中 小 发表于 2010-8-31 23:05  只看该作者



留个记号  

  

  





  





















    







    













