if __name__ == "__main__":
    n = int(input())
    if n < 2:
        tmp = int(input())
        print(tmp)
    else:
        array = []
        for i in range(0, n):
            tmp = int(input())
            array.append(tmp)
        dp = []
        dp.append(0)
        dp.append(array[0])
        dp.append(dp[1] + array[1])
        for i in range(3, n+1):
            tmp1 = dp[i-3] + array[i-2] + array[i-1]
            tmp2 = dp[i-2] + array[i-1]
            tmp3 = dp[i-1]
            dp.append(max(tmp1, tmp2, tmp3))
        print(dp[n])


'''
1번째 잔을 빼는 경우    dp[i-3] + array[i-2] + array[i-1]
2번째 잔을 빼는 경우    dp[i-2] + array[i-1]
3번재 잔을 빼는 경우    dp[i-1]

dp[0] = 0
dp[1] = 6
dp[2] = 16

'''