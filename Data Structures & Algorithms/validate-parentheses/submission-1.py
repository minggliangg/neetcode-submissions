class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []

        for bracket in s:
            if bracket == "[" or bracket == "(" or bracket == "{":
                tracker.append(bracket)
            else:
                if not tracker:
                    return False
                opening_bracket = tracker.pop()
                if opening_bracket == "[" and bracket == "]":
                    continue
                if opening_bracket == "(" and bracket == ")":
                    continue
                if opening_bracket == "{" and bracket == "}":
                    continue
                return False

        return not tracker
