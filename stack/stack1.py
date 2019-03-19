def solution(arrangement):
    stack = []
    pre = ''
    now = arrangement[0]
    answer = 0
    for i in arrangement:
        pre = now
        now = i
        if pre == '(' and now == ')':
            stack.pop()
            answer = answer + len(stack)
        elif i == '(':
            stack.append(i)
        else:
            answer = answer + 1
            stack.pop()

    return answer


'''
    '('를 스택에 쌓으면서 현재 걸린 막대기 수 파악
    (뒤에 ) 가 있으면 레이저로 추정.
    )가있으면 pop하여 막대기 제거

'''