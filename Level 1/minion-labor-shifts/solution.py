from collections import Counter

def solution(data,n):
    d = Counter(data)
    return [i for i in data if d[i]>=n]
