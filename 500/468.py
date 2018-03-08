class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_ipv4(ip):
            sub = ip.split('.')
            for s in sub:
                if not s.isdigit() or (len(s) != len(str(int(s)))) or not (0 <= int(s) <= 255) :
                    return False
            return len(sub) == 4
        
        def is_ipv6(ip):
            sub = ip.split(':')
            for s in sub:
                if len(s) > 4 or not ('0' <= s.upper() <= 'FFFF'):
                    return False
            return len(sub) == 8
        
        if is_ipv4(IP):
            return 'IPv4'
        if is_ipv6(IP):
            return 'IPv6'
        return 'Neither'
