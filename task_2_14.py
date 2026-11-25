"""
Задача 2.14 — доведення співвідношень.

Згідно із зауваженням у методичці, для доведення треба запропонувати
алгоритм обчислення виразу з лівої частини, час виконання якого має
оцінку з правої частини. Вважаємо арифметичні операції елементарними
(вартість O(1)). Кожна функція також рахує кількість виконаних
множень/додавань (ops), щоб показати оцінку на практиці.
"""
from math import factorial, isclose, prod


# a) sum_{i=0}^{n} i = O(n): один цикл з n+1 ітерацій
def sum_a(n):
    s, ops = 0, 0
    for i in range(n + 1):
        s += i; ops += 1
    return s, ops


# b) sum_{i=0}^{n} i^2 = O(n): у кожній ітерації одне множення і одне додавання
def sum_b(n):
    s, ops = 0, 0
    for i in range(n + 1):
        s += i * i; ops += 2
    return s, ops


# c) sum_{i=0}^{n} a^i = O(n): степінь a^i отримуємо з a^(i-1) одним множенням
def sum_c(n, a):
    s, p, ops = 0, 1, 0
    for i in range(n + 1):
        s += p; ops += 1
        p *= a; ops += 1
    return s, ops


# d) sum_{i=0}^{n} i^i = O(n^2): i^i рахуємо внутрішнім циклом з i множень,
#    усього 0 + 1 + ... + n = n(n+1)/2 = O(n^2) множень
def sum_d(n):
    s, ops = 1, 0           # 0^0 = 1
    for i in range(1, n + 1):
        p = 1
        for _ in range(i):
            p *= i; ops += 1
        s += p; ops += 1
    return s, ops


# e) prod_{i=1}^{n} 1/(1+i) = O(n)
def prod_e(n):
    r, ops = 1.0, 0
    for i in range(1, n + 1):
        r /= (1 + i); ops += 2
    return r, ops


# f) prod_{i=1}^{n} 1/(1+i!) = O(n): i! = (i-1)! * i — одне множення на крок
def prod_f(n):
    r, fact, ops = 1.0, 1.0, 0
    for i in range(1, n + 1):
        fact *= i; ops += 1
        r /= (1 + fact); ops += 2
    return r, ops


# g) prod_{i=1}^{n} a^i/(1+i!) = O(n): a^i та i! оновлюємо інкрементально
def prod_g(n, a):
    r, p, fact, ops = 1.0, 1.0, 1.0, 0
    for i in range(1, n + 1):
        p *= a; fact *= i; ops += 2
        r *= p / (1 + fact); ops += 3
    return r, ops


# h) prod_{i=1}^{n} 1/(1+i^m) = O(nm): i^m — внутрішній цикл з m множень
def prod_h(n, m):
    r, ops = 1.0, 0
    for i in range(1, n + 1):
        p = 1.0
        for _ in range(m):
            p *= i; ops += 1
        r /= (1 + p); ops += 2
    return r, ops


# i) prod_{i=1}^{n} 1/(1+i^i) = O(n^2): i^i — внутрішній цикл з i множень
def prod_i(n):
    r, ops = 1.0, 0
    for i in range(1, n + 1):
        p = 1.0
        for _ in range(i):
            p *= i; ops += 1
        r /= (1 + p); ops += 2
    return r, ops


def check():
    n, a, m = 15, 3, 4
    assert sum_a(n)[0] == sum(range(n + 1))
    assert sum_b(n)[0] == sum(i * i for i in range(n + 1))
    assert sum_c(n, a)[0] == sum(a ** i for i in range(n + 1))
    assert sum_d(n)[0] == sum(i ** i for i in range(n + 1))
    assert isclose(prod_e(n)[0], prod(1 / (1 + i) for i in range(1, n + 1)))
    assert isclose(prod_f(n)[0], prod(1 / (1 + factorial(i)) for i in range(1, n + 1)))
    assert isclose(prod_g(n, a)[0], prod(a ** i / (1 + factorial(i)) for i in range(1, n + 1)))
    assert isclose(prod_h(n, m)[0], prod(1 / (1 + i ** m) for i in range(1, n + 1)))
    assert isclose(prod_i(n)[0], prod(1 / (1 + i ** i) for i in range(1, n + 1)))
    print("Значення всіх виразів збігаються з еталонними.")


if __name__ == "__main__":
    check()
    print("\nКількість операцій (ops), поділена на оцінку з умови:")
    print(f"{'n':>6} {'a/n':>6} {'b/n':>6} {'c/n':>6} {'d/n^2':>6} {'e/n':>6}"
          f" {'f/n':>6} {'g/n':>6} {'h/nm':>6} {'i/n^2':>6}")
    m = 5
    for n in (10, 100, 1000):
        print(f"{n:>6} {sum_a(n)[1]/n:6.2f} {sum_b(n)[1]/n:6.2f} {sum_c(n, 2)[1]/n:6.2f}"
              f" {sum_d(n)[1]/n**2:6.2f} {prod_e(n)[1]/n:6.2f} {prod_f(n)[1]/n:6.2f}"
              f" {prod_g(min(n, 170), 2)[1]/min(n, 170):6.2f} {prod_h(n, m)[1]/(n*m):6.2f}"
              f" {prod_i(n)[1]/n**2:6.2f}")
