#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, содержащий сумму многочленов.

with open('equation1.txt', 'r') as file:
    first = file.readline()
with open('equation2.txt', 'r') as file:
    second = file.readline()


def encode_equation(equation: str) -> dict:
    new_equation = []
    equation = equation.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    for item in equation:
        if not 'x' in item:
            new_equation.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    new_equation.append(['1', '1'])
                elif item == '-x':
                    new_equation.append(['-1', '1'])
                else:
                    new_equation.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    new_equation.append(('1' + item).split('x**'))
                elif item.startswith('-x'):
                    new_equation.append(item.replace('-', '-1').split('x**'))
                else:
                    new_equation.append(item.split('*x**'))
    equation_pattern = {}
    for item in new_equation:
        equation_pattern[int(item[1])] = int(item[0])
    return equation_pattern


first_equation = encode_equation(first)
second_equation = encode_equation(second)

print(first_equation)
print(second_equation)

def equation_sum(first_dict: dict, second_dict: dict) -> dict:
    base = {}
    base.update(first)
    base.upsate(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])



result = equation_sum(first_equation, second_equation)
print(result)