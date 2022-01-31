from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums)

        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1

        print(nums)
        return


print(Solution().sortColors([2, 0, 1, 0, 2, 1]))