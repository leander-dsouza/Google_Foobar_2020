def solution(src, dest):
    start_x = 1 + src//8
    start_y = src - 8*(start_x-1) +1

    end_x = 1 + dest//8
    end_y = dest - 8*(end_x-1) +1


    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    q = []
    q.append([start_x,start_y,0])
    reached = [[False for i in range(8 + 1)]
                      for j in range(8 + 1)]

    reached[start_x][start_y] = True

    while len(q)>0:
        t = q[0]
        q.pop(0)

        if t[0] == end_x and t[1] == end_y:
            return t[2]

        else:
            for i in range(8):
                x = t[0]+dx[i]
                y = t[1]+dy[i]

                if 1<=x<=8 and 1<=y<=8 and not reached[x][y]:
                    reached[x][y] = True
                    q.append([x,y,t[2]+1])
