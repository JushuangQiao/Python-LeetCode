class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        row = col = 0
        for s in moves:
            if s == 'U':
                col += 1
            elif s == 'D':
                col -= 1
            elif s == 'L':
                row -= 1
            elif s == 'R':
                row += 1
            else:
                pass
        if row == 0 and col == 0:
            return True
        return False

