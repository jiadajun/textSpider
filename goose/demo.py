# -*- coding: utf-8 -*-
from goose3 import Goose
from goose3.text import StopWordsChinese


# 初始化，设置中文分词
g = Goose({'stopwords_class': StopWordsChinese})
g = Goose({'browser_user_agent': 'Version/5.1.2 Safari/534.52.7'})
url = "https://www.nbweikang.com/index.html"
#提取，可以传入 url 或者 html 文本：
article = g.extract(url=url)
#article = g.extract(raw_html=html)
print(article.title)# 标题
print(article.cleaned_text)# 显示正文
print(article.top_image)# 显示正文
