def solution(s):
    s=s.lower()
    return True if s.count('p') == s.count('y') or (s.count('p')==0 and s.count('y') ==0) else False
