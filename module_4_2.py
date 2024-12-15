def test_function(*args):
    def inner_function(*args):
        print ("Я в области видимости функции test_function")
    inner_function()

test_function()

inner_function()