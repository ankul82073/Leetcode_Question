class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for ans, num in count.items():
            group_size = ans + 1
            res += math.ceil(num / group_size) * group_size
        return res