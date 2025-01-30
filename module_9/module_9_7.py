"""
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
"""


def is_prine(func):
    def wrapper(*args):
        result = func(*args)
        primes = [0,2,3,5,7,11]
        if result in primes:
            print('простое')
        else:
            print('Составное')
        return result
    return wrapper
    
@is_prine
def sum_three(a,b,c):
    result = a+b+c
    return result    
    
    
result = sum_three(2, 3, 6)
print(result)
