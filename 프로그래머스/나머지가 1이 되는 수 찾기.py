def solution(n):
    answer = min([i for i in range(1,n+1) if 1==n%i])
    return answer
