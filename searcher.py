import sys
import os
from importlib.resources import files
from platform import system
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QFileDialog
from docutils.nodes import option
from PyQt5.QtCore import QThread,pyqtSignal

#import openpyxl
class WorkerThread(QThread):
    finished = pyqtSignal()
    result = pyqtSignal(list)

    def __init__(self, files):
        super().__init__()
        self.files = files

    def run(self):
        processed_files = []
        processed_files.append(files)
        print(self.files)

        self.result.emit(processed_files)  # Передать обработанные файлы
        self.finished.emit()

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.btn = QPushButton('open',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('allFiles')
        self.show()
    def showDialog(self):
        options = QFileDialog.Option()
        options |= QFileDialog.DontUseNativeDialog
        files, _=QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()","","ALl Files(*);;Excel Files(*.xlsx)")
        if files:
            self.worker_thread = WorkerThread(files)
            self.worker_thread.finished.connect(self.on_finished)
            self.worker_thread.result.connect(self.on_result)
            self.worker_thread.start()

    def on_finished(self):
        print("Обработка файлов завершена")  # Пример действий по завершении
        self.worker_thread = None  # Очищаем ссылку на worker_thread

    def on_result(self, processed_files):
        print(processed_files)
if __name__ =="__main__":
     app = QApplication(sys .argv)
     ex =MyApp()
     sys.exit(app.exec_())

#searching = True
"""
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
"""

