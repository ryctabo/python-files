def say_hello(name = None):
    if name is None:
        return 'Hello world!'
    else:
        return f'Hi {name}!'
    
hello1 = say_hello()
print(hello1)

hello2 = say_hello('kevin')
print(hello2)
