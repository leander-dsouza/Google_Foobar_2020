def solution(s):
    ans = cnt = 0
    for i in s:
        if i == '<':
            ans += cnt;
        elif i == '>':
            cnt += 1
    return ans << 1
