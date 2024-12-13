import sys
import os
from importlib.resources import files
from itertools import count
from platform import system
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLineEdit, QVBoxLayout, QLabel,QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QThread, pyqtSignal, Qt

import openpyxl
from openpyxl.styles.builtins import total
from pygments.lexers.webassembly import keywords

class WorkerThread(QThread):
    finished = pyqtSignal()
    results = pyqtSignal(list) # Изменено на список для хранения множества результатов
    total_matches_changed = pyqtSignal(int)

    def __init__(self, files,keyword):
        super().__init__()
        self.files = files
        self.keyword = keyword
        self.total_matches = 0

    def run(self):
        processed_files = []
        for file in self.files:
            results = []  # Список для хранения результатов по файлу
            workbook = openpyxl.load_workbook(file)
            sheet = workbook.active
            for row_idx, row in enumerate(sheet.iter_rows()):
                for cell in row:
                    if str(self.keyword).lower() in str(cell.value).lower(): # Поиск с учетом регистра
                        results.append(f"{file} -- {'--'.join(str(cell.value) for cell in row[0:5])}")
                        self.total_matches += 1


            processed_files.append(results)

        self.total_matches_changed.emit(self.total_matches)
        self.results.emit(processed_files)  # Выдаем список результатов
        self.finished.emit()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_files = []
        self.results = []
        self.count = count
        self.initUI()
        self.setFixedSize(1200, 700)

    def initUI(self):
        self.btn = QPushButton('Открыть', self)
        self.btn1 = QPushButton('Поиск', self)
        self.btn.move(5, 20)
        self.btn1.move(5, 100)
        self.label = QLabel("Гатов к поиску")
        self.label.setStyleSheet("color: green;")
        font_label = QFont()
        font_label.setPointSize(32)
        self.label.setFont(font_label)
        self.label_1 = QLabel()
        font_label_1 = QFont()
        font_label_1.setPointSize(20)
        self.label_1.setFont(font_label_1)
        font_scrol_area = QFont()
        font_scrol_area.setPointSize(16)

        self.textbox = QLineEdit()
        self.scroll_area = QScrollArea()
        self.scroll_area.setFont(font_scrol_area)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setFixedHeight(450)
        layout = QVBoxLayout()
        layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        layout.addWidget(self.btn1, alignment=Qt.AlignHorizontal_Mask)
        layout.addWidget(self.textbox, alignment=Qt.AlignTop | Qt.AlignRight)
        layout.addWidget(self.label, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(self.label_1, Qt.AlignCenter | Qt.AlignCenter)
        layout.addWidget(self.scroll_area,alignment=Qt.AlignTop)
        self.label = QLabel()
        self.scroll_area.setWidget(self.label)
        self.textbox.setFixedSize(300, 30)
        self.setLayout(layout)
        self.btn.clicked.connect(self.showDialog)
        self.btn1.clicked.connect(self.find_word)
        self.setWindowTitle('Поиск по файлам')
        self.show()


    def find_word(self):
        self.results.clear()  # Очистить предыдущие результаты перед поиском
        self.keyword = str(self.textbox.text()).lower()
        self.worker_thread = WorkerThread(self.selected_files, self.keyword)
        self.worker_thread.finished.connect(self.on_finished)
        self.worker_thread.results.connect(self.on_result)
        self.worker_thread.total_matches_changed.connect(self.on_total_matches)
        self.worker_thread.start()

    def showDialog(self):
        options = QFileDialog.Option()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Выбор файлов", "", " Файлы Excel (*.xlsx)")
        if files:
            self.selected_files = files

    def on_total_matches(self, total_matches):
        print(f"Найдено совпадений: {total_matches}")
        self.label_1.setText(f"Найдено совподений : {total_matches}")

    def on_finished(self):
        print("Обработка файлов завершена")


    def on_result(self, processed_files):
        result_text = "\n".join(item for sublist in processed_files for item in sublist)
        result_text = "\n".join(result.split("/")[-1] for result in result_text.splitlines())
        print(result_text)
        self.label.setText(result_text)
        if len(result_text) == 0:
            self.label.setText('Нет совподаемых слов !!!')
        #self.label.setText(f"Найдено соваодений : {self.total_matches}")
        # Получаем размер виджета и определяем позицию нижнего правого угла
        size = self.label.sizeHint()
        x = size.width()
        y = size.height()

        # Делаем нижний правый угол видимымre
        self.scroll_area.ensureVisible(x, y)


if __name__ =="__main__":
     app = QApplication(sys .argv)
     ex =MyApp()
     sys.exit(app.exec_())
