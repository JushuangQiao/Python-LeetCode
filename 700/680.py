class Solution(object):

    def isPalindrome(self, s, left, right, flag):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if flag == 1:
                    return False
                flag = 1
                return (self.isPalindrome(s, left+1, right, flag) or
                        self.isPalindrome(s, left, right-1, flag))
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s)-1, 0)
