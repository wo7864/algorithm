def hap(n):
    cnt = 0
    if n == 0:
        return 1
    cnt += hap(n - 1)
    if n >= 2:
        cnt += hap(n - 2)
    if n >= 3:
        cnt += hap(n - 3)
    return cnt



if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        a = int(input())
        b = 0
        b = hap(a)
        print(b)
