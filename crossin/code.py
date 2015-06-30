# -*- coding:utf-8 -*-
import web  #导入web.py模块



urls = (
    '/', 'index' 
)
#指定网站 url 的匹配规则，左边是正则表达式，右边是对应处理函数的名称

movies = [
	{
		'title':'Forrest Gump',
		'year':'1994',
	},
	{
		'title':'Titanic',
		'year':'1997',
	},
]

class index:
	def GET(self):
		page = ''
   		for m in movies:
       		page += '%s (%d)\n' % (m['title'], m['year'])
   return "呵呵"


if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()
