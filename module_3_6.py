# "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# type ()
# dict {}
# list []

# def calculate_structure_sum(data_structure):
#     summa = 0
#     for elem in data_structure:
#         if isinstance(elem, (list, tuple)):
#             summa += calculate_structure_sum(elem)
#         elif isinstance(elem, (set)):
#             summa += calculate_structure_sum(list(elem))
#         elif isinstance(elem, dict):
#             summa += calculate_structure_sum(list(elem.keys()))
#             summa += calculate_structure_sum(list(elem.values()))
#         elif isinstance(elem, int):
#             summa += elem
#         elif isinstance(elem, str):
#             summa += len(elem)
#     return summa

def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            summa += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, (int)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa

result = calculate_structure_sum(data_structure)
print(result)
