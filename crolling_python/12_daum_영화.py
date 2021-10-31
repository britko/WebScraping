import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    # enumerate: ??????????????
    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]

        # startswith: ???????????
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # with open: ??????????????
        with open(r"C:\Users\pc\Desktop\고영국\개발\웹\WebScraping_basic\크롤링 데이터\12_영화 사진\movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:    # 상위 5개 이미지까지만 다운로드
            break