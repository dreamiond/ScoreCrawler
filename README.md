工作说明:

	爬取新浪高考的分数线数据，存储在MongoDB内，本工作为其他项目的先导工作。
	
	数据包括院校名称、考生所在地、考生类别、批次、年份、最高分、平均分。

环境说明：

	操作系统：windows10
	
	语言：Python3.6.5
	
	爬虫框架：Scrapy
	
	数据库：MongoDB 4.0.10 Community
	
	插件：pymongo
	
目录结构：

	/spiders			# 存储全部Spider程序的目录
		-_init_.py		# Scrapy自动生成的类似readme的文档
		-sinaSpider.py 	# Spider主程序，负责指定用于下载的初始URL、跟进网页中的链接、分析页面中的内容、提取生成item
	/univFile			# 存储json文件的目录。json存储方式用于调试时使用。
	-init_.py			# Scrapy自动生成的空文档
	-items.py			# 定义需从网页中提取的条目
	-main.py			# 程序入口。也可以不用此程序转而使用命令行，效果相同。
	-middlewares.py		# 中间件。Scrapy自动生成，未作改动。
	-pipeline.py		# 负责将数据存储到数据库中。
	-settings.py		# 整个项目的配置文件。
	
其他说明：

	本项目中settings.py中ROBOTSTXT_OBEY = True，也就是说本爬虫遵循了新浪高考的robots协议。在此感谢新浪高考。
	
	项目详细开发流程请移步我的博客：https://dreamiond.github.io/2019/06/14/ScoreCrawler/
	
presented by:

	王健鑫@dreamiond
	
	2019/6/14

