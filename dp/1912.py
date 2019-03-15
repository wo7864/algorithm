if __name__ == "__main__":
    n = int(input())
    array = []
    str_array = input()
    str_array = str_array.split()
    for i in str_array:
        tmp = int(i)
        array.append(tmp)
    for i in range(1, n):
        if array[i-1] > 0:
            if array[i-1]+array[i] > 0:
                array[i] = array[i-1] + array[i]
    result = -1000
    for i in range(0, n):
        if array[i] > result:
            result = array[i]
    print(result)
