from random import choice

def create_string():
    string = ''
    for i in range(10):
        if i % 2 == 0:
            string += choice('2468')
        else:
            string += choice('abcdefghijklmnopqrstuvwxyz')
    return string

print(create_string())

