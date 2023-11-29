from random import choice
class RandomSet:
    '''
    Insert, delete, getRandom all in O(1)
    '''
    def __init__(self):
        self.index_map = {}
        self.list_of_values = []
        self.last_val = -1
    
    def insert(self, val):
        if val in self.index_map.keys():
            return True
        self.list_of_values.append(val)
        self.index_map[val] = self.last_val
        return False
    
    def delete(self, val): 
        if val not in self.index_map.keys():
            return False
        else: # swap the value to be deleted with last element, and then pop it
            self.last_val -= 1
            last_val, index = self.list_of_values[-1], self.index_map[val]
            self.list_of_values[index] = val
            self.index_map[last_val] = index
            self.list_of_values.pop()
            return True
    
    def getRandom(self):
        return choice(self.list_of_values)
    
if __name__ == "__main__":
    s = RandomSet()
    print(s.insert(1))
    print(s.delete(2))
    print(s.insert(2))
    print(s.insert(3))
    print(s.getRandom())
    print(s.delete(3))
    print(s.getRandom())
    print(s.delete(2))
    print(s.getRandom())