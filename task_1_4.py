from functools import lru_cache

def rec_a(n, a):
    return 1 if n <= a else rec_a(n - a, a) + 1

def formula_a(n, a):
    return max(1, -(-n // a))


@lru_cache(maxsize=None)
def rec_b(n):
    return 1 if n == 0 else rec_b(n - 1) + 2 ** n

def formula_b(n):
    return 2 ** (n + 1) - 1


@lru_cache(maxsize=None)
def rec_c(n):
    return 1 if n == 1 else 2 * rec_c(n // 2) + 1

def formula_c(n):
    k = n.bit_length() - 1
    return 2 ** (k + 1) - 1

if __name__ == "__main__":
    for a in range(1, 8):
        for n in range(-5, 300):
            assert rec_a(n, a) == formula_a(n, a), (a, n)
    print("1.4 a) T(n) = ceil(n/a) — перевірено")
    for n in range(0, 500):
        assert rec_b(n) == formula_b(n), n
    print("1.4 b) T(n) = 2^(n+1) - 1 — перевірено")
    for n in range(1, 5000):
        assert rec_c(n) == formula_c(n), n
    print("1.4 c) T(n) = 2^(floor(log2 n)+1) - 1 — перевірено")
