import os
from math import sin, sinh, cos, cosh, tan, tanh, pi, sqrt, ceil, floor, factorial
from sys import set_int_max_str_digits

set_int_max_str_digits(100000)

calculation = ''
answer = ''

def ans():
    return answer

def wrkr() -> int:
    global calculation, answer
    while True:
        calculation = input('\nEnter calculation -> ').replace('^', '**')
        try:
            answer = eval(f'{calculation}')
        except Exception as e:
            print(f'An exception occured ({e})')
        print(f'\nAnswer:\n{answer}')

def main() -> None:
    wrkr()

if __name__ == '__main__': main()