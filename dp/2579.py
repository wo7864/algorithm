if __name__ == "__main__":
    N = int(input())
    a = []
    for i in range(0, N):
        b = int(input())
        a.append(b)
    dp = []
    dp.append(0)
    dp.append(a[0])
    dp.append(a[0]+a[1])
    for idx, j in enumerate(a):
        n = idx+3
        if n-1==len(a):
            break
        value = max(dp[n-2]+a[n-1], dp[n-3]+a[n-2]+a[n-1])
        dp.append(value)
    print(dp[N])


'''
가장 큰 경우, 두번째로 큰 경우

20 10
20 25
20 25 15
20 25 20
20 25 20 10

20 25 20 25 20 25 20 25

20 
20 25
20 25
20 25 25
20 25 25 20
20 25 25 25
20 25 25 25 20
20 25 25 25 25
'''