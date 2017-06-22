import sys

import requests
import xlrd
from requests.auth import HTTPBasicAuth

loginUrl = 'http://10.185.7.63:8080/cb/login.spr'
itemUri = 'http://10.185.7.63:8080/cb/rest/item/'

loginId = '-'
loginPw = '-'

excelFilePath = '-'

if len(sys.argv) != 4:
    print("usage: thisProgram \"your_id\" \"your_password\" \"excelFilePath\"")
    exit(-1)

logInId = sys.argv[1]
logInPassword = sys.argv[2]
excelFilePath = sys.argv[3]


def deleteFromList(itemList):
    deletedCount = 0
    for item in itemList:
        if (item.isdigit() == False):
            continue
        response = requests.delete(itemUri + item, auth=HTTPBasicAuth(loginId, loginPw))
        if (response.text == 'null'):
            deletedCount = deletedCount + 1
            print(item + " is deleted");
        else:
            print(item + " is not exist")
    return deletedCount


def getItemList(excelFilePath):
    workbook = xlrd.open_workbook(excelFilePath)
    sheet = workbook.sheet_by_index(0)
    nrows = sheet.nrows
    itemList = []
    for row in range(nrows):
        itemList.append(str(sheet.row_values(row)[0]).split('.')[0])
    return itemList


deletedCount = deleteFromList(getItemList(excelFilePath))
print("Total Deleted: " + str(deletedCount))
