import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

# 셀레니움 작동하기전 Chrome DevTools Protocol 실행해서 브라우저를 실행 시켜놓고 해당 브라우저로 크롤링
# 우분투인경우 /usr/bin/google-chrome --no-sandbox --headless --disable-gpu --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
# 맥인경우 /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # 자동종료 방지
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("--incognito")

# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(time_to_wait=5)
wait = WebDriverWait(driver, 10)

# 로그인페이지 이동
url = "https://www.hometax.go.kr" 
driver.get(url)
time.sleep(1)
driver.find_element(by=By.ID, value='textbox81212912').click()

# 로그인 폼 선택을 위한 프레임 전환
driver.switch_to.frame('txppIframe')
time.sleep(1)

# 로그인
MYID = 'YOUR_ID1'
MYPW = 'YOUR_PW1'

driver.find_element(by=By.ID, value='anchor15').click()
el_id = driver.find_element(by=By.ID, value='iptUserId')
el_id.send_keys(MYID)
el_pw = driver.find_element(by=By.ID, value='iptUserPw')
el_pw.send_keys(MYPW)
el_pw.send_keys(Keys.RETURN)


# 마이홈텍스 페이지 이동
url = 'https://www.hometax.go.kr/websquare/websquare.wq?w2xPath=/ui/pp/index_pp.xml'
time.sleep(1)
driver.find_element(By.ID, value='group120').click()

# confirm 처리
alert = wait.until(expected_conditions.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

html = driver.page_source
print(html)

with open("hometax.html", "w") as f:
    f.write(html)

# driver.quit()