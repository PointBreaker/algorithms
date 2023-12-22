class disJointSet:
    def __init__(self, n):
        ranks = []
        parents = []
        for i in range(n):
            ranks.append(0)
            parents.append(i)
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x]) # path compression
        return self.parents[x]
    
    def check(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x # attatch low rank to high rank
        self.parents[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1

if __name__ == "__main__":
    pass