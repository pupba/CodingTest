def solution(arr, divisor):
    l = sorted([e for e in arr if e%divisor == 0])
    return l if len(l) !=0 else [-1]
