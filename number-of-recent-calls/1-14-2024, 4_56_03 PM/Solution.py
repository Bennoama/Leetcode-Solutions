// https://leetcode.com/problems/number-of-recent-calls

class RecentCounter:

    def __init__(self):
        self.lastPings = []

    def ping(self, t: int) -> int:
        count = 0
        self.lastPings.append(t)
        for ping in self.lastPings:
            if (ping + 3000 >= t):
                count += 1
        return count

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)