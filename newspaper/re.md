作者从requests库的简洁与强大得到灵感，使用python开发的可用于提取文章内容的程序

Newspaper可以用来提取新闻、文章和内容分析。使用多线程，支持10多种语言等


给Article传入两个参数，一个为url，一个为支持的语言（这里对于中文语言应都添加为‘zh’，否则大部分网站都抓取不了），生成一个article对象后，调用对象的download()方法，download在内部调用network的get_html_2XX_only方法，调用requests从而得到网页源码；parse()中包含文档清理以及输出格式化，对标签进行清理，可以得到正文的内容


安装

    pip install newspaper3k （Python3以上的版本）

    pip install newspaper （Python2版本）
