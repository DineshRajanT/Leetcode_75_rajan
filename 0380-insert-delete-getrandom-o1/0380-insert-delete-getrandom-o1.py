import random
class RandomizedSet:

    def __init__(self):
        self.newSet = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.newSet:
            self.newSet.add(val)
            return True
        return False
         
        

    def remove(self, val: int) -> bool:
        if val in self.newSet:
            self.newSet.remove(val)
            return True
        return False

        

    def getRandom(self) -> int:
        if self.newSet:
            return random.choice(tuple(self.newSet))

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

