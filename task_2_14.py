from math import factorial, isclose, prod

def sum_a(n):
    s, ops = 0, 0
    for i in range(n + 1):
        s += i; ops += 1
    return s, ops

def sum_b(n):
    s, ops = 0, 0
    for i in range(n + 1):
        s += i * i; ops += 2
    return s, ops

def sum_c(n, a):
    s, p, ops = 0, 1, 0
    for i in range(n + 1):
        s += p; ops += 1
        p *= a; ops += 1
    return s, ops

def sum_d(n):
    s, ops = 1, 0
    for i in range(1, n + 1):
        p = 1
        for _ in range(i):
            p *= i; ops += 1
        s += p; ops += 1
    return s, ops

def prod_e(n):
    r, ops = 1.0, 0
    for i in range(1, n + 1):
        r /= (1 + i); ops += 2
    return r, ops

def prod_f(n):
    r, fact, ops = 1.0, 1.0, 0
    for i in range(1, n + 1):
        fact *= i; ops += 1
        r /= (1 + fact); ops += 2
    return r, ops

def prod_g(n, a):
    r, p, fact, ops = 1.0, 1.0, 1.0, 0
    for i in range(1, n + 1):
        p *= a; fact *= i; ops += 2
        r *= p / (1 + fact); ops += 3
    return r, ops

def prod_h(n, m):
    r, ops = 1.0, 0
    for i in range(1, n + 1):
        p = 1.0
        for _ in range(m):
            p *= i; ops += 1
        r /= (1 + p); ops += 2
    return r, ops

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
