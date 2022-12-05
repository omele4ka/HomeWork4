#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as RI

def create_polinom(min: int, max: int) -> dict:
    degree = int(input('Введите степень многочлена: '))
    equation_pattern = {}
    for key in range(degree, -1, -1):
        value = RI(min, max)
        equation_pattern[key] = value
    return equation_pattern

def create_equation(equation: dict) -> str:
    new_equation = ''
    first = True
    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'- {value *(-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1 '
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:
                    if key == 0:
                        new_equation += f'+ {value} '
                    elif key == 1:
                        new_equation += f'+ {value}*x '
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 0:
                        new_equation += f'- 1 '
                    elif key == 1:
                        new_equation += f'- x '
                    else:
                        new_equation += f'- x**{key}'
                elif value < 1:
                    if key == 0:
                        new_equation += f'- {abs(value)} '
                    elif key == 1:
                        new_equation += f'- {abs(value)}*x '
                    else:
                        new_equation += f'- {abs(value)}*x**{key} '
    return new_equation + '= 0'

first_polinom = create_polinom(-100, 100)
with open ('equation1.txt', 'w') as file:
    file.write(create_equation(first_polinom))
second_polinom = create_polinom(-100, 100)
with open ('equation2.txt', 'w') as file:
    file.write(create_equation(second_polinom))
print(first_polinom)
print(second_polinom)
print(create_equation(first_polinom))
print(create_equation(second_polinom))
