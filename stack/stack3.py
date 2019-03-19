def solution(bridge_length, weight, truck_weights):
    bridge_length=2
    weight=10
    truck_weights=[7,4,5,6]
    ing = []
    i = 0
    target = 0
    ing.append([truck_weights[target], 0 + bridge_length])

    while 1:
        print(i, ing)
        i = i + 1
        if i == ing[0][1]:
            ing.pop(0)
        hap = 0
        for k in ing:
            hap = hap + k[0]
        if target + 1 < len(truck_weights):
            if hap + truck_weights[target + 1] <= weight:
                target = target + 1
                ing.append([truck_weights[target], i + bridge_length])

        if len(ing) == 0:
            break

    return i

if __name__ == "__main__":
    solution(0,0,0)
'''
건너는 트럭을 이중배열로 만들어서 빠져나오는 i를 설정해줌
1초에 하나씩 트럭을 넣으려고 시도함.
무게가 차지않으면 더넣음.
다리를 건너는 트럭이 비면 종료. 경과시간을 출력함.

'''