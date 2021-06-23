# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, my_list):
        self._my_list = my_list

    def __str__(self):
        for row in self._my_list:
            for x in row:
                print(f"{x:1} ", end="")
            print('')
        return ''

    def __add__(self, other):
        for i in range(len(self._my_list)):
            for j in range(len(other._my_list[i])):
                self._my_list[i][j] = self._my_list[i][j] + other._my_list[i][j]
        return Matrix.__str__(self)

t1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Первая матрица')
t1.__str__()
t2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print('Вторая матрица')
t2.__str__()
print('Сумма матриц')
print(t1.__add__(t2))
