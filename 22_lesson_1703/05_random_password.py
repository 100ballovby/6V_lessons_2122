import random as r
import string as s

passwords = []
alphabet = s.ascii_letters  # сохраняю все буквы английского алфавита
nums = s.digits  # сохраняю цифры

for password in range(20):
    passw = ''  # пустой пароль
    for symbol in range(8):  # повторить 8 раз
        symbols = r.choice(alphabet + nums)
        # Складываю символы и числа в одну строку и достаю случайный элемент
        passw += symbols  # добавляю случайный символ к паролю
    passwords.append(passw)  # добавляю пароль в список

print(passwords)


