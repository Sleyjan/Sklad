import openpyxl

searching = True

def find_keyword(filename, keyword):
    global searching
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active

        if not keyword:
            searching = False

        if keyword:
            for row_idx, row in enumerate(sheet.iter_rows()):
                for cell in row:
                    if keyword.lower() in str(cell.value).lower():
                        straka = [str(cell.value) for cell in row]
                        print(file, '--'.join(straka[1:5]))

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

excelist =['Ткацкая Lohia.xlsx','Швейка New Long.xlsx','Экструдер Lohia.xlsx','6 m Сетка.xlsx','Bayby Lofil 20HT-80HT.xlsx','Gabbar швейка.xlsx','Дробилка Hao You.xlsx','Камерсиогка Lohia.xlsx','Камерсионка Hoa You.xlsx','Компрессор..xlsx','Крутилка.xlsx','Ламинатор Hoa You.xlsx','Ламинатор Hoa You.xlsx','Общые веши.xlsx','Печать.xlsx','Подшипники.xlsx','Ролики Ткацкий.xlsx','Склад 1чи Хона 2 кават.xlsx','Страпа.xlsx','Страпа Хитой.xlsx','Швейка китай склад.xlsx','Шпула резка.xlsx']

excel_dir ='/home/oybek/excel/'


for file in excelist:
    find_keyword(excel_dir + file, '')


