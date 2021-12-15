import requests
import re
from bs4 import BeautifulSoup


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36"}
for i in range(1, 6):
    print("페이지: ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        #광고 제품 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("  <광고 상품을 제외합니다>")
            continue    # 아래 코드를 실행하지 않고 건너뜀

        name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명
        # 애플 제품 제외
        if "Apple" in name:
            # print("  <Apple 상품을 제외합니다>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()   # 가격


        rating = item.find("em", attrs={"class":"rating"})   # 평점
        # 평점 없는 상품 제외
        if rating:
            rating = rating.get_text()
        else:
            # print("  <평점 없는 상품을 제외합니다>")
            continue

        rating_cnt = item.find("span", attrs={"class":"rating-total-count"})   # 리뷰 수
        if rating_cnt:
            rating_cnt = rating_cnt.get_text()[1:-1]    # ()안의 평점 수만 추출
        else:
            # print("  <리뷰 없는 상품을 제외합니다>")   # 평점이 없는 상품은 리뷰도 없기 때문에 필요없는 코드이긴 함
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        
        # 평점이 4.5이상이고 리뷰 개수가 100개 이상인 상품만 조회
        if float(rating) >= 4.5 and int(rating_cnt) >= 100:
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rating}점 ({rating_cnt}개)")
            print("바로가기: {}".format("https://www.coupang.com" + link))
            print("-"*100)  # 줄긋기