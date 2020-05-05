def solution(l):
    l.sort(key=lambda v: map(int, v.split('.')))
    return l
