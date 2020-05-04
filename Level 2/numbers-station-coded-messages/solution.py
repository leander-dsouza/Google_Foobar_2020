def solution(l,t):

    for i in range(len(l)):
        count = 0
        for j in range(i,len(l)):
            count+=l[j]
            if count > t:
                break
            if count ==t:
                return [i,j]

    return [-1,-1]
