summ = float(input('Стоимость покупки: '))

if summ > 1000:
    print(f'Скидка 15%. итоговая стоимость: {summ * 0.85}')
else:
    print(f'Итоговая сумма: {summ}')


