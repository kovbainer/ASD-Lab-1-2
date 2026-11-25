def f(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

def f_fast(n):
    return n * (n + 1) // 2

if __name__ == "__main__":
    for n in range(1, 2000):
        assert f(n) == f_fast(n)
    print("2.10: f(n) = n(n+1)/2, f — O(n), f_fast — O(1); перевірено")
    print("f(10) =", f(10), " f_fast(10) =", f_fast(10))
