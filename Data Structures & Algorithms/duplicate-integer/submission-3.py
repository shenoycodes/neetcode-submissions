from typing import Optional
class Solution:
    def hasDuplicate(self, nums: List[int])->bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True      # or x
            seen.add(x)
        return False