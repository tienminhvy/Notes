class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = target;
        currI = 0;
        i = 1;
        while(i < len(nums)):
            if currI >= len(nums):
                break;
            if nums[i] == target - nums[currI]:
                nextI = i;
                break;
            if i+1 == len(nums):
                currI += 1;
                i = currI + 1;
                continue;
            i+=1;
        return [currI, nextI];

        

test = Solution();
# res1 = test.twoSum([2,7,11,15], 9);
# res2 = test.twoSum([3, 2, 4], 6);
# res3 = test.twoSum([3, 3], 6);
# res = test.twoSum([2,7,11,15], 9);
# print(res);
# res = test.twoSum([3,2,4], 6);
# print(res);
# res = test.twoSum([3,3], 6);
# print(res);
res = test.twoSum([6,9,3,4,2], 12);
print(res);
# res = test.twoSum([3, 2, 3], 6);
# print(res);