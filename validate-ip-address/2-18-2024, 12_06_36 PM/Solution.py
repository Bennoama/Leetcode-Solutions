// https://leetcode.com/problems/validate-ip-address

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        parts = queryIP.split('.')
        if len(parts) == 4:
            return self.validV4(parts)
        parts = queryIP.split(':')
        if len(parts) == 8:
            return self.validV6(parts)
        return "Neither"

    def validV4(self, ipParts) -> bool:
        for part in ipParts:
            if not part.isdigit():
                return "Neither"
            if int(part) > 255:
                return "Neither"
            if len(part) > 1 and int(part[0]) == 0:
                return "Neither"
        return "IPv4"

    def validV6(self, ipParts) -> bool:
        for part in ipParts:
            if (len(part) < 1 or len(part) > 4):
                return "Neither"
            if not self.isHexa(part):
                return "Neither"
        return "IPv6"
    
    def isHexa(self, string:str) -> bool:
        hexaCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        for c in string:
            if c.lower() not in hexaCharacters:
                return False
        return True