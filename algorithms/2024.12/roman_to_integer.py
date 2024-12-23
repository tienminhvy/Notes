class Solution(object):
    def getValue(self, c):
            if c == "I":
                return 1;
            if c == "V":
                return 5;
            if c == "X":
                return 10;
            if c == "L":
                return 50;
            if c == "C":
                return 100;
            if c == "D":
                return 500
            if c == "M":
                return 1000;

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = None;
        value = 0;
        for c in reversed(s):
            if prev is not None and c != prev:
                if c == "I" or c == "X" or c == "C":
                    if self.getValue(c) < self.getValue(prev):
                        value -= self.getValue(c);
                        prev = c
                        continue;
            value += self.getValue(c);
            prev = c;
        return value;

s = Solution();
result = s.romanToInt("MCMXCIV");
print(result);