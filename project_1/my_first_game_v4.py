"""Игра угадай число
компьютер сам загадывает и угадывает число"""

import numpy as np

enigma = np.random.randint(1, 16) # рандомно загадываем число
print(f'Число которое надо угадать {enigma}')
def random_predict(number:int=1) -> int:

    """рандомно угадываем число
    
    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 16) # предполагаемое загаданное число
    while True:
        count += 1
        if number == predict_number:
            break # выход из цикла, если угадали
        if number < predict_number:
            predict_number -= 1
        if number > predict_number:
            predict_number += 1
            
        
    return count

print(f'Количество попыток: {random_predict(enigma)}')