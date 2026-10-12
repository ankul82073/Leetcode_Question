class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 30
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    bit_counts[i] += 1
        
        arr = [0] * len(nums)
        for i in range(30):
            count = bit_counts[i]
            for j in range(count):
                arr[j] |= (1 << i)
        
        arr.sort(reverse=True)
        
        mod = 10**9 + 7
        total_sum = 0
        for i in range(k):
            total_sum = (total_sum + arr[i] * arr[i]) % mod
            
        return total_sum