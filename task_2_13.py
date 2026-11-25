from functools import lru_cache

def T_a(n):
    t = 1
    for _ in range(n):
        t += 1
    return t

def T_e(n):
    t = 1
    for k in range(1, n + 1):
        t += k
    return t

def make_T_g(a):
    @lru_cache(maxsize=None)
    def T(n):
        return 1 if n <= 1 else a * T(n // a) + 1
    return T

if __name__ == "__main__":
    print("a)  n, T(n)/n")
    for n in (10, 100, 1000, 10000):
        print(f"   {n:>6} {T_a(n) / n:.4f}")
    print("e)  n, T(n)/n^2")
    for n in (10, 100, 1000, 10000):
        print(f"   {n:>6} {T_e(n) / n**2:.4f}")
    for a in (2, 3, 5):
        T = make_T_g(a)
        print(f"g)  a={a}: n, T(n)/n")
        for k in (3, 6, 9, 12):
            n = a ** k
            print(f"   {n:>10} {T(n) / n:.4f}")
