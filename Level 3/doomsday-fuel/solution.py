import math


def generate_dist_vector(size, start, tot_length, length):
    tmp = [start]
    count = 0
    l, r = -length, tot_length - length
    for i in range(size):
        left = tmp[0]
        right = tmp[count]
        left += (l * 2)
        right += (r * 2)
        l, r = -r, -l
        tmp = [left] + tmp + [right]
        count += 2
    return tmp


def make_mat(vec1, vec2):
    mat = []
    count = 0
    for i in vec2:
        mat.append([])
        for j in vec1:
            mat[count].append((j, i))
        count += 1
    return mat


def translate(x, y, vec):
    mat = []
    count = 0
    for i in vec:
        mat.append([])
        for j in i:
            mat[count].append((j[0] + x, j[1] + y))
        # print mat[count]
        count += 1

    return mat


def serialize(vec):
    start = int(len(vec) / 2)
    elms = [vec[start][start]]
    count = 3
    start -= 1
    while (start >= 0):
        x = start
        y = start
        for j in range(1, count):
            x += 1
            elms += [vec[y][x]]
        for j in range(1, count):
            y += 1
            elms += [vec[y][x]]
        for j in range(1, count):
            x -= 1
            elms += [vec[y][x]]
        for j in range(1, count):
            y -= 1
            elms += [vec[y][x]]

        start -= 1
        count += 2
    return elms


def key(x, y):
    return format(math.atan2(x, y), '.32f')


def dist(x, y):
    return math.hypot(x, y)


def calc(cap, bad, distance):
    visited = {}
    l = len(cap)
    count = 0
    for i in range(l):
        ce = cap[i]
        be = bad[i]

        visited[key(ce[0], ce[1])] = True
        if distance - dist(be[0], be[1]) >= 0:
            k = key(be[0], be[1])
            if k not in visited:
                count += 1
                visited[k] = True
        else:
            k = key(be[0], be[1])
            visited[k] = True



    return count


def solution(dimensions, captain, badguy, distance):
    _x = 0
    _y = 1
    tx = captain[_x]
    ty = captain[_y]
    width = dimensions[0]
    height = dimensions[1]
    mat_size = int(math.ceil(max(distance / width, distance / height))) + 1
    bad_x = generate_dist_vector(mat_size, badguy[_x], width, badguy[_x])
    bad_y = generate_dist_vector(mat_size, badguy[_y], height, badguy[_y])
    cap_x = generate_dist_vector(mat_size, captain[_x], width, captain[_x])
    cap_y = generate_dist_vector(mat_size, captain[_y], height, captain[_y])

    elms_bad = serialize(translate(-tx, -ty, make_mat(bad_x, bad_y)))

    elms_cap = serialize(translate(-tx, -ty, make_mat(cap_x, cap_y)))


    return calc(elms_cap, elms_bad, distance)
