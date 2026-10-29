import requests

url = 'https://ja.wikipedia.org/w/index.php'
# 辞書形式でURLパラメータを指定
param = {
    'title': '武蔵野大学',
    'oldid': 100769128
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

res = requests.get(url,params=param,headers=header)

print(f"ステータスコード：{res.status_code}")
print(f"ステータスメッセージ：{res.reason}")

print(f"レスポンスボディ：{res.text}")