CREDENTIALS_FILE = 'objectspy-16fdec13bb13.json'  # Имя файла с закрытым ключом
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 
spreadsheetId = "1Bj2iwLI4rdxtG-m14cpTFtQ89_sI5_CJHiQRDXRspgg"
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)