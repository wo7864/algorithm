def select(arr, i, j, N):
    for a in range(0, N):
        arr[i][a] = 1
        arr[a][j] = 1

    max_value = 0
    min_value = 0
    if i > j:
        max_value = i
        min_value = j
    else:
        max_value = j
        min_value = i
    tmp1 = i
    tmp2 = j
    for a in range(max_value, N):
        arr[tmp1][tmp2] = 1
        tmp1 = tmp1 + 1
        tmp2 = tmp2 + 1
    tmp1 = i
    tmp2 = j
    for a in range(0, min_value+1):
        arr[tmp1][tmp2] = 1
        tmp1 = tmp1 - 1
        tmp2 = tmp2 - 1
    tmp1 = i
    tmp2 = j
    while tmp1 < N and tmp2 >= 0:
        arr[tmp1][tmp2] = 1
        tmp1 = tmp1 + 1
        tmp2 = tmp2 - 1
    tmp1 = i
    tmp2 = j
    while tmp2 < N and tmp1 >= 0:
        arr[tmp1][tmp2] = 1
        tmp2 = tmp2 + 1
        tmp1 = tmp1 - 1
    return arr

def print_arr(arr):
    length = len(arr)
    print("배열입니다")
    for i in range(0, length):
        for j in range(0, length):
            print(arr[i][j], end=" ")
        print()

def check(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length):
            if arr[i][j] == 0:
                return 0
    return 1

def reset(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length):
            arr[i][j] = 0
    return arr

if __name__ == "__main__":
    N = int(input())
    max = 0
    arr = []
    tmp = []
    for i in range(0, N):
        tmp = []
        for j in range(0, N):
            tmp.append(0)
        arr.append(tmp)
    cnt = 0
    for k in range(0, N):
        for r in range(0, N):
            visit = []
            arr = reset(arr)
            i = k
            j = r
            arr = select(arr, i, j, N)
            visit.append([i, j])
            while len(visit) >= 1:
                j = j + 1
                if j >= N:
                    j = 0
                    i = i + 1
                    if i == N:
                        pop_value = visit.pop()
                        if len(visit) == 0:
                            break
                        i = pop_value[0]
                        j = pop_value[1]+1
                        arr = reset(arr)
                        for a, b in visit:
                            arr = select(arr, a, b, N)
                if j < N and i < N:
                    if arr[i][j] == 0:
                        arr = select(arr, i, j, N)
                        visit.append([i, j])



                    if check(arr) == 1:
                        length = len(visit)
                        if length == N:
                            cnt = cnt + 1
                        pop_value = visit.pop()
                        i = pop_value[0]
                        j = pop_value[1]
                        arr = reset(arr)
                        for a, b in visit:
                            arr = select(arr, a, b, N)
    print(cnt)

'''
    1개 지정한다.
    못들어가게 수정한다.
    
    다음 가능한 자리를 탐색한다.
    못들어가게 수정한다.
    반복한다.
    
    가능한 자리가 없으면 갯수를 파악한다.
    만족하면 cnt 증가.
    
    없으면 다음 스택에서 팝하고, 다음 자리를 찾는다.
    
    방문하지 않겠다고 기록한다.
    
    arr[0][0] = 1
    select(arr, 0, 0, N)
    visit.append(0)
    
    select(arr, 1, 2, N)
    
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ
    
    
'''