from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('V:/Python36/chromedriver.exe')


driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 URL로 이동하기
driver.find_element_by_name('id').send_keys('chsst') # 값 입력
driver.find_element_by_name('pw').send_keys('dufrhd87*&')
driver.find_element_by_xpath(
    '//*[@id="frmNIDLogin"]/fieldset/input'
).click() # 버튼클릭하기
driver.get('https://order.pay.naver.com/home') # Naver 페이 들어가기
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())