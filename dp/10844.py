if __name__ == "__main__":
    N = int(input())
    dp = []
    dp.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    result = 0
    for i in range(1, N):
        tmp = []
        for j in range(0, 10):
            if j == 0:
                tmp.append(dp[i - 1][j + 1])
            elif j == 9:
                tmp.append(dp[i - 1][j - 1])
            else:
                tmp.append(dp[i-1][j-1] + dp[i-1][j+1])
        dp.append(tmp)
    for i in range(0, 10):
        result = result + dp[N-1][i]
    print(result%1000000000)



'''
dp[0] = 9                         
dp[1] = 9 * 2 -1               9가 하나생김 이유는 8이 1개있었기 때문

0 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9
1 1 2 2 2 2 2 2 2 1
dp[2] = 17 * 2 - 2  = 32?               dp[1]이 8이 2개, 1이 1개 였으므로, 9가 2개, 0이 1개 생김
0 1 1 1 2 2 2 3 3 3 3 4 4 4 4 5 5 55 5 6 6 6 6 7 7 7 7 8 8 8 9 9
1 3 3 4 4 4 4 
dp[3] = 32 * 2 - 2
0 0 0 0 1 1 1 1 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3

40 + 7 + 7 + 5+ 3
54 59 62

'''