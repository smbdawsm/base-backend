# Подключаем библиотеки
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import itertools
from mongo import Database
from properties import LIST_OF_TABLE
import time


CREDENTIALS_FILE = 'objectspy-0e5376c4ae44.json'  # Имя файла с закрытым ключом
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 
spreadsheetId = "1-_INlB5BVp_N3mYomwivBvdeLqnURAnXfgkmoJvx66Y"
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()

'''
def ListsOfSheet(spreadsheet):
    lists = spreadsheet.get('sheets')
    return lists


sheetList = spreadsheet.get('sheets')
for sheet in sheetList:
    print(sheet['properties']['sheetId'], sheet['properties']['title'])
    
sheetId = sheetList[0]['properties']['sheetId']

print('Мы будем использовать лист с Id = ', sheetId)
'''

row = 1
db = Database()

def Add_to_Base(row):
    ranges = ["A1:Z1"]          
    results = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheetId, 
                                        ranges = ranges, 
                                        valueRenderOption = 'FORMATTED_VALUE',  
                                        dateTimeRenderOption = 'FORMATTED_STRING').execute() 
    sheet_values = results['valueRanges'][0]['values']
    ranges2 = [f"A{row}:Z{row}"]
    results2 = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheetId, 
                                        ranges = ranges2, 
                                        valueRenderOption = 'UNFORMATTED_VALUE',  
                                        dateTimeRenderOption = 'FORMATTED_STRING').execute() 
    sheet_values2 = results2['valueRanges'][0]['values']
    list1=sum(sheet_values,[])
    list2=sum(sheet_values2,[])
    parsed_string = zip(list1,list2)
    object_ot = dict(parsed_string)
    if object_ot['Октябрь 2020'] == '':
        print(f'ROW {row} - Bad entree')
        time.sleep(1)
        pass
    elif object_ot['Октябрь 2020'] != '' and object_ot['key'] == 1 :
        db.insert_document(db.objects_collection, object_ot)
        print(f'ROW {row}, OK, {object_ot}')
        time.sleep(1)
while row < 810:
    row += 1
    Add_to_Base(row)