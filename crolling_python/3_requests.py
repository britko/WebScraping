import requests
# res = requests.get("http://nadocoding.tistory.com")
res = requests.get("http://google.com")
res.raise_for_status()
# print("응답코드: ", res.status_code)    # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

# with open(r"C:\Users\pc\Desktop\고영국\개발\웹\WebScraping_basic\크롤링 데이터\HTML\nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)

with open(r"C:\Users\pc\Desktop\고영국\개발\웹\WebScraping_basic\크롤링 데이터\HTML\google.html", "w", encoding="utf8") as f:
    f.write(res.text)