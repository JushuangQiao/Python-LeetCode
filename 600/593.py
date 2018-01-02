class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        a = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        b = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
        c = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
        d = (p2[0] - p3[0]) ** 2 + (p3[1] - p2[1]) ** 2
        e = (p4[0] - p2[0]) ** 2 + (p4[1] - p2[1]) ** 2
        f = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
        counter = set([a, b, c, d, e, f])
        if len(counter) == 2:
            t = [a, b, c, d, e, f]
            m, s = counter
            u = t.count(m)
            v = t.count(s)
            return (u == 4 and 2 * m == s) or (v == 4 and 2 * s == m)
        return False

