---
layout: default

date: 2010-1-29

title: 警告：Firefox和微软已将CNNIC添加到根证书列表中

categories: 国家局域网研究所

---





# 警告：Firefox和微软已将CNNIC添加到根证书列表中



本主题由 张书记 于 2010-2-4 12:28 合并 bbscn



长期不明真相的围观群众





1楼 大 中 小 发表于 2010-1-29 05:34  只看该作者



警告：Firefox和微软已将CNNIC添加到根证书列表中



源地址：http://www.cnbeta.com/articles/103170.htm  

感谢流氓不可怕，就怕流氓有证实的投递  

SummerWa 写道 "Microsoft和Firefox已经将CNNIC作为根证书颁发机构添加到证书列表中……"  

IE 8, Firefox 3.6以及Chrome都会受到影响，可证实该消息的来源：  

  

Microsoft 的PDF  

https://bugzilla.mozilla.org/show_bug.cgi?id=47676 6  

https://bugzilla.mozilla.org/show_bug.cgi?id=52500 8  

  

如果不信任该证书，可以按这里的方法操作。  

  

新闻来源:solidot  

  

  

  

+++++++++++++++++++++++++氧化钙GFW的分割线+++++++++++++++++++++++++  

  

  

源地址：http://felixcat.net/2010/01/throw-out-cnnic/  

  

  

                      

  

CNNIC，我不信任你！ ——从“受信任的根证书”里赶走CNNIC  

Posted by Felix Yan in Uncategorized on 27-01-2010  

  

在Twitter上惊闻“微软把CNNIC列为根证书发布者”，赶紧Google一把，发现 Mozilla同样也已经在3.6版的Firefox里这么做了。  

  

出于对CNNIC深深的不信任，我决定将CNNIC ROOT从“受信任”的列表里赶出去。  

  

因为IE/Chrome采用微软的CA目录，而微软现在暂未将CNNIC加入，因此需要先从Firefox中导出这几个证书，再添加到Windows的“不信任”列表(更新：现在可以直接从Windows里导入再导入了，操作类似)，以防范于未然。下面便是具体的步骤了（包括IE/Chrome/Firefox）：  

  

1、如果没有安装Firefox浏览器的3.6最新版，或者在下面的操作中没有找到相应的证书，可以从这里下载这三个证书，然后跳到第5步：CNNICROOT.crt

CNNICSSL.crt Entrust.netSecureServerCertificationAuthority.crt  

  

2、打开Firefox浏览器，工具(Tools)->选项(Options)->高级(Advanced)->加密

(Encryption)->查看证书(View Certificates)  

  

3、在证书机构(Authorites)标签页中找到”CNNIC“组的”CNNIC ROOT“项，按导出(Export)（备份到本地），然后删除

(Delete)。（RT JimmyXu:在Firefox里对自带根证书执行“删除”操作就相当于是禁用其所有目的，并不会将其删除。）  

  

4、在”Entrust.net“组中找到”Entrust.net Secure Server Certification

Authority“(序列号37:4A:D2:43的)和”CNNIC

SSL“证书，同样导出并删除。（注：Entrust.net这个也是验证CNNIC所用的证书）  

  

﻿  

  

5、打开开始菜单->运行（或者直接按Win-R）  

  

6、输入certmgr.msc，打开Windows 的证书管理器。  

  

7、展开”不受信任的证书(Untrusted Certificates)“，右键单击其下”证书(Certificates)“项，在”所有任务(All

Tasks)“子菜单下单击”导入(Import)…“  

  

8、分别找到刚才保存的三个证书，依次导入(Next->Browse…(找到相应文件)->Next->Next->Finish)。  

  

9、将导入的证书复制(Ctrl-C)，然后粘贴(Ctrl-V)到受信任的证书颁发者(Trusted Root Certification

Authorities)中，然后在这个窗口中分别右键单击粘贴过来的3个证书，选择“属性(Properties)”，然后单击“停用这个证书的所有目的(Disable

all purposes for this certificate)”。  

  

（感谢 Jimmy Xu 供图）  

  

想检验操作是否成功？在浏览器里访问 https://www.enum.cn/ ，如果提示证书被拒绝，就证明操作成功了！  

  

——————7:30 PM更新——————  

  

不需要关闭自动更新，上述步骤多了第9步，请注意！  

  

——————6:15 PM更新！！——————  

  

0、在默认情况下，微软会自动连接到Windows Update服务器更新CA列表，这样会导致以下操作对IE/chrome失效，具体解决方法：  

  

0a:对于Windows XP用户：控制面板(Control Panel)->添加/删除程序(Add/Remove

Programs)->添加/删除windows组件(Add/Remove Windows Components)->取消勾选“更新根目录证书(Update

Root Certificates)”  

  

（感谢推友@tOmMyanG供图！）  

  

0b:对于Windows Vista/Windows 7用户：组策略(运行->gpedit.msc)->计算机配置(Computer

Configuration)->管理模板(Administrative Templates)->系统(System)->Internet

通信管理(Internet Communication Management)->Internet 通信设置(Internet Communication

settings)，启用(Enable)“关闭自动根证书更新(Turn off Automatic Root Certificates Update)”  

  

十分感谢推友 @Ratoo 和 @jimmy_xu_wrk 在这个问题上对我的帮助：）  

  

（另：十分感谢使用中文版系统的朋友告诉我相应选项在中文版中的名字，谢谢！）  

  

参考资料：http://www.networkworld.com/community/node/17703  

  

[ 本帖最后由 bbscn 于 2010-1-29 05:36 编辑 ]  

  

  





  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



bbscn



长期不明真相的围观群众





2楼 大 中 小 发表于 2010-1-30 16:21  只看该作者



没人关注啊，我来解释一下吧。难保有那么一天，TG劫持dns，做个假的GMAIL.COM，你在不知情的情况下把密码就告诉他了。  

  

  





  

pillarchang





3楼 大 中 小 发表于 2010-1-30 18:47  只看该作者



记号～ 有点繁琐  

  

  





  

jason32





4楼 大 中 小 发表于 2010-1-30 18:54  只看该作者



自从删完那个 我的ＦＦ就打不开任何网页了  

  

  





  

Phillip



路边社特邀围观群众





5楼 大 中 小 发表于 2010-1-30 21:31  只看该作者



有个副作用, 就是网易的邮箱无法SSL安全登录了, 因为用的就是CNNIC的证书  

  

不过也无所谓, 网易邮箱就是不存什么重要信息的.  

  

  





  

王九蛋





6楼 大 中 小 发表于 2010-1-31 00:23  只看该作者



删除CNNIC根证书，附方法  

文章提交者：灵鹫山 加帖在 猫眼看人 【凯迪网络】 http://www.kdnet.net  

  

   "Microsoft和Firefox已经将CNNIC作为根证书颁发机构添加到证书列表中……"IE 8, Firefox

3.6以及Chrome都会受到影响。我是非常不信任这个CNNIC的根证书的，立刻检查系统，已经手动将这个“CNNIC ROOT”，给删除出受信任列表了。  

    最简单办法，打开IE或者TT浏览器，工具-----intenet选项------内容------受信任证书，在列表之下把全部c字母开头的根证书里，很容易就能把颁发机构为CNNIC的根证书揪出来，然后删除它！  

    如果你是用的是Firefox浏览器，按照如下详细设置办法可以将CNNIC颁发的根证书全部列禁！  

    http://felixcat.net/2010/01/throw-out-cnnic/  

    和莫名其妙的可能监控以及流氓软件有关的根证书，给我滚！  

   注：操作完毕之后，记得进入控制面板----添加或删除程序-------

添加或删除windows组件，找出更新根证书目录，把那钩去掉，点击下一步，彻底把CNNIC死气掰咧给你自动植入的通路给封锁掉，要不你前脚删除，后脚他有它又偷偷给你安上。  

     还有一种情况，可能您的电脑里有和cnnic有关的赖皮软件隐藏着，您发现多次删除，cnnic还在偷偷给您植入证书，那您采取如下狠招对付它：  

    运行certmgr.msc，然后，受信任的证书颁发机构，然后，cnnic root双击，然后，详细信息，然后 编辑属性， 最后下狠手，停用这个证书的所有目的！  

  

  





  

weke



挪威.奥斯陆





7楼 大 中 小 发表于 2010-1-31 00:37  只看该作者



just巳全删所有证书，不影响上网。  

  

  





  

fp456789





8楼 大 中 小 发表于 2010-1-31 22:21  只看该作者



SSL会话将恐遭遇劫持，Firefox和微软已将CNNIC添加到根证书列表中！



从cnBeta上看到的消息（http://www.cnbeta.com/articles/103170.htm）：  

  

  

SummerWa 写道 "Microsoft和Firefox已经将CNNIC作为根证书颁发机构添加到证书列表中……"  

IE 8, Firefox 3.6以及Chrome都会受到影响，可证实该消息的来源：  

  

Microsoft 的PDF ：http://docs.google.com/viewer?ur ... vember%25202009.pdf  

https://bugzilla.mozilla.org/show_bug.cgi?id=47676 6  

https://bugzilla.mozilla.org/show_bug.cgi?id=52500 8  

  

如果不信任该证书，可以按这里的方法操作。  

  

新闻来源:solidot  

  

附：  

除去CNNIC证书的方法：CNNIC，我不信任你！——从“受信任的根证书”里赶走CNNIC

http://felixcat.net/2010/01/throw-out-cnnic/  

  

[ 本帖最后由 fp456789 于 2010-1-31 22:43 编辑 ]  

  

  





  

飞牛





9楼 大 中 小 发表于 2010-1-31 23:10  只看该作者



标记学习  

  

  





  

坚壁清野





10楼 大 中 小 发表于 2010-1-31 23:12  只看该作者



学习。  

  

  





  

kurverse





11楼 大 中 小 发表于 2010-2-1 19:42  只看该作者



学习了  

  

  





  

rationalcrow



拆呐拆呐不拆怎么成china





12楼 大 中 小 发表于 2010-2-2 10:01  只看该作者



AutoProxy 作者WCM《CNNIC CA：最最最严重安全警告！》



http://autoproxy.org/zh-CN/node/66  

最新进展：  

受DDOS 攻击下线，存档： https://docs.google.com/View?id=d5j3s7p_7f9r489fg  

  

各位，虽然此事与 AutoProxy 无关，但它对所有（也包括 AutoProxy）用户都是一个非常严重的安全威胁。我，WCM，AutoProxy

作者，以个人名誉强烈建议您认真阅读并采取措施。  

  

背景知识  

  

网上传输的任何信息都有可能被恶意截获。尽管如此，我们仍然在网上保存着很多重要的资料，比如私人邮件、银行交易。这是因为，有一个叫着 SSL/TLS/HTTPS

的东西在保障我们的信息安全，它将我们和网站服务器的通信加密起来。  

  

如果网站觉得它的用户资料很敏感，打算使用 SSL/TLS/HTTPS 加密，必须先向有 CA (Certificate Authority)

权限的公司/组织申请一个证书。有 CA 权限的公司/组织都是经过全球审核，值得信赖的。  

  

  

发生了什么事  

  

最近，CNNIC——对，就是那个臭名昭著的利用系统漏洞发布流氓软件的、就是那个使劲忽悠 CN 域名又突然停止域名解析的 CNNIC

(中国互联网络信息中心)，它——偷偷地获得了 CA 权限！在所有中文用户被隐瞒的情况下！  

  

  

意味着什么  

  

意味着 CNNIC 可以随意造一个假的证书给任何网站，替换网站真正的证书，从而盗取我们的任何资料！  

  

这就是传说中的 SSL MITM 攻击。以前这个攻击不重要是因为攻击的证书是假的，浏览器会告诉我们真相；现在，因为 CNNIC 有了 CA

权限，浏览器对它的证书完全信任，不会给我们任何警告，即使是造假的证书！  

  

你信任 CNNIC (中国互联网络信息中心) 吗？你相信它有了权限，会安守本分，不会偷偷地干坏事吗？  

我对此有3个疑问：  

  

   1\. 某 party 对 GMail 兴趣浓厚，GFW 苦练 SSL 内功多年，无大进展。如今有了 CA，若 GFW 令下，CNNIC 敢不从否？  

   2\. CNNIC 当年利用所谓官方头衔，制流氓软件祸害网民。如今有了 CA，如何相信它不会故伎重演？  

   3\. 为了得到指定网站的合法证书，其它流氓公司抛出钱权交易，面对诱惑，CNNIC 是否有足够的职业操守？  

  

  

影响范围  

  

基本上所有浏览器的所有用户均受影响！  

  

  

行动第一步：立即安全防御  

  

在此只介绍 Firefox 浏览器的防御方法，其它浏览器的用户请自行 Google，原理类似。  

  

    * 菜单栏：工具/编辑->首选项->高级->加密->查看证书->证书机构(Authorites)  

    * 这是一个很长的列表，按照字母顺序，你应该能找到一个叫着 "CNNIC ROOT" 的记录，就是这个东西，告诉 Firefox，我们不信任它！  

    * 选中 CNNIC ROOT，点击下面的“编辑”按钮，弹出一个框，应该有3个选项，把所有选项的勾都去掉！保存。  

    * 还没有完，狡兔有三窟。  

    * 接着往下找，有一个叫着 Entrust.net 的组，这个组里应该有一个 "CNNIC SSL" (如果没有，访问一下 这个网站 就有了)  

    * 别急着下手，这回情况不一样，这个证书是 Entrust 签名的。我们信任 Entrust，Entrust 说它信任 CNNIC，所以我们就被迫信任 CNNIC SSL 了。找到 "Entrust.net Secure Server Certification Authority" 这一条，同上面一样，把3个选项的勾都去掉，保存（提示：取消了对 Entrust 的信任以后，可能会没法打开它签名的某些正常网站。至于哪个网站用了它的签名，随便试了一下，没找到例子）。  

    * 最后，让我们验证一下。重启 Firefox，打开 这个 和 这个 网站，如果Firefox 对这两个网站都给出了安全警告，而非正常浏览，恭喜，您已经摆脱了 CNNIC CA 的安全威胁！  

  

  

行动第二步：治标还需治本  

  

几天前听到这个消息的时候，我简单地、轻蔑地将 CNNIC 删除了事。可是这个周末，我忽然觉得这样很不好。因为只要它存在，始终会有大部分的用户受到威胁。和写

AutoProxy

时同样的想法：如果大部分人都处于安全威胁当中，一个人苟且偷安又有什么意义？如果不能将自由与安全的门槛降低一点点，所谓的技术又有什么好侥幸的？  

  

所以我呼吁大家，贡献一点时间和知识，团结起来说服各浏览器取消 CNNIC 的 CA 权限。这种事不可能有公司来推动，只有我们社区。  

  

首先推荐的是 Firefox，作为一个公益组织 Mozilla 的决策过程更为开放、更愿意听取社区的声音。Bug 476766 记录了事件的全过程。Bug

542689 和 Mozilla.dev.security.policy 进行着现在的讨论（注意，你可以把自己添加到 Bugzilla 的 CC List

以表达你对此事的关切。但是不要随便说一些不靠谱的话，免遭讨厌。强调政治、GFW

的之类的不管用，必须就事论事。比如它在申请过程中采取欺骗、隐瞒的手段，或者申请成功后的某些行为违反了 Mozilla 的 CA

政策；比如它的属性和过往行为表明它不会忠于自己的职责，而(帮助)做出 MITM 这种 CA 共愤的事情）。  

  

其次是 Entrust，它说它信任，导致了我们也被迫信任 CNNIC SSL。不妨 告诉 Entrust 此事很严重，因为它错误地信任了

CNNIC，大量用户不得不删除它的 CA。如果能找到使用 Entrust 证书的网站更好。给这些网站写信，因为此次事件我们不得不删除了 Entrust 的

CA，请求他们另选别家认证。如果反响强烈，势必给 Entrust 造成很大压力。  

  

除此之外，来投个票吧（结果统计）！  

  

最后，强烈建议大家，发现证书警告的时候最好直接关掉，不要轻易添加例外。证书的信任体系是一级依赖一级的，一不小心你可能就会连带信任一个不想信任的

CA。上面用于验证的两个网站，不妨定期（每周/每月）测一测，如果哪天你发现其中的任何一个网站没有证书警告，就要注意了！  

  

各位：  

DNS 劫持已然成为常态，不要让 SSL 劫持再次普及！此事刚刚发布，尚有评议空间。待时间流逝，你我皆成温水中之青蛙！  

  

[ 本帖最后由 rationalcrow 于 2010-2-2 10:14 编辑 ]  

  

  





  

albert_qhd





13楼 大 中 小 发表于 2010-2-2 10:11  只看该作者



同意！已删除之  

  

  





  

rationalcrow



拆呐拆呐不拆怎么成china





14楼 大 中 小 发表于 2010-2-2 10:12  只看该作者



AutoProxy 官网因为 CNNIC 一文被 DDOS 服务器下线，以下是存档：

https://docs.google.com/View?id=d5j3s7p_7f9r489fg  

  

  





  

rationalcrow



拆呐拆呐不拆怎么成china





15楼 大 中 小 发表于 2010-2-2 10:23  只看该作者



发现有2条“Entrust.net Secure Server Certification Authority”，都处理掉  

  

  





  

rationalcrow



拆呐拆呐不拆怎么成china





16楼 大 中 小 发表于 2010-2-2 11:15  只看该作者



警告：CNNIC，我不信任你！——从“受信任的根证书”里赶走CNNIC（Win7/Vista/Xp）  

  

本文转自：http://felixcat.net/2010/01/throw-out-cnnic/#comment-970  

  

注意：做到第9步时就不用关闭根证书自动更新了。  

  

在Twitter上惊闻“微软把CNNIC列为根证书发布者”，赶紧Google一把，发现 Mozilla同样也已经在3.6版的Firefox里这么做了。  

出于对CNNIC深深的不信任，我决定将CNNIC ROOT从“受信任”的列表里赶出去。  

因为IE/Chrome采用微软的CA目录，而微软现在暂未将CNNIC加入，因此需要先从Firefox中导出这几个证书，再添加到Windows的

“不信任”列表(更新：现在可以直接从Windows里导入再导入了，操作类似)，以防范于未然。下面便是具体的步骤了（包括IE/Chrome

/Firefox）：  

  

1、如果没有安装Firefox浏览器的3.6最新版，或者在下面的操作中没有找到相应的证书，可以从这里下载这三个证书，然后跳到第5

步：CNNICROOT.crt CNNICSSL.crt Entrust.netSecureServerCertificationAuthority.crt  

  

2、打开Firefox浏览器，工具(Tools)->选项(Options)->高级(Advanced)->加密

(Encryption)->查看证书(View Certificates)  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-26-58.png)  

3、在证书机构(Authorites)标签页中找到”CNNIC“组的”CNNIC ROOT“项，按导出(Export)（备份到本地），然后删除

(Delete)。（RT JimmyXu:在Firefox里对自带根证书执行“删除”操作就相当于是禁用其所有目的，并不会将其删除。）  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-29-47.png)  

4、在”Entrust.net“组中找到”Entrust.net Secure Server Certification

Authority“(序列号37:4A:D2:43的)和”CNNIC

SSL“证书，同样导出并删除。（注：Entrust.net这个也是验证CNNIC所用的证书）  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-31-46.png)  

5、打开开始菜单->运行（或者直接按Win-R）  

  

6、输入certmgr.msc，打开Windows 的证书管理器。  

  

7、展开”不受信任的证书(Untrusted Certificates)“，右键单击其下”证书(Certificates)“项，在”所有任务(All

Tasks)“子菜单下单击”导入(Import)…“  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-33-09.png)  

8、分别找到刚才保存的三个证书，依次导入(Next->Browse…(找到相应文件)->Next->Next->Finish)。  

  

9、将导入的证书复制(Ctrl-C)，然后粘贴(Ctrl-V)到受信任的证书颁发者(Trusted Root Certification

Authorities)中，然后在这个窗口中分别右键单击粘贴过来的3个证书，选择“属性(Properties)”，然后单击“停用这个证书的所有目的(Disable

all purposes for this certificate)”。  

[attach]2270020[/attach]  

（感谢 Jimmy Xu 供图）  

  

想检验操作是否成功？在浏览器里访问 https://www.enum.cn/ ，如果提示证书被拒绝，就证明操作成功了！  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-34-19.png)  

  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-35-16.png)  

  

![](http://felixcat.net/wp-content/uploads/2010/01/2010-01-27-17-36-22.png)  

  

不需要关闭自动更新  

  

参考资料：http://www.networkworld.com/community/node/17703  

  

  





  

萧易寒





17楼 大 中 小 发表于 2010-2-2 13:38  只看该作者



顶作者，自己删除没有用的，还有99%的用户没有删除  

  

  





  

reborn



嗷嗷嗷





18楼 大 中 小 发表于 2010-2-2 15:16  只看该作者



这个要学习  

  

  





  

Phillip



路边社特邀围观群众





19楼 大 中 小 发表于 2010-2-2 18:06  只看该作者



回复 6楼 萧易寒 的话题



只要有人给相关机构写信, 让他们在新版本浏览器操作系统里去掉CNNIC的信任就行了  

  

  





  

Zenu



资深潜水员





20楼 大 中 小 发表于 2010-2-2 18:15  只看该作者



感谢!已经彻底禁用了CNNIC这个流氓...希望Entrust尽快吊销对流氓之信任...  

分享一个IE用户彻杀CNNIC的方法  

http://hi.baidu.com/litiejun/blo ... 9a3f3e32fa1c73.html  

  

  





  

pillarchang





21楼 大 中 小 发表于 2010-2-2 20:18  只看该作者



mark  

  

  





  

胺氰聚三郎



怪组员





22楼 大 中 小 发表于 2010-2-2 21:29  只看该作者



* 菜单栏：工具/编辑->首选项->高级->加密->查看证书->证书机构(Authorites)  

    * 这是一个很长的列表，按照字母顺序，你应该能找到一个叫着 "CNNIC ROOT" 的记录，就是这个东西，告诉 Firefox，我们不信任它！  

===================  

不理解  

我就没找到  

是电脑问题吗  

  

  





  

胺氰聚三郎



怪组员





23楼 大 中 小 发表于 2010-2-2 21:33  只看该作者



是点  

工具——internet选项——内容——证书  

那里找吗  

  

  





  

winddeer



天朝有风险，投胎须谨慎





24楼 大 中 小 发表于 2010-2-2 21:50  只看该作者



开始——运行——certmgr.msc，然后，受信任的证书颁发机构，然后，cnnic root双击，然后，详细信息，然后 编辑属性，

最后下狠手，停用这个证书的所有目的！  

  

  





  

02304H



10001100000100B





25楼 大 中 小 发表于 2010-2-2 22:21  只看该作者



回复 11楼 胺氰聚三郎 的话题



你用的ie吧，那文里说的是firefox  

  

  





  

unloop



不特别的一人





26楼 大 中 小 发表于 2010-2-3 06:07  只看该作者



删除Entrust 的CA后，这个网站的加密访问受到影响 http://www.worldcommunitygrid.org/  

是无奈的连带伤害么～～  

  

  





  

过客





27楼 大 中 小 发表于 2010-2-3 10:33  只看该作者



按给出的方法做了，杀不死这个流氓，当时清除干净一重启又出现了！－－IE浏览器  

  

  





  

investigate



围观圣手





28楼 大 中 小 发表于 2010-2-3 15:12  只看该作者



找不到。。。。。  

  

  





  

精彩在wall





29楼 大 中 小 发表于 2010-2-3 15:46  只看该作者



我试了好几次，按照文中的步骤，但是一旦访问那2个验证网站，CNNIC root证书又会出现在信任证书列表里，烦不胜烦。  

  

  





  

鼠标土豆



古典自由主义土豆





30楼 大 中 小 发表于 2010-2-3 16:47  只看该作者



请教高手：刚才把CNNIC的证书全开除了，结果163的邮箱就不能用SSL安全登录了，那么火狐浏览器会自动加密吗？  

  

  





  

张书记



http://twitter.com/SecretaryZhang





31楼 大 中 小 发表于 2010-2-4 12:29  只看该作者



RT @WCM: 手机号被 CNNIC 翻出来了，聊了一个小时，对方很客气。如果我要去喝茶，已做好准备。  

  

  





  

OpenBL





32楼 大 中 小 发表于 2010-2-6 02:50  只看该作者



回复 19楼 Phillip 的话题



微软会鸟你屁民，火狐都难  

  

  





  

wkh





33楼 大 中 小 发表于 2010-2-6 13:13  只看该作者



学习了  

  

  





  

paradox





34楼 大 中 小 发表于 2010-2-6 22:50  只看该作者



求教，chrome怎么改呢？  

  

  





  





















    







    













