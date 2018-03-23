Структура проекта

/ram_data/*.py - модули, содержашие в себе описания структуры базы данных(схемы, доменов, таблиц и т.д.)
/convertion_modules/minidom_fixed.py - исправленая библиотека minidom для корректного экспорта в xml-формат
/convertion_modules/ram_to_xml.py - конвертирует ram-представление в xml-файл
/convertion_modules/xml_to_ram.py - конвертирует содержимое xml-файла в ram-представление
/convertion_modules/ram_to_dbd.py - конвертирует ram-представление в db-файл
/main.py - главный модуль, последовательно вызывающий модули конвертации
/tasks.xml - ресурс-файл, конвертируется в ram
/result.xml - результирующий xml-файл, генерируется из созданного ram_to_xml.py документа minidom
/result.db - результирующий db-файл, генерируется с помощью ram_to_dbd.py
