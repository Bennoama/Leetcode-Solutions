class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        myMap = {}
        i = 0
        for c in key:
            if c == ' ':
                continue
            if c not in myMap:
                myMap[c] = ord('a') + i
                i += 1
        decoded = ''
        for c in message:
            if c in myMap:
                decoded += chr(myMap[c])
            else:
                decoded += c
        return decoded
