import math


def solution(progresses, speeds):
    speeds = [1,1,5]
    progresses = [93,93,55]
    arr = []
    for i in range(0, len(progresses)):
        arr.append(math.ceil((100 - progresses[i]) / speeds[i]))
    answer = []
    while len(arr) > 0:
        remove = []
        cnt = 0
        check = 0
        length = len(arr)
        for i in range(1, length):
            if arr[i] > arr[0]:
                check = 1
            if arr[0] >= arr[i] and check == 0:
                remove.append(arr[i])
                cnt = cnt + 1
        for i in remove:
            arr.remove(i)
        arr.pop(0)
        cnt = cnt + 1
        answer.append(cnt)
    print(answer)
    return answer

if __name__ == "__main__":
    solution(0,0)
'''
(math.ceil(100- progresses/speeds))
첫번째기능이 완성될때, 이보다 작은 숫자들 모두 팝
반복. 끝

'''