"""
Задание "Программистам всё можно"
"""
def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except:
        a = f"{a}"
        b = f"{b}"
        return a + b

if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
