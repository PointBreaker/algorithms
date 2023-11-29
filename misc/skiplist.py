class Skiplist:

    def __init__(self):
        self.s = {}

    def search(self, target: int) -> bool:
        if target in self.s.keys():
            return self.s[target] >= 1
        return False

    def add(self, num: int) -> None:
        if num in self.s.keys():
            self.s[num] += 1
        else:
            self.s[num] = 1

    def erase(self, num: int) -> bool:
        if num in self.s and self.s[num] > 0:
            self.s[num] -= 1
            return True
        else:
            return False

if __name__ == "__main__":
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    print(skiplist.search(0))
    skiplist.add(4)
    skiplist.search(1)
    skiplist.erase(0)
    skiplist.erase(1)
    skiplist.search(1)
    