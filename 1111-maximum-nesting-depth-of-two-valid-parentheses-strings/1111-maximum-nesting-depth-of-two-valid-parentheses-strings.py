class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                res.append(d % 2)
            else:
                res.append(d % 2)
                d -= 11
        return res
        