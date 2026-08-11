class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
                if c == '+':
                    stack.append(stack.pop()+stack.pop())
                elif c == '-':
                    a = stack.pop()
                    b = stack.pop()
                    result = b-a
                    stack.append(result)
                elif c == '*':
                    result = stack.pop()*stack.pop()
                    stack.append(result)
                elif c == '/':
                    a = stack.pop()
                    b = stack.pop()
                    result = int(b/a)
                    stack.append(result)
                else:
                    stack.append(int(c))
        return stack[0]

        