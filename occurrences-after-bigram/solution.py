class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        thirds = []
        for i in range(len(words) - 2):
            if words[i] == first:
                if words[i + 1] == second:
                   thirds.append(words[i + 2])
        return thirds 
