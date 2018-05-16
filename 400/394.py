class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums, chars = [], []
        i, length = 0, len(s)
        while i < length:
            j = i + 1
            if s[i].isdigit():
                num = int(s[i])
                while j < length:
                    if s[j].isdigit():
                        num = num * 10 + int(s[j])
                        j += 1
                    else:
                        break
                nums.append(num)
            elif s[i] == '[' or s[i].isalpha():
                chars.append(s[i])
            else:
                t, tmpc = chars.pop(), []
                while t != '[':
                    tmpc.append(t)
                    t = chars.pop()
                tchars = nums.pop() * ''.join(tmpc[::-1])
                chars.append(tchars)
            i = j
        return ''.join(chars)
