#Работа со словарями
my_dict = {'Vasya' : 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:',my_dict['Vasya'])
print('Not existing value:', my_dict.get('Kamila'))
my_dict.update({'Kamila': 1981, 'Artem' : 1915})
a = my_dict.pop('Egor')
print('Deleted value:',a)
print('Modified dict:', my_dict)

#Работа с множествами
my_set = [1,'Яблоко', 42.314, 1,'Яблоко', 42.314,1,'Яблоко', 42.314,]
my_set = set(my_set)
print('Set:',my_set)
my_set.update([5,5,7,7,'Elka'])
my_set.discard (1)
print('Modified set:',my_set)