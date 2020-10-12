# Подключаем библиотеки
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import itertools
from mongo import insert_document, objects_collection
import config

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
    insert_document(objects_collection, object_ot)
    print('ROW OK')
while row < 293:
    row += 1
    Add_to_Base(row)