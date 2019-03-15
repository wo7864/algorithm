def fun(n, cnt):
    if n % 3 == 0:
        fun(n / 3, cnt)
    elif n % 2 == 0:
        fun(n / 2, cnt)
    else:
        fun(n - 1, cnt)
    if n == 1:
        return cnt
    cnt += 1


if __name__ == "__main__":
    N = int(input())
    print(fun(N, 0))