class Matrix:

    def __init__(self, user_list):
        self.user_list = user_list

    def __str__(self):
        matrix_show = ""
        for lst in self.user_list:
            lst = "    ".join(str(el) for el in lst)
            matrix_show += lst + "\n"
        return f"{matrix_show}"

    def __add__(self, other):
        len_matrix = range(len(self.user_list))
        len_el = range(len(self.user_list[0]))
        new_matrix = self.user_list
        for line in len_matrix:
            for el in len_el:
                self.user_list[line][el] = self.user_list[line][el] + other.user_list[line][el]
        return Matrix(new_matrix)


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[1, 2, 3], [4, 5, 6]])
print(a + b)