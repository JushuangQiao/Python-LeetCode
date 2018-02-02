class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        # ret = []
        # for word in words:
        #     if any([set(word.lower()).issubset(rows[0]), 
        #            set(word.lower()).issubset(rows[1]), 
        #            set(word.lower()).issubset(rows[2])]):
        #         ret.append(word)
        # return ret
        return [word for word in words if any([set(word.lower()).issubset(row) for row in rows])]
