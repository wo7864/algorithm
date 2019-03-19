def solution(priorities, location):
    arr = []
    arr2 = []
    for idx, i in enumerate(priorities):
        arr.append(i)
        arr2.append(idx)
    arr.sort(reverse=True)
    priorities.reverse()
    arr2.reverse()
    i = len(priorities)-1
    cnt = 0
    while 1:
        print(arr2)
        print(priorities)
        if priorities[i] == arr[0]:
            arr.pop(0)
            answer = arr2.pop()
            priorities.pop()
            cnt = cnt + 1
            if answer == location:
                break
            i = i -1
        else:
            tmp1 = arr2.pop()
            tmp2 = priorities.pop()
            arr2.insert(0, tmp1)
            priorities.insert(0,tmp2)

    return cnt