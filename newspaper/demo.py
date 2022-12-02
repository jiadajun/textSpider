from newspaper import Article

url = 'https://www.nbweikang.com/index.html'
article = Article(url, language='zh')
article.download()
# print('html:', article.html)

article.parse() # 解析网页

print('题目：',article.title)       # 新闻题目
print('正文：\n',article.text)      # 正文内容
print(article.authors)     # 新闻作者
print(article.keywords)    # 新闻关键词
print(article.summary)     # 新闻摘要

# print('authors:', article.authors)
# print('title:', article.title)
# print('date:', article.publish_date)
# print('text:', article.text)
# print('text_len:', len(article.text))
# print('top image:', article.top_image)
# print('images:', article.images)
# print('movies:', article.movies)


# article.nlp()
# print('keywords:', article.keywords)
# print('summary:', article.summary)
