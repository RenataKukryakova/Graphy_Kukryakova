from Constants import Constants
from UI.Windows.MainWindow import MainWindow
from UI.Windows.SizeWindow import SizeWindow
from UI.Windows.MatrixWindow import MatrixWindow

class Application:
    def __init__(self):
       self.__main_window = MainWindow(self)

    def run(self):
        self.__main_window.mainloop()

    def go_to_size_window(self):
        size_window = SizeWindow(self)
        size_window.geometry("300x100")
        size_window.resizable(False, False)
        size_window.grab_set()

    def go_to_matrix(self, rows, columns):
        matrix_window = MatrixWindow(rows, columns)
        matrix_window.resizable(False, False)
        matrix_window.grab_set()