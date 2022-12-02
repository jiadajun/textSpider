Goose 是一个 文章内容提取器 ，可以从任意资讯文章类的网页中提取 文章主体 ，并提取 标题、标签、摘要、图片、视频 等信息，且 支持中文 网页。它最初是由 http://Gravity.com 用 Java 编写的。python-goose 是用 Python 重写的版本。

有了这个库，你从网上爬下来的网页可以直接获取正文内容，无需再用 bs4 或正则表达式一个个去处理文本。

安装 ：

pip install goose3

除了标题 title 和正文 cleaned_text 外，还可以获取一些额外的信息，比如：
meta_description ：摘要
meta_keywords ：关键词
tags ：标签
top_image ：主要图片
infos ：包含所有信息的 dict
raw_html ：原始 HTML 文本


如有有些网站限制了程序抓取，也可以根据需要添加 user-agent 信息：

g = Goose({'browser_user_agent': 'Version/5.1.2 Safari/534.52.7'})