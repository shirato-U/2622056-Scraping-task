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

# ----- 指定したタグで要素を検索する ------- #

# 5-1. 指定したタグが最初に使われている要素のうち、一番最初に出てくる要素をTagオブジェクトとして取得する
h2 = html_soup.find('h2')
print(type(h2))
print(h2)

# 5-2. 指定したタグが使われている要素を全て取得する

# h2 タグの場合
h2_all = html_soup.find_all('h2')

for h2 in h2_all:
    
    #print(type(h2))
    if h2.span is not None:
        print(h2.span.string)

# aタグの場合
a_list = html_soup.find_all('a',limit=5)

for a in a_list:
    print(a.string)


# 5-3. 複数のタグで検索
tag_a_span_list = html_soup.find_all(['a','span'],limit=5)

for tag in tag_a_span_list:
    print(tag)

# 5-4. 任意の属性で検索
# hrefが'/'になっている部分を検索したい場合
tag_href_list = html_soup.find_all(attrs={"href:'/'"})
for tag in tag_href_list:
    print(tag)

# 5-5. idやclass名で検索
print(html_soup.find_all(id='footer'))
print(html_soup.find_all(class_='l-header'))