from tkinter import *
from tkinter import ttk
from UI.Constants import Constants

class MatrixWindow(Toplevel):


    def __init__(self, rows, columns):
        super().__init__()

        self.rows = rows
        self.columns = columns

        self.__matrix = []

        for row_number in range(self.rows):
            self.__matrix.append([])
            for column_number in range(self.columns):
                self.__matrix[row_number].append(None)

                text_field = ttk.Entry(master= self)
                text_field.insert(0, "0")
                text_field.grid(row = row_number, column = column_number)

                self.__matrix[row_number].append(text_field)

        make_analiz_button = ttk.Button(self,
                                            text="Выполнить анализ",
                                            command= self.make_analiz)
        make_analiz_button.grid(row = self.rows, column= self.columns)
    def make_analiz(self):
        matrix_for_model = [ [] for _ in range(self.rows)]

        for row_number in range(self.rows):
            for column_number in range(self.columns):
                print(row_number)
                print(column_number)

