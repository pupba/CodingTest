def solution(d, budget):
    result = len(d)
    total = sum(d)
    d.sort()
    for i in range(result-1,-2,-1):
        if total > budget:
            total-=d[i]
            result-=1
        else:
            break
    return result
