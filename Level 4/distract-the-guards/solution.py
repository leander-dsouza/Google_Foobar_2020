class Graph:
    def __init__(self,banana_list):
        self.list_len = len(banana_list)
        self.graph = list([0]*self.list_len for i in xrange(self.list_len))
        for i in xrange(self.list_len):
            for j in xrange(self.list_len):
                if i < j: 
                    self.graph[i][j] = self.dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j]  

    def gcd(self, x, y):
       while(y):
           x, y = y, x % y
       return x

    def dead_lock(self, x,y):
        if x == y:
            return 0

        l = self.gcd(x,y)

        if (x+y) % 2 == 1:
            return 1

        x,y = x/l,y/l
        x,y = max(x,y), min(x,y)    
        return self.dead_lock(x-y,2*y)
 
    # A DFS based recursive function that returns true if a
    # matching for vertex u is possible
    def bpm(self, u, matchR, seen):
        for v in range(self.list_len):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True # Mark v as visited
 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
 

    def maxGuardPair(self):
        matchR = [-1] * self.list_len
        result = 0 
        for i in range(self.list_len):
            seen = [False] * self.list_len
            if self.bpm(i, matchR, seen):
                result += 1
        return self.list_len- 2*(result/2)


def solution(l):
    return Graph(l).maxGuardPair()
