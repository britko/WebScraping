import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=736989&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 평점 구하기
total_rate = 0

cartoons = soup.find_all("div", attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)

print("평균 점수: ", total_rate / len(cartoons))