class Solution:
    def isValid(self, s: str) -> bool:

        # Input validation
        if not s:
            return False

        par_stack = []
        index = 0

        for c in s:

            peek = None

            if len(par_stack) > 0:
                peek = par_stack[-1]

            if c in ('(', '[', '{'):
                par_stack.append(c)
            elif (c == ')' and peek == '(') or (c == ']' and peek == '[') or (c == '}' and peek == '{'):
                par_stack.pop()
            else:
                return False
            
            index += 1

        if len(par_stack) > 0:
            return False
        else:
            return True

        