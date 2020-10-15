# Подключаем библиотеки
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import itertools
from mongo import Database
CREDENTIALS_FILE = 'objectspy-16fdec13bb13.json'  # Имя файла с закрытым ключом
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 
spreadsheetId = "1Bj2iwLI4rdxtG-m14cpTFtQ89_sI5_CJHiQRDXRspgg"
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
spreadsheet = service.spreadsheets().get(spreadsheetId = spreadsheetId).execute()
def ListsOfSheet(spreadsheet):
    return sheetList = spreadsheet.get('sheets')
row = 1
def Add_to_Base(row):
    ranges = ["БД Объекты!A1:CO1"]          
    results = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheetId, 
                                        ranges = ranges, 
                                        valueRenderOption = 'FORMATTED_VALUE',  
                                        dateTimeRenderOption = 'FORMATTED_STRING').execute() 
    sheet_values = results['valueRanges'][0]['values']
    ranges2 = [f"БД Объекты!A{row}:CO{row}"]
    results2 = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheetId, 
                                        ranges = ranges2, 
                                        valueRenderOption = 'FORMATTED_VALUE',  
                                        dateTimeRenderOption = 'FORMATTED_STRING').execute() 
    sheet_values2 = results2['valueRanges'][0]['values']
    list1=sum(sheet_values,[])
    list2=sum(sheet_values2,[])
    shit = zip(list1,list2)
    object_ot = dict(shit)
    Database.insert_document(objects_collection, object_ot)
    print('ROW OK')
while row < 293:
    row += 1
    Add_to_Base(row)