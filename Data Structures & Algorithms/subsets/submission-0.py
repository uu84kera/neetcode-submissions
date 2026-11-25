class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start):
            result.append(path.copy())

            for i in range(start, len(nums)):
                # pick
                path.append(nums[i])
                # explore
                backtrack(i+1)
                # undo
                path.pop()
        
        backtrack(0)
        return result