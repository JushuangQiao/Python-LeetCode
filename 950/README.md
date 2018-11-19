# LeegtCode 901-950

905 [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)
```python
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start, end = 0, len(A) - 1
        while start <= end:
            if A[start] % 2 and not A[end] % 2:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            elif A[start] % 2 and A[end] % 2:
                end -= 1
            elif not A[start] % 2 and not A[end] % 2:
                start += 1
            else:
                start += 1
                end -= 1
        return A
```
929 [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses)
```python
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ret = {self.simplifyEmail(email): True for email in emails}
        return len(ret.keys())

    def simplifyEmail(self, email):
        name, domain = email.split('@')
        return ''.join(name.split('+')[0].split('.')) + '@' + domain
```