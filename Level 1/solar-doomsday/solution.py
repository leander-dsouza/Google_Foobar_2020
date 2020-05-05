def solution(area):
    res = []
    while (area > 0):
        biggest_square_side = int(area ** 0.5)
        biggest_square = biggest_square_side ** 2
        area -= biggest_square
        res.append(biggest_square)
    return res
