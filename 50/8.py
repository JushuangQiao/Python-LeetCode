class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = ''
        for i in str.strip():
            if i == '-' or i == '+' or i.isdigit():
                if '-' not in s or '+' not in s:
                    s += i
            else:
                break
        try:
            ret = int(s)
            if ret >= -2147483648 and ret <= 2147483647:
                return ret
            elif ret < -2147483648:
                return -2147483648
            elif ret > 2147483647:
                return 2147483647
            else:
                return 0
        except:
            return 0
