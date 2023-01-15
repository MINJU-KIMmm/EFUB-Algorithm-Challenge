def solution(array, commands):
    list_ = []
    for comm in commands:
        arr = array[comm[0]-1:comm[1]]
        arr1 = sorted(arr)
        arr2 = arr1[comm[2]-1]
        list.append(arr2)
    return list