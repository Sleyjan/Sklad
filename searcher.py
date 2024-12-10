import sys
import os
from importlib.resources import files
from platform import system
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QFileDialog,QLineEdit,QVBoxLayout

from docutils.nodes import option
from PyQt5.QtCore import QThread,pyqtSignal,Qt

import openpyxl
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
        self.selected_files = []
        self.initUI()
    def initUI(self):
        self.btn = QPushButton('open',self)
        self.btn1 = QPushButton('Search',self)
        self.btn.move(5,20)
        self.btn1.move(5,100)

        self.textbox =  QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.btn,alignment=Qt.AlignLeft)
        layout.addWidget(self.btn1, alignment=Qt.AlignHorizontal_Mask )
        layout.addWidget(self.textbox, alignment=Qt.AlignTop | Qt.AlignRight)
        self.textbox.setFixedSize(300,30)
        self.setLayout(layout)
        self.btn.clicked.connect(self.showDialog)
        self.btn1.clicked.connect(self.find_word)
        self.setGeometry(100,100,450,350)
        self.setWindowTitle('allFiles')
        self.show()

    def find_word(self):
        print(self.selected_files)
        keyword = str(self.textbox.text())
        for file in self.selected_files:

            workbook = openpyxl.load_workbook(file)
            sheet = workbook.active
            for row_idx, row in enumerate(sheet.iter_rows()):
                for cell in row:
                    if keyword in str(cell.value):
                        print(file,'--'.join(str(cell.value) for cell in row[0:5]))
                    else:
                        print('Нет ключевое слово токое')

    def showDialog(self):
        options = QFileDialog.Option()
        options |= QFileDialog.DontUseNativeDialog
        files, _=QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()","","ALl Files(*);;Excel Files(*.xlsx)")
        if files:
            self.selected_files = files
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
