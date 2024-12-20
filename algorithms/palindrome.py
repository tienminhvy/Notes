class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False;
        if x >= 0:
            if x == 0:
                return True;
            result = str()
            temp = x;
            while(temp != 0):
                result += str(temp % 10);
                temp = int(temp / 10);
            if len(result) == 0:
                return False;
            return int(result) == x;

solution = Solution()
res = solution.isPalindrome(1001);
print(res);