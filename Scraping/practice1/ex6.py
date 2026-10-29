import requests
from bs4 import BeautifulSoup

url = 'https://www.musashino-u.ac.jp'
res = requests.get(url)

print(f"ステータスコード：{res.status_code}")
print(f"ステータスメッセージ：{res.reason}")

# HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理
# html_soup = BeautifulSoup(res.text, 'html.parser')
html_soup = BeautifulSoup(res.content, 'html.parser')
print(f"html_soupの型：{type(html_soup)}")

# ------ CSSセレクタを使った検索 ------ #

# id指定（# + 検索id名）
# id名がfooter
print(html_soup.select('#footer'))

# class指定（. + 検索クラス名）
# class名がl-header
print(html_soup.select('.l-header'))

# HTML構造を指定して検索
print(html_soup.select("div > ul > li"))

print(html_soup.select("body > div.l-wrapper > main > div > div > section.l-top.l-top--features > article.p-introduction > div > div:nth-child(2) > div > p.p-introduction__detail.u-text"))
