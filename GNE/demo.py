from gne import GeneralNewsExtractor
import requests
extractor = GeneralNewsExtractor()


def parse_info(html):
    result = extractor.extract(html, with_body_html=True)
    print(result)


def run():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    resp = requests.get('https://www.nbweikang.com/index.html', headers=headers)
    resp.encoding = 'utf8'
    # print(resp.text)
    parse_info(resp.text)


run()

