class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        paranthMap = {")":"(" , "]" : "[" , "}": "{"}
        for c in s:
            if c in paranthMap:
                if stack and stack[-1] == paranthMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
