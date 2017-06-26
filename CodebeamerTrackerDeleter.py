import sys
import requests
import xlrd
from requests.auth import HTTPBasicAuth

exceptionTrackerNameSubstring = '-'
projectKey = '-'
loginUrl = 'http://10.185.7.63:8080/cb/login.spr'
trackerListUrl = 'http://10.185.7.63:8080/cb/rest/project/' + projectKey + '/trackers'
trackerDeleteUrl = 'http://10.185.7.63:8080/cb/rest/'


loginId = '-'
loginPw = '-'


# if len(sys.argv) != 4:
#     print("usage: thisProgram \"your_id\" \"your_password\" \"excelFilePath\"")
#     exit(-1)
#
# logInId = sys.argv[1]
# logInPassword = sys.argv[2]
# excelFilePath = sys.argv[3]


def deleteFromList():
    # deletedCount = 0
    # for item in itemList:
    #     if (item.isdigit() == False):
    #         continue
    #     response = requests.delete(itemUri + item, auth=HTTPBasicAuth(loginId, loginPw))
    #     if (response.text == 'null'):
    #         deletedCount = deletedCount + 1
    #         print(item + " is deleted");
    #     else:
    #         print(item + " is not exist")
    # return deletedCount
    print("do nothing")


def getTrackerList(trackerListUrl):
    trackerUriList = []
    response = requests.get(trackerListUrl, auth=HTTPBasicAuth(loginId, loginPw))
    responseJson = response.json()
    for eachJson in responseJson:
        if exceptionTrackerNameSubstring not in eachJson['keyName']:
            trackerUriList.append(eachJson['uri'])
    # print(trackerUriList)
    return trackerUriList

def deleteTrakers(trackerUriList):
    for trackerUri in trackerUriList:
        response = requests.delete(trackerDeleteUrl + trackerUri, auth=HTTPBasicAuth(loginId, loginPw))
        print(trackerUri + " deletion status : " + str(response.status_code))


deleteTrakers(getTrackerList(trackerListUrl))
