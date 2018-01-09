class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a.split('+'), b.split('+')
        a1, a2 = int(a[0]), int(a[1][:-1])
        b1, b2 = int(b[0]), int(b[1][:-1])
        c = a1 * b1 - a2 * b2
        d = a1 * b2 + a2 * b1
        return str(c) + '+' + str(d) +'i'
