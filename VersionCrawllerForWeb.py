import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

"""
Codebeamer http://10.185.7.63:8080/cb/rest/version (Basic Auth + Rest)
JIRA http://collab.lge.com/support/secure/AboutPage.jspa (Basic Auth + web parsing)
Coverity http://cim.lge.com:5469/about.htm(Basic Auth + web parsing)
"""

codebeamerVersionUrl = 'http://10.185.7.63:8080/cb/rest/version'
jiraVersionUrl = 'http://collab.lge.com/support/secure/AboutPage.jspa'
coverityVersionUrl = 'http://cim.lge.com:5469/about.htm'

loginId = '-'
loginPw = '-'
loginPw2 = '-'


def getCodebeamerVersion():
    response = requests.get(codebeamerVersionUrl, auth=HTTPBasicAuth(loginId, loginPw))
    if response.status_code == 401:
        response = requests.get(codebeamerVersionUrl, auth=HTTPBasicAuth(loginId, loginPw2))
    return 'Codebeamer version : ' + str(response.text)

def getJiraVersion():
    result = ""
    response = requests.get(jiraVersionUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    found = soup.find(id='content')
    versionList = found.find_all("h3")
    return versionList[0].get_text() + "\n" + versionList[1].get_text()

def getCoverityVersion():
    response = requests.get(coverityVersionUrl, auth=HTTPBasicAuth(loginId, loginPw))
    if response.status_code == 401:
        response = requests.get(coverityVersionUrl, auth=HTTPBasicAuth(loginId, loginPw2))

    soup = BeautifulSoup(response.text,'lxml')
    return 'Coverity version:' + str(soup.find_all("li")[1]).split('</b>')[1].split('</li>')[0]

print(getCoverityVersion())
