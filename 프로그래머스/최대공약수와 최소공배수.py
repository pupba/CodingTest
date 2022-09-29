def GCD(n,m):
    while(m):
        n,m =m,n%m
    return n
def LCM(n,m):
    return (n*m)//GCD(n,m)
def solution(n, m):
    return [GCD(n,m),LCM(n,m)]
