class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        g.sort()
        s.sort()
        for size in s:
            if (len(g) == 0):
                break
            minimumGreed = g[0]
            if size >= minimumGreed:
                content += 1
                g.remove(minimumGreed)
        return content
