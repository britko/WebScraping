from selenium import webdriver

options = webdriver.ChromeOptions()
# headless 크롬: 크롬을 띄우지 않고 백그라운드에서 작업을 진행함(빠른 성능, 생산성 증가)
options.headless = True
options.add_argument("window-size=1920x1080")
# headless는 거부되는 서버가 있기 때문에 실제 User-Agent값을 넣어주어야 한다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# User-Agent 값
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()