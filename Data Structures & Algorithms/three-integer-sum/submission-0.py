class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            # 1. 跳过重复的 nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    # 找到答案
                    result.append([nums[i], nums[left], nums[right]])

                    # 移动 pointers
                    left += 1
                    right -= 1
                    
                    # 跳过 duplicates
                    while left<right and nums[left]==nums[left-1]:
                        left += 1
                    while left<right and nums[right]==nums[right+1]:
                        right -= 1
        return result