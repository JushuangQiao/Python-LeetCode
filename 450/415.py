class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        min_len = len(num1) if len(num1) < len(num2) else len(num2)
        max_len = len(num1) if len(num1) > len(num2) else len(num2)
        ret, carry, digit = '', 0, -1
        if len(num1) <= len(num2):
            num1 = '0' * (max_len - min_len) + num1
        else:
            num2 = '0' * (max_len - min_len) + num2
        while digit >= -max_len:
            n1 = ord(num1[digit]) - ord('0')
            n2 = ord(num2[digit]) - ord('0')
            ret += str((n1 + n2 + carry) % 10)
            carry = (n1 + n2 + carry) / 10
            digit -= 1
        if carry != 0:
            ret += str(carry)
        return ret[::-1]
