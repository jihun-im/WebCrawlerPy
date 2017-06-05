import sys
import requests
from bs4 import BeautifulSoup  # url = 'naver.com/' + str(page)

# startUrl = 'http://collab.lge.com/main/display/VWMIBOI/D202_Configuration+management/'
startUrl = 'http://collab.lge.com/main/display/VWMIBOI/D202_Configuration+management'
loginUrl = 'http://collab.lge.com/main/login.action/'
baseUrl = 'http://collab.lge.com/'
historyUrl = 'http://collab.lge.com/main/pages/viewpreviousversions.action?pageId='
showChildAppender = '?showChildren=true'

pageUrlList = []
pageTitleList = []
pageVersionList = []

if len(sys.argv) != 4:
    print("usage: thisProgram.py \"your_ep_id\" \"your_ep_password\" \"collabParentPage\"")
    exit(-1)

logInId = sys.argv[1]
logInPassword = sys.argv[2]
startUrl = sys.argv[3]

loginPayload = {
    'os_username': logInId,
    'os_password': logInPassword
}

# 로그인 세션 유지
with requests.Session() as session:
    # 로그인
    loginPage = session.post(loginUrl, data=loginPayload)


    # print the html returned or something more intelligent to see if it's a successful login page.
    # print(loginPage.text)

    # 각 페이지마다 수행할 visit 함수
    def visit(whereToVisit):
        # 전체 페이지 가져오기
        # An authorised request.
        targetPage = session.get(whereToVisit)
        # print(targetPage.text)

        # lxml형식으로 파싱 + 보기편하게
        targetPageText = targetPage.text
        targetSoup = BeautifulSoup(targetPageText, 'lxml')
        # print(soup)

        # Title과 현재Version을 List에 저장
        for link in targetSoup.select('meta[name="ajs-page-title"]'):
            pageTItle = link.get('content')
            pageTitleList.append(link.get('content'))
            # print(link.get('content'))  # 제목

        # page-id로 히스토리에 접근해서 Version 가져오기
        for link in targetSoup.select('meta[name="ajs-page-id"]'):
            # page-id가져오기
            pageId = link.get('content')
            historyPage = session.get(historyUrl + pageId)
            historyPageText = historyPage.text
            historySoup = BeautifulSoup(historyPageText, 'lxml')
            # 맨 위에있는 버전만 필요함
            for link in historySoup.select('#page-history-container > tbody > tr > td > strong'):
                pageVersion = str(link).split('(')[1].split(')')[0]
                pageVersionList.append(pageVersion)
                # print(pageVersion) # Page Version
                break

        for link in targetSoup.select("#page-children > span > a"):
            # if "viewpage.action?pageId=" not in str(link.get('href')):
            #     childUrl = baseUrl + link.get('href') + showChildAppender
            # else:
            #     childUrl = baseUrl + link.get('href')
            childUrl = baseUrl + link.get('href')
            visit(childUrl)


    # 최초로 함수 호출
    visit(startUrl)
    # 로그인 세션 끝

# 처리가 다 끝나고 결과값 출력
for each in pageTitleList:
    print(each)
for each in pageVersionList:
    print(each)
