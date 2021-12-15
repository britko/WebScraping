from selenium import webdriver  # selenium 프레임 워크에서 webdriver 가져오기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()    # "./chromedriver.ex
browser.maximize_window()   # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)    # url로 이동

# 가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번 달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번 달

# 다음 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음 달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# 이번 달 27일, 다음 달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번 달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# 도착 선택
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/a[2]").click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/div[2]/table[1]/tbody/tr[1]/td[1]/a").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# WebDriverWait를 통해서 브라우저를 최대 10초 동안 기다린다. 10초가 넘으면 에러 발생
# 10초 동안(until) 어떤 조건(EC)의 엘리멘트가 위치할 때까지(elements_located) 기다린다. 그 조건은 XPATH 값에 해당하는(BY.XPATH) xpath의 실행
# xpath 외에도 id, class_name, link_text 등 사용 가능
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 대 동작 수행
    print(elem.text)   # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]").click()
# print(elem.text)