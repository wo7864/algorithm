arr = []

def lotto(a, b, arr, S, k, c):
    if b == 6:
        print(arr)
        return
    for i in range(a, k):
        arr.append(S[i])
        if S[i] == 7:
            for j in range(0, c):
                arr.pop()
            c = c + 1
        elif len(arr) >= 6:
            arr.pop()
        lotto(i+1, b+1, arr, S, k, c)



if __name__ == "__main__":
    while True:
        k = int(input())
        if k == 0:
            break
        S = []
        arr = []
        for i in range(0, k):
            n = int(input())
            S.append(n)
        lotto(0, 0, arr, S, k, 1)

'''
0
추가
0 1 추가
0 1 2가되면 가득찼으므로 

'''