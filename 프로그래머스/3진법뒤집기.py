def solution(n):
    int_3 = ''
    while n:
        int_3+= str(n%3)
        n //= 3
    return sum([3**idx*int(i) for idx,i in enumerate(int_3[-1::-1])])
