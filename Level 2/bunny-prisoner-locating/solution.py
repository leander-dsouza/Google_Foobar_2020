def solution(x, y):
    y_diff = y - 1
    corner = x + y_diff
    id = corner * (corner + 1) // 2
    id -= y_diff
    return str(id)
