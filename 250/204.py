class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        tmp = [1] * n
        tmp[0] = tmp[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if tmp[i]:
                for j in range(2, (n - 1)/i+1):
                    tmp[i*j] = 0
        return sum(tmp)