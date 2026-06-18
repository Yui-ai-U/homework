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
