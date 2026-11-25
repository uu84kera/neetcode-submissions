class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        n = len(s)

        # Palindrome Checking
        def isPalindrome(left, right):
            while left<right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        
        def backtrack(i):
            if i == n:
                result.append(path.copy())
                return
            
            # Palindrome Partitioning
            for j in range(i, n):
                if isPalindrome(i,j):
                    # pick
                    path.append(s[i:j+1])

                    # explore
                    backtrack(j+1)

                    # undo
                    path.pop()
        backtrack(0)
        return result
