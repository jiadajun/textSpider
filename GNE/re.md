GNE(GeneralNewsExtractor)是一个通用新闻网站正文抽取模块，输入一篇新闻网页的 HTML， 输出正文内容、标题、作者、发布时间、正文中的图片地址和正文所在的标签源代码。GNE 在提取今日头条、网易新闻、游民星空、 观察者网、凤凰网、腾讯新闻、ReadHub、新浪新闻等数百个中文新闻网站上效果非常出色，几乎能够达到 100%的准确率。


如何安装 GNE
直接使用 pip 安装 GNE ：

pip install gne
1
如果访问 pypi 官方源太慢，你也可以使用网易源：

pip install gne -i https://pypi.tuna.tsinghua.edu.cn/simple


