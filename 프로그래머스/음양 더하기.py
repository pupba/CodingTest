def solution(absolutes, signs):
    return sum([i if op else -1*i for i,op in zip(absolutes,signs)])
