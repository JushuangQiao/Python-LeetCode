class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        return len({self.simplifyEmail(email): True for email in emails})

    def simplifyEmail(self, email):
        name, domain = email.split('@')
        return ''.join(name.split('+')[0].split('.')) + '@' + domain
