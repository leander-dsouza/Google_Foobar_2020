def solution(start, length):
    checksum = 0
    l = length
    while l:
        checksum^=xor_sum(start)^xor_sum(start+l)
        start+=length
        l-=1
    return checksum

def xor_sum(n):
    if n == 0:
        return 0
    elif (n-1) % 4 == 0:
        return n-1
    elif (n-1) % 4 == 1:
        return 1
    elif (n-1) % 4 == 2:
        return n
    else:
        return 0
