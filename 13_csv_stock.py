import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

#  newline="": 공백 행을 삭제
filename = r"C:\Users\pc\Desktop\고영국\개발\웹\WebScraping_basic\크롤링 데이터\13_시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# 탭으로 구분해서 리스트 형식으로 저장 ["N", "종목명", "현재가", ...]
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# 각 열마다 제목 삽입
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1:   # 의미 없는 데이터 skip
            continue
        
        # strip(): ???????????
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)