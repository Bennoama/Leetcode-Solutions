class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = 'qwertyuiop'
        secondRow = 'asdfghjkl'
        thirdRow = 'zxcvbnm'

        oneLineWords = []

        for word in words:
            occurences = [0, 0, 0]
            for c in word.lower():
                if c in firstRow:
                    occurences[0] += 1
                elif c in secondRow:
                    occurences[1] += 1
                elif c in thirdRow:
                    occurences[2] += 1
            if occurences.count(0) == 2:
                oneLineWords.append(word)
        
        return oneLineWords
