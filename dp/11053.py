if __name__ == "__main__":
    N = int(input())
    array = []
    str_array = input()
    str_array = str_array.split()
    for i in str_array:
        array.append(int(i))
    dp = []
    max_value = 0
    for idx, i in enumerate(array):
        a = 0
        for j in range(0, idx+1):
            if i > array[j]:
                if a < dp[j]:
                    a = dp[j]
        a = a + 1
        if max_value < a:
            max_value = a
        dp.append(a)
    print(max_value)

'''
10 20 30 1 2 3 4 5 60
'''