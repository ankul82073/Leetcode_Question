class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if not nums1:
            return True
        
        min_val = min(nums1)
        
        if min_val % 2 == 1:
            return True
            
        min_odd = min((x for x in nums1 if x % 2 == 1), default=float('inf'))
        
        for x in nums1:
            if x % 2 == 1:
                if x - min_odd < 1:
                    return False
                    
        return True