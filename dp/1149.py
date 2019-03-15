if __name__ == "__main__":
    N = int(input())
    house = []
    dp = []
    for i in range(0, N):
        pay = []
        data = input()
        data = data.split()
        for j in data:
            pay.append(int(j))
        house.append(pay)
    dp.append(house[0])
    for i in range(1, N):
        r_dp = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
        g_dp = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
        b_dp = min(dp[i-1][1], dp[i-1][0]) + house[i][2]
        dp.append([r_dp, g_dp, b_dp])
    print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

'''
    집이 하나 일 때 : 집하나의 최소 색깔
    집이 두개 일 때 : 겹치지 않는 인덱스의 최소들의 합.
    집이 세개 일 때 : 
    
    
    26 40 27
    49 1000 57
    13 89 99
    
    간단하게는 
    dp[i] = dp[i-1] + min(a[i])
    dp[0][0] = house[0][0]
    dp[0][1] = house[0][1]
    dp[0][2] = house[0][2]
    
    dp[n][0] = min(dp[n-1][1],dp[n-1][2]) + house[n][0]
'''