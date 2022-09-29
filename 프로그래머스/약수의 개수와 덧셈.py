def check_divisor_count(n):
    count = len([i for i in range(1,n+1) if n%i == 0])
    return n if count%2 == 0 else -n

def solution(left, right):
    return sum([check_divisor_count(i) for i in range(left,right+1)])
