class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.arr = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            return False
        self.arr.append(val)
        self.length += 1
        self.data[val] = self.length - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            last = self.arr.pop()
            self.length -= 1
            if val != last:
                self.arr[self.data[val]] = last
                self.data[last] = self.data[val]
            del self.data[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        if self.length:
            return self.arr[random.randrange(self.length)]
