import requests

print(requests.get('https://vk.com/'))
print(requests.post('https://vk.com/', 'g'))

import random as r
print(r.uniform(2.0, 10.0))

from random import randint, choice, seed, getstate
print(randint(1, 6))
print(choice('алпоарцкщшпоща4цу'))

from math import *  # импортировать все
print(f'√49 = {sqrt(49)}')


def sqrt(x: int):
    return 'Ха! лох!'

print(f'√49 = {sqrt(49)}')
