<h2>多线程电商(淘宝，京东)图片爬虫</h2>

<h3>用途</h3>
用于爬取淘宝（包含阿里巴巴，淘宝，天猫），京东宝贝页面图片,包括页面中的宝贝详情图片，宝贝属性图片及介绍视频

<h3>文件基本说明</h3>
qt_zh_CN.qm与widgets_zh_CN.qm为pyqt5界面汉化文件<br>
source.py为背景图片等图片内容<br>
verify.py 项目开始出于商业，用于设置加密收费，现在弃用<br>
Ali.py JD.py分别为爬取淘宝和京东宝贝的爬虫代码<br>


<h3>运行条件</h3>
运行环境：python 3.7
必备包：PyQt5,re,requests,urllib,bs4,demjson，pyinstall（将程序打包成exe）

<h3>运行</h3>
直接运行run.py文件即可
一次性可以粘贴多个宝贝链接到链接框（用换行隔开），最多一次性启动3线程同时爬取

![Alt text](https://github.com/enhey/ImageCrawl/blob/master/MarkdwonImg/download_url.png)<br><br>

![Alt text](MarkdwonImg/downloading.png)<br><br>

![Alt text](MarkdwonImg/result.png)

<h3>程序使用<h3/>
<h5>使用前必须在设置中选择好图片保存路径与爬取的具体项目<br>
  
![Alt text](MarkdwonImg/setting.png)

<h3>程序打包说明<h3/>
<h5>程序可以直接打包成exe程序在windows中运行<br>
打包方法：在terminal运行以下命令<br>
pyinstaller -F -w -i img.ico run.py<br>
-F 指只生成一个exe文件，不生成其他dll文件<br>
-w 不弹出命令行窗口<br>
-i 设定程序图标 ，其后面的ico文件就是程序图标（根据自己想要的图标进行修改）<br>
run.py 就是要打包的程序<br>
-c 生成的exe文件打开方式为控制台打开。<br> 
  
  
![Alt text](MarkdwonImg/package_command.png)<br><br>


打包成功后显示：<br>
![Alt text](MarkdwonImg/package_success.png)<br><br>


最终可以在dist目录下看到打包的结果
![Alt text](MarkdwonImg/software.png)<br><br>
如果电脑安装360杀毒，运行可能会被拦截，如果程序运行不成功，检查下是否被360拦截
