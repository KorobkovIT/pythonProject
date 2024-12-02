#  "Распаковка"
def print_params(a=1, b='строка', c=True):
    print(a ,b, c)

print_params(b = 25)
print_params(c = [1,2,3])
values_list = (5, 5.6, 'string')
values_dict = {'a':343, 'b':56.9, 'c':"Ulia"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)