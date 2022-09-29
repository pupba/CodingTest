def solution(price, money, count):
    total = sum([i*price for i in range(1,count+1)])
    return 0 if total <= money else total-money
