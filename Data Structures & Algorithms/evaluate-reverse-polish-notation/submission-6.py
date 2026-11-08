class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if not stack:
                stack.append(token)
            if token == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(b+a))
            
            elif token == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(b-a))
            
            elif token == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(b*a))
            
            elif token == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(int(b/a)))

            else:
                stack.append(token)
        return int(stack[-1])