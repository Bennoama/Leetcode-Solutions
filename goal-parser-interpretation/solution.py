class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ""
        while i < len(command):
            match command[i]:
                case "G":
                    res += "G"
                    i += 1
                    
                case "(":
                    if command[i + 1] == ")":
                        res += 'o'
                        i += 2
                    else:
                        res += "al"
                        i += 4
                    
        return res
