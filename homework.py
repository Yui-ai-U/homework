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

def show_basic_operations(a, b):
    """四則演算の結果を表示する関数"""
    print("\n【四則演算の結果】")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} × {b} = {a * b}")

    if b == 0:
        print(f"{a} ÷ {b} = 計算できません（0で割ることはできません）")
    else:
        print(f"{a} ÷ {b} = {a / b}")

def show_integer_functions(a, b):
    """整数のときだけ使える追加機能を表示する関数"""
    print("\n【整数向けの追加機能】")

    if not (is_integer_number(a) and is_integer_number(b)):
        print("小数が含まれているため、最大公約数・最小公倍数・素因数分解は省略します。")
        return

    int_a = int(a)
    int_b = int(b)

    if int_a == 0 and int_b == 0:
        print("0と0の最大公約数・最小公倍数は計算できません。")
    else:
        gcd_value = math.gcd(int_a, int_b)
        print(f"最大公約数：{gcd_value}")

        if int_a == 0 or int_b == 0:
            print("最小公倍数：0")
        else:
            lcm_value = abs(int_a * int_b) // gcd_value
            print(f"最小公倍数：{lcm_value}")

    print(f"{int_a} の素因数分解：{prime_factorization(abs(int_a))}")
    print(f"{int_b} の素因数分解：{prime_factorization(abs(int_b))}")

def show_ratio(a, b):
    """2つの数の比を約分して表示する関数"""
    print("\n【比の約分】")

    if b == 0:
        print("2つ目の数が0のため、比の約分はできません。")
        return

    ratio = Fraction(a / b).limit_denominator()
    print(f"{a} : {b} = {ratio.numerator} : {ratio.denominator}")