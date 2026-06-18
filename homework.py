print("四則演算を行うプログラム")

import math
import random
from fractions import Fraction

def get_number(message):
    """数字が入力されるまで繰り返す関数"""
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("数字を入力してください。")

def is_integer_number(value):
    """float型の値が整数として扱えるか判定する関数"""
    return value.is_integer()

def prime_factorization(n):
    """正の整数を素因数分解する関数"""
    if n <= 0:
        return "正の整数ではありません"

    if n == 1:
        return "1"

    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return " × ".join(map(str, factors))