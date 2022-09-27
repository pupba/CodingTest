def solution(arr):
    arr.pop(arr.index(min(arr)))
    return [-1] if 0 == len(arr) else arr
