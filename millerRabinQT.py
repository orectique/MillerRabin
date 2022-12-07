import math
from sympy import factorint

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

def millerRabin(n):
    n = int(n)
    if n == 0 or n == 1:
        message = 'Forget about 0 and 1. We don\'t consider them in this argument.'
    elif n == 2:
        message = '2 is prime. In fact, it\'s the only even prime number. It is also the smallest prime number.'
    elif n % 2 == 0:
        message = f'{n} is not prime. It is divisible by 2.'
    else:
        primality = True

        d = n - 1
        s = 0

        while d % 2 == 0:
            d = d // 2
            s += 1

        for a in range(2, min(n - 2, math.floor(2 * (math.log(n)**2))) + 1):
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for r in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    primality = False
                    break
                if x == n - 1:
                    break
            else:
                primality = False
                break
        
        if primality:
            message = f'{n} is prime.'
        else:
            message = f'{n} is not prime.'

            f = factorint(n)

            strOut = f'{n} = '
            for k, v in f.items():
                strOut += ''.join([f'{k}*' for i in range(v)])

            message += ' \n' + strOut[:-1]
        
    return str(message)

mR = millerRabin(num)