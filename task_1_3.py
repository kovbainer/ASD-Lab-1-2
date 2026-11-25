"""
Задача 1.3 (a, b, d, e) — час виконання фрагментів програм.

Модель: кожен рядок фрагмента (присвоєння, перевірка умови циклу,
арифметична дія) — одна елементарна операція вартістю 1.
Кожна функція виконує фрагмент і рахує, скільки разів виконано рядки,
а потім порівнює з виведеною аналітично формулою T(n).
"""
import math


def frag_a(n):
    t = 0
    k = 0
    k += 1; t += 1          # 1  k += 1
    i = n; t += 1           # 2  i = n
    while True:
        t += 1              # 3  while i > 0
        if not i > 0:
            break
        i -= 1; t += 1      # 4  i -= 1
    return t


def formula_a(n):
    # 1 + 1 + (n + 1) перевірок + n декрементів
    return 2 * n + 3


def frag_b(n):
    t = 0
    k = 0
    i = n; t += 1           # 1
    while True:
        t += 1              # 2  while i > 1
        if not i > 1:
            break
        k += 1; t += 1      # 3
        i //= 2; t += 1     # 4
    return t


def formula_b(n):
    # m = floor(log2 n) ітерацій: 1 + (m + 1) + 2m
    m = n.bit_length() - 1 if n >= 1 else 0   # точне floor(log2 n)
    return 3 * m + 2


def frag_d(n):
    t = 0
    k = 0
    i = 0; t += 1                   # 1
    while True:
        t += 1                      # 2  while i < n
        if not i < n:
            break
        j = 0; t += 1               # 3
        while True:
            t += 1                  # 4  while j < i*i
            if not j < i * i:
                break
            k += 1; t += 1          # 5
            j += 1; t += 1          # 6
        i += 1; t += 1              # 7
    return t


def formula_d(n):
    # 1 + (n+1) + sum_{i=0}^{n-1} (3 + 3 i^2) = n^3 - 3/2 n^2 + 9/2 n + 2
    return (2 * n**3 - 3 * n**2 + 9 * n + 4) // 2


def frag_e(n):
    t = 0
    k = 0
    i = 1; t += 1                   # 1
    while True:
        t += 1                      # 2  while i < n
        if not i < n:
            break
        j = 1; t += 1               # 3
        while True:
            t += 1                  # 4  while j < n
            if not j < n:
                break
            k += 1; t += 1          # 5
            j *= 2; t += 1          # 6
        i *= 2; t += 1              # 7
    return t


def ceil_log2(n):
    # кількість степенів двійки 1, 2, 4, ... менших за n
    return (n - 1).bit_length() if n >= 1 else 0


def formula_e(n):
    p = ceil_log2(n)
    # 1 + (p+1) + p * (1 + (p+1) + 2p + 1) = 3p^2 + 4p + 2
    return 3 * p * p + 4 * p + 2


if __name__ == "__main__":
    for name, frag, formula, rng in [
        ("a", frag_a, formula_a, range(0, 300)),
        ("b", frag_b, formula_b, range(1, 3000)),
        ("d", frag_d, formula_d, range(0, 60)),
        ("e", frag_e, formula_e, range(1, 3000)),
    ]:
        for n in rng:
            assert frag(n) == formula(n), (name, n, frag(n), formula(n))
        print(f"1.3 {name}) формула збігається з підрахунком для n у {rng}")
