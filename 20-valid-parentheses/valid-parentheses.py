from collections import deque

valid_paran = {')':'(' ,'}':'{', ']':'['}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if ch in ['(','{', '[']:
                stack.append(ch)
            elif ch in [')','}',']']:
                if not stack or stack.pop() != valid_paran[ch]:
                    return False
        return True if len(stack) == 0 else False
                