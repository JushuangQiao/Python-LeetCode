class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            val = i
            flag = 1
            while i:
                remain = i % 10
                if not remain or val % remain != 0:
                    flag = 0
                    break
                i /= 10
            if flag:
                ret.append(val)
        return ret

