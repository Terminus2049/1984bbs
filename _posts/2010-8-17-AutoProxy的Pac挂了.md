---
layout: default

date: 2010-8-17

title: AutoProxy的Pac挂了

categories: 国家局域网研究所

---





# AutoProxy的Pac挂了



Shuangyan



爱IT，更爱Animations & Cosmics . 爱RPG & RTS，更爱暴雪出品。 爱《Animal Farm》，更爱 《Canon in D

major》. 爱《1812序曲》，更爱《1984》. 爱Nonviolence Revolution，更爱Social Democracy.

我是ShuangYan，我与你分享 ...





1楼 大 中 小 发表于 2010-8-17 14:18  只看该作者



AutoProxy的Pac挂了



今天用FeedDemon和Seesmic Destop 2的时候发现无法登陆Google

Reader、Twiiter和Facebook,查了一下才知道https://autoproxy2pac.appspot.com/挂掉了，IE里面的Pac无法解析了，请问有什么办法能解决吗？Firefox里的导出似乎只能导出自定义规则。  

  

  







  

---

[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)

---



Phillip



路边社特邀围观群众





2楼 大 中 小 发表于 2010-8-17 14:56  只看该作者



回复 1楼 Shuangyan 的话题



这里有  

https://1984bbs.com/viewthread.php?tid=55432&extra=page%3D1  

  

其实就是先翻墙上到https://autoproxy2pac.appspot.com/, 把对应的pac文件下载到本地然后浏览器使用.

这样就要经常上去下载最新列表.  

  

  





  

Shuangyan



爱IT，更爱Animations & Cosmics . 爱RPG & RTS，更爱暴雪出品。 爱《Animal Farm》，更爱 《Canon in D

major》. 爱《1812序曲》，更爱《1984》. 爱Nonviolence Revolution，更爱Social Democracy.

我是ShuangYan，我与你分享 ...





3楼 大 中 小 发表于 2010-8-17 15:02  只看该作者



回复 2楼 Phillip 的话题



感谢回复，不过可能是我没解释清楚，这次https://autoproxy2pac.appspot.com/挂掉应该不是GFW所致，估计是Google

Appspot的服务器出了故障或其他原因，因为不管翻墙不翻墙，网页都出现这么一行字：  

  

“Over Quota  

This Google App Engine application is temporarily over its serving quota.

Please try again later. ”  

  

我目前找到一个折中的办法就是让IE使用全局代理，不过好在Firefox平时订阅的时候都是自动下载的，所以这次Firefox倒不是很受影响。但是IE和Google

Chrome如果没有下载本地PAC文件的话就没办法了，只能使用全局代理了。  

  

  







  

Shuangyan



爱IT，更爱Animations & Cosmics . 爱RPG & RTS，更爱暴雪出品。 爱《Animal Farm》，更爱 《Canon in D

major》. 爱《1812序曲》，更爱《1984》. 爱Nonviolence Revolution，更爱Social Democracy.

我是ShuangYan，我与你分享 ...





4楼 大 中 小 发表于 2010-8-17 15:49  只看该作者



终于找到了一个根本的解决途径：  

有编程达人制作了个脚本能把GFWList自动打包为PAC文件，经下载验证完全可用，解决了https://autoproxy2pac.appspot.com/无法访问的问题  

  

原文在这里：http://bbs.kafan.cn/thread-685803-1-1.html  

  

我把脚本制作包上传到空间里方便没有卡饭号的下载：http://u.115.com/file/f65f1d02bd  

  

PS:PAC文件制作完成后请打开并修改当中的端口号，因为它默认打包是8000端口。  

  

  







  

Phillip



路边社特邀围观群众





5楼 大 中 小 发表于 2010-8-17 16:34  只看该作者



回复 4楼 Shuangyan 的话题



gfwlist不是有base64加密吗, 这个导出是已经解密的了?  

  

  





  

Shuangyan



爱IT，更爱Animations & Cosmics . 爱RPG & RTS，更爱暴雪出品。 爱《Animal Farm》，更爱 《Canon in D

major》. 爱《1812序曲》，更爱《1984》. 爱Nonviolence Revolution，更爱Social Democracy.

我是ShuangYan，我与你分享 ...





6楼 大 中 小 发表于 2010-8-17 18:09  只看该作者



回复 5楼 Phillip 的话题



应该是 这个脚本会自动下载GFWLIST，然后自动转成PAC，然后保存到D盘下面，然后在IE里PAC地址填上就和原来一样了  

  

  







  

Phillip



路边社特邀围观群众





7楼 大 中 小 发表于 2010-8-17 23:29  只看该作者



既然PAC可以打开修改端口设置, 那就一定是不加密的.  

/autoproxy2pac生成的PAC是加密的,  

IE CHROME都支持脚本BASE64解码所以可以用, Opera就必须使用解密好的脚本.  

  

  





  

Shuangyan



爱IT，更爱Animations & Cosmics . 爱RPG & RTS，更爱暴雪出品。 爱《Animal Farm》，更爱 《Canon in D

major》. 爱《1812序曲》，更爱《1984》. 爱Nonviolence Revolution，更爱Social Democracy.

我是ShuangYan，我与你分享 ...





8楼 大 中 小 发表于 2010-8-18 00:15  只看该作者



回复 7楼 Phillip 的话题



这个权当做紧急方案吧，万一哪天Autoprxoy2Pac那个网站有挂了，这个就能作补充，晚上我看的时候，网站已经修复了。  

  

  







  

Phillip



路边社特邀围观群众





9楼 大 中 小 发表于 2010-8-18 01:18  只看该作者



回复 8楼 Shuangyan 的话题



好像appspot上的应用每月都有流量限制的. 比如GAE翻墙就是这样. 所以每月超流量挂掉是正常的.  

  

  





  





















    







    













