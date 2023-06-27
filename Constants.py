class Constants:
    application_title = "Graphy"

    __application_width = "500"
    __application_height = "75"

    adjacency_button_text = "Задать матрицу смежности"
    incidence_button_text = "Задать матрицу инцидентности"

    buttons_width = 50
    buttons_height = 50

    matrix_size_info = "Пожалуйста, укажите размерность вашей матрицы"

    def application_metrics(self):
        return self.__application_width + "x" + self.__application_height

    def button_metrics(self):
        return self.buttons_width + "x" + self.buttons_height