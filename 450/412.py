class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [(not i % 3)*'Fizz' + (not i % 5)*'Buzz' or str(i) for i in range(1, n+1)]
