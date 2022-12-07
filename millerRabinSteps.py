import math
from sympy import factorint

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

        # n = 2^s * d + 1

        message = f'{n} = 2^{s} * {d} + 1\n\n'

        for a in range(2, min(n - 2, math.floor(2 * (math.log(n)**2))) + 1):

            message += f'\nFor a = {a}, \n'
            x = pow(a, d, n)
            message += f'x = {x} \n'
            if x == 1 or x == n - 1:
                message += f'{x} = 1 or {x} = {n - 1} \n'
                continue
            for r in range(1, s):
                message += f'\tFor r = {r}, \n'
                x = pow(x, 2, n)
                message += f'\t\tx = {x} \n'
                if x == 1:
                    message += f'\t\tx = 1 \n'
                    primality = False
                    break
                if x == n - 1:
                    message += f'\t\tx = {n - 1} \n'
                    break
            else:
                message += f'\tx = {n - 1} \n'
                primality = False
                break
        
        if primality:
            message += f'{n} is prime.'
        else:
            message += f'\n\n{n} is not prime.'

            f = factorint(n)

            strOut = f'{n} = '
            for k, v in f.items():
                strOut += ''.join([f'{k}*' for i in range(v)])

            message += ' \n' + strOut[:-1]
        
    return str(message)

mR = millerRabin(num)