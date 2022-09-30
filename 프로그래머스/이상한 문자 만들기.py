def solution(s):
    return ' '.join(map(lambda x:''.join([i.upper() if idx%2==0 else i.lower() for idx,i in enumerate(x)]),s.split(" ")))
