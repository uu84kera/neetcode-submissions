class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        for ch in s:
            if ch in parentheses:
                stack.append(ch)

            else:
                if not stack:
                    return False
                
                cur = stack.pop()
                if ch != parentheses[cur]:
                    return False
        
        return not stack