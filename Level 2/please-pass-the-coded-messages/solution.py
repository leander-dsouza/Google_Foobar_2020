def calc_counts(c1, c2):
    if c2 == 0:
        return [3*int(c1/3), 0]
    diff = c1 - c2
    extra = diff % 3
    if extra == 2:
        return [c1, c2-1]
    elif extra == 1:
        return [c1 - 1, c2]
    else:
        return [c1, c2]

def form_array(h, count):
    c1, c2 = count
    ret = h[0][:]
    if c1 == 0 and c2 == 0:
        return ret
    if c1 != 0:
        a1 = h[1][:]
        a1.sort(reverse=True)
        ret.extend(a1[:c1])
    if c2 != 0:
        a2 = h[2][:]
        a2.sort(reverse=True)
        ret.extend(a2[:c2])
    return ret

def solution(l):
    h = {0: [], 1:[], 2: []}
    for i in l:
        h[i%3].append(i)
    count_1 = len(h[1])
    count_2 = len(h[2])
    arr = []
    if count_1 == count_2:
        # all elements
        arr = l
    elif count_1 > count_2:
        count_1, count_2 = calc_counts(count_1, count_2)
        arr = form_array(h, [count_1, count_2])
    else:
        count_2, count_1 = calc_counts(count_2, count_1)
        arr = form_array(h, [count_1, count_2])
    arr.sort(reverse=True)
    ret = ''.join(list(map(str, arr)))
    if len(ret) == 0:
        return 0
    return int(ret)
