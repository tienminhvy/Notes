class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip();
        arr = s.split()
        lastWord = arr[-1];
        return len(lastWord);

s = Solution();
res = s.lengthOfLastWord("Hello World");
print(res)
res = s.lengthOfLastWord("   fly me   to   the moon  ");
print(res)
res = s.lengthOfLastWord("luffy is still joyboy");
print(res)