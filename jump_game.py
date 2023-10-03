from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0
    
        for i in range(len(nums)):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
            if max_reach >= len(nums) - 1:
                return True
        
        return True


a = Solution()

print(a.canJump([2, 3, 0, 0, 0, 0]))
print(a.canJump([2, 3, 1, 1, 4]))
print(a.canJump([4,0,4,2,2,0,1,3,3,0,3]))
