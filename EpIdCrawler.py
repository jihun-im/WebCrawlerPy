import xlrd
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse

driver = webdriver.Chrome('V:/Python36/chromedriver.exe')

driver.implicitly_wait(3)  # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get(
    'https://sso.lge.com/eplogin.jsp?TYPE=33554433&REALMOID=06-3d8ecda9-7458-0006-0000-703f0000703f&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-gFbimnoUfHFCpX4o0x%2bq3yTv6aUBx1gEPllBt6wxA96gPMmAlqwJmeOLClUK7Z3g&TARGET=-SM-HTTP%3a%2f%2fsso%2elge%2ecom%2findex%2ejsp%3flang%3den')
driver.find_element_by_xpath('/html/body/form/div/div/div/p/input').send_keys('MyEpId')
driver.find_element_by_name('LDAPPASSWORD').is_selected()
driver.find_element_by_name('LDAPPASSWORD').send_keys('MyEpPW')
driver.find_element_by_name('OTPPASSWORD').send_keys('MyOTP_PWD')
driver.find_element_by_class_name('btn').click()

xlsxFile = 'C:\\Users\\user\\Desktop\\a.xlsx'
nameList = []
epIdList = []

workbook = xlrd.open_workbook(xlsxFile)
sheet = workbook.sheet_by_index(0)
nrows = sheet.nrows

for row in range(nrows):
    nameList.append(sheet.row_values(row)[0] + " " + sheet.row_values(row)[1])


# excel writing start
# outputWorkbook = xlwt.Workbook(encoding='utf-8')
# worksheet = outputWorkbook.get_sheet()


# name = '임지훈 개발2팀'
# driver.get('http://sso.lge.com/Portlets/seoul/newep3searchPortlet.jsp?tp=' + parse.quote(parse.quote(name)))
# html = driver.page_source
# #soup = BeautifulSoup(html, 'html.parser')
# soup = BeautifulSoup(html, 'lxml')
# print(soup.findAll("a", {"class": "sendMail"})[0].get_text().strip())


for eachName in nameList:
    driver.get('http://sso.lge.com/Portlets/seoul/newep3searchPortlet.jsp?tp=' + parse.quote(parse.quote(eachName)))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    try:
        epId = soup.findAll("a", {"class": "sendMail"})[0].get_text().strip()
        print(epId)
        epIdList.append(epId)
    except IndexError as e:
        print("결과없음")
        epIdList.append("결과없음")


print(epIdList)