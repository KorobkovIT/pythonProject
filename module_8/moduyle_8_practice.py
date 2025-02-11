"""
Блоки try и except: эти конструкции являются основным инструментом для обработки исключений в Python.

try: В этом блоке помещается код, который может вызвать ошибку.
except: Здесь указывается, как программа должна реагировать на возникновение определенного типа ошибки.
"""


def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    print(operand_1, operand_2, operation)
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'Результат: {operand_1 + operand_2}')
    if operation == '-':
        print(f'Результат: {operand_1 - operand_2}')
    if operation == '/':
        print(f'Результат: {operand_1 / operand_2}')
    if operation == '//':
        print(f'Результат: {operand_1 // operand_2}')
    if operation == '%':
        print(f'Результат: {operand_1 % operand_2}')
    if operation == '*':
        print(f'Результат: {operand_1 * operand_2}')


cnt = 0

with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.arga[0]:
                print(f'Ошибка в линии {cnt}, возникло {exc}, не хватает данных для ответа.')
            else:
                print(f'Ошибка в линии {cnt}, возникло {exc}б нельзя перевести число.')
