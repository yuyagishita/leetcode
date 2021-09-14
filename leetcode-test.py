import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums = collections.Counter(nums)
        for k, v in count_nums.items():
            if v >= len(nums) / 2:
                return k
        return 0


h = Solution()
print(h.majorityElement([3, 2, 3]))
