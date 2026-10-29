import time
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag

# 最初にアクセスするURL
start_url = 'https://www.musashino-u.ac.jp/'
# 同一ドメインか判定するためのドメイン名
domain = urlparse(start_url).netloc

# 1回アクセスするごとに待つ秒数
sleep_sec = 0.2
# 取得するページ数の上限（テスト用。本番はNone）
max_pages = None

# URLとタイトルを入れる辞書
pages = {}

# これから行くURLのリスト
queue = [start_url]
# もう見たURL（同じページに2回行かないように）
seen = {start_url}

# 行くURLが残っていて、上限に達してない間くり返す
while queue and (max_pages is None or len(pages) < max_pages):

    # リストの先頭から1個取り出す
    url = queue.pop(0)

    # アクセスする前に必ずsleep
    time.sleep(sleep_sec)

    # リクエストを送って、レスポンスをresに入れる（ex4、ex5）
    # エラーで止まらないようにtry/exceptを使う
    try:
        res = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"エラー：{url} {e}")
        continue

    # HTMLじゃないもの（PDFとか）は飛ばす
    if 'text/html' not in res.headers.get('Content-Type', ''):
        continue

    # HTMLのソースコードをBeautifulSoupオブジェクトに変換する処理（ex4、ex5）
    html_soup = BeautifulSoup(res.content, 'html.parser')

    # <title>の文字列を取る（ex4の.string）
    # titleがないとNoneになるため、その時は空文字にしておく
    if html_soup.title is not None and html_soup.title.string is not None:
        title = html_soup.title.string.strip()
    else:
        title = ''

    # 辞書にURLとタイトルを入れる
    pages[url] = title
    print(f"{len(pages)} {url} {title}")

    # リンクを全て取得する（ex5の5-2）
    a_list = html_soup.find_all('a', href=True)

    # aタグを1個ずつ取り出して、リンク先を調べる
    for a in a_list:
        # 相対パスをフルのURLにする
        link = urljoin(url, a['href'])
        # #から後ろを消す
        link, _ = urldefrag(link)

        # 同じドメインで、まだ見てないURLだけリストに追加
        if urlparse(link).netloc == domain and link not in seen:
            seen.add(link)
            queue.append(link)

print(f"完了：{len(pages)}ページ取得しました")

# 辞書をもとにCSVに保存する
# utf-8-sigにすると、Excelで開いても文字化けしにくい
with open('sitemap.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    # 1行目は見出し
    writer.writerow(['url', 'title'])
    # 辞書から1組ずつ取り出して書き込む
    for url, title in pages.items():
        writer.writerow([url, title])