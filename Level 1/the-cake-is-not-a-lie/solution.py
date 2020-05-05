def solution(s):
    if not bool(s):
        return 0
    result = 0
    howlong = len(s)
    i = howlong
    while i > 0:
        n = howlong / i
        if (n * i) == howlong:
            valid = 1
            part = s[:int(n)]
            j = 1
            while j < i:
                if not s[int(j*n):int(j*n+n)] == part:
                    valid = 0
                    break
                j = j + 1
        if bool(valid):
            result = i
            break
        i = i - 1
    return result
