class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1;
        digits[i] += 1;
        while True:
            if i < -len(digits):
                break;
            if digits[i] >= 10:
                digits[i] = 0;
                try:
                    digits[i-1] += 1;
                except IndexError:
                    digits.insert(i-1, 1);
            else:
                break;
            i-=1;
        return digits;

s = Solution();
res = s.plusOne([1,2,3]);
print(res);
res = s.plusOne([9]);
print(res);
res = s.plusOne([4,9,9]);
print(res);