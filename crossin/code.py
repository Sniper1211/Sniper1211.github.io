# -*- coding:utf-8 -*-
import web  #导入web.py模块

urls = (
    '/', 'index' 
)
#指定网站 url 的匹配规则，左边是正则表达式，右边是对应处理函数的名称

class index:
    def GET(self):
        return "testing"
# ⬆️处理请求的函数 index。
# GET 和 POST 是 HTTP 的两种请求方式
# 一般来说，GET 用于请求网页，而 POST 多用于提交表单
# 举个不严谨的栗子：
# 当你在浏览器地址栏中输入一个地址并按下回车，就是发送了一个 GET 请求；
# 而当你在打开的页面中输入用户名和密码，点击登录按钮，则是发送了一个 POST 请求。
# 这里的 GET 函数描述了对于一个 GET 请求的处理方式：直接返回一个字符串。

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
# 当这个代码文件被执行时
# 我们将创建一个 application
# 它会按照我们定义的 url 规则进行对应的处理
# 并在后台一直运行，独自等待请求的到来。
