if __name__ == "__main__":
    N = int(input())
    dp = []
    dp.append(1)
    dp.append(1)
    for i in range(2, N):
        dp.append(dp[i-2] + dp[i-1])
    print(dp[N-1])


'''
1
1
2
3
맨 끝자리가 
그 이전 것에 0 을 붙인 모든경우 + 이전것에서 0인경우를 찾을 방법??
'''