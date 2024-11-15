def add_everything_up(a, b):#функция принимает a и b, которые могут быть как числами(int, float), так и строками (str)

    if type(a) == float and type(b) == int:
        return round((a + b), 3)

    elif type(a) or type(b) == float:
        try:
            a + b
        except TypeError:
            return str(a) + str(b)

    elif type(a) or type(b) == int:
        try:
            a + b
        except TypeError:
            return str(a) + str(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



