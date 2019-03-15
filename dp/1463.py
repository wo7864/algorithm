def fun(n):
    if n == 1:
        return 1
    if n % 3 == 0:
        return 1 + fun(n / 3)
    elif n % 3 == 1:
        return 2 + fun((n - 1) / 3)
    elif n > 6 and n % 6 == 5:
        return 3 + fun((n - 2) / 3)
    elif n % 2 == 0:
        return 1 + fun(n / 2)
    else:
        return 1 + fun(n - 1)


if __name__ == "__main__":
    N = int(input())
    print(fun(N)-1)


'''
6의 나머지가

'''