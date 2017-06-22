import requests
from requests.auth import HTTPBasicAuth


def createContent(pageTitle, content):
    baseUrl = 'http://collab.lge.com/main/rest/api/content/'
    childPageId = '623018243'
    #pageTitle = pageTitle
    #pageTitle = '20170622'
    projectKey = 'VWMIBOI'
    loginId = 'myid'
    loginPw = 'mypasswd'
    #content = '<p>This is a new page</p>'

    requestBodyAsJson = {
        "type": "page",
        "title": pageTitle,
        "ancestors": [
            {
                "type": "page",
                "id": childPageId
            }
        ],
        "space": {
            "key": projectKey
        },
        "body": {
            "storage": {
                "value": content,
                "representation": "storage"
            }
        }
    }

    response = requests.post(baseUrl, json=requestBodyAsJson, auth=HTTPBasicAuth(loginId, loginPw))
    print(response.text)
    print(response.json)
    print(response.status_code)
    return response.status_code
