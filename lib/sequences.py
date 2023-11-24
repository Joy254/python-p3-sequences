#!/usr/bin/env python3

def print_fibonacci(n):

    if n == 0:
        print('[]')
    elif n == 1:
        print('[0]')
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(f'[{", ".join(map(str, fib_sequence))}]')
