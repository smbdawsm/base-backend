# base-backend

`mongo.py` - скрипт для коннекта к базе, с функциями записи, удаления, редактирования и вывода записей


`GsheetParser.py` скрипт для парсинга Google таблиц, с записью в базу.

`quickstart.py` дефолтный файл от Google

 Добавлен файл `properties.py` с константами.
 содержание:
 
 
          `DBADDRESS` IP адрес MongoDB


          `OPTIONS` Опции для GET запроса данных из базы в формате { '_id': 0, 'name': 1}


          `NAME` Имя проекта FastAPI


          `LIST_OF_TABLE` = "страница таблицы!A1:C1" Константа для задания первой строки  названиями ключей для MongoDB, Для корректной работы скрипта нужно будет вручную изменить переменную row и строку с данными в файле `GsheetParser.py`
