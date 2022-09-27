def solution(num):
    count = 0
    answer = 0
    while(True):
        if count==500:
            answer = -1
            break
        elif num==1:
            answer = count
            break
        elif num%2==0:
            num//=2
        else:
            num = (num*3)+1
        count+=1
    return answer
