# class Solution:
#     def isValid(self, s: str) -> bool:
#         tracker = []

#         for bracket in s:
#             if bracket == "[" or bracket == "(" or bracket == "{":
#                 tracker.append(bracket)
#             else:
#                 if not tracker:
#                     return False
#                 opening_bracket = tracker.pop()
#                 if opening_bracket == "[" and bracket == "]":
#                     continue
#                 if opening_bracket == "(" and bracket == ")":
#                     continue
#                 if opening_bracket == "{" and bracket == "}":
#                     continue
#                 return False

#         return not tracker

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:          # odd length can never be balanced
            return False

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs:                       # closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:                                 # opening bracket
                stack.append(ch)

        return not stack
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack
