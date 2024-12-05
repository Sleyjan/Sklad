import openpyxl

def find_keyword(filename, keyword):
  """Ищет указанное ключевое слово во всех ячейках Excel файла.

  Args:
    filename: Имя файла Excel.
    keyword: Искомое ключевое слово.
  """

  workbook = openpyxl.load_workbook(filename)
  sheet = workbook.active  # Выбираем активный лист
  print(keyword)

  for row_idx, row in enumerate(sheet.iter_rows()):
    for cell in row:
      if keyword in str(cell.value):
        straka = [str(cell.value) for cell in row]
        print('--'.join(straka[1:5]))



# Пример использования
find_keyword('/home/oybek/Ткацкая Lohia.xlsx', 'rh')
