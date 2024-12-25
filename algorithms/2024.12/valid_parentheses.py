class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c);
                continue;
            if len(stack) == 0 or pairs.get(c) != stack.pop():
                return False;
        if len(stack) > 0:
            return False;
        return True;

s = Solution()
res = s.isValid("()");
print(res);
res = s.isValid("()[]{}");
print(res);
res = s.isValid("(]");
print(res);
res = s.isValid("([])");
print(res);
res = s.isValid("(");
print(res);
res = s.isValid("([]");
print(res);
res = s.isValid(")");
print(res);
res = s.isValid("[]}");
print(res);