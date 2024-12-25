my_list = ["dog", 23, "cat",
41, "fish"]
for elem in my_list:
    if isinstance(elem, str):
        print(elem.upper())
    else:
        print(elem)