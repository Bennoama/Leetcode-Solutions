class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        characters = [*s]
        while (i < j):
            if (characters[i] in vowels and characters[j] in vowels):
                characters[i], characters[j] = characters[j], characters[i]
                i += 1
                j -= 1
            elif characters[i] in vowels:
                j -= 1
            else:
                i += 1
        return ''.join(characters)
