# User-Agent를 헤더에 넣어줌으로써 사용자 정보를 알려주고 페이지의 자세한 정보를 받아올 수 있다. 

import requests
url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open(r"C:\Users\pc\Desktop\고영국\개발\웹\WebScraping_basic\크롤링 데이터\HTML\google_headers.html", "w", encoding="utf8") as f:
    f.write(res.text)