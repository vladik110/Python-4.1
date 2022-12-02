#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 20)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

        # находим максимальное число и его координаты
        # [0] - максимальное число, [1] - строка максимума, [2] - столбец максимума,
        # [3] - число четных
        list_information_max_num = find_max(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            # выводим на кэран информацию о расположении максимального числа
            self.label_max.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']\n'
                + 'Число четных:' + str(list_information_max_num[3]))

    def solve(self):
        try:
            list_information_max_num = find_max(self.tableWidget)

            if not list_information_max_num:
                self.label_error.setText('Введены некорректные данные!')
            else:
                self.label_max.setText(
                    'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                    str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']\n'
                    + 'Число четных:' + str(list_information_max_num[3]))

                max_num = list_information_max_num[0]
                row_max_number = list_information_max_num[1]
                col_max_number = list_information_max_num[2]
                count = list_information_max_num[3]
                # -*- решение задания -*-
                self.tableWidget.setItem(row_max_number, col_max_number, QTableWidgetItem(str(max_num + count)))
                self.label_error.setText('')
        except:
            self.label_error.setText('Введены некорректные данные!')


def find_max(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    max_num = int(table_widget.item(row_max_number, col_max_number).text())  # Максимальное значение

    count = 0  # Число четных
    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        row = 0
        while row < (row_max_number + 1):
            if row == row_max_number:
                while col < col_max_number:
                    number = int(table_widget.item(row, col).text())
                    if (number % 2) == 0:
                        count += 1
                    col += 1
            else:
                while col < table_widget.columnCount():
                    number = int(table_widget.item(row, col).text())
                    if (number % 2) == 0:
                        count += 1
                    col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number, count]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
