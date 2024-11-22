name = 'Chris'
food = 74
print(f'Hello. My name is {name} and I like {food}.')
print(f'Hello. My name is {name} and I like {food}.')
a = 7
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")