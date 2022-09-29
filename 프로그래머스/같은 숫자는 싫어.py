def solution(arr):
    result = [arr[0]]
    pre = arr[0]
    for e in arr[1:]:
        if e != pre:
            result.append(e)
            pre = e
    return result
