# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n)。
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        if not nums:
            return 0 
        nums_set = set(nums)
        max_len = 1
        for num in nums_set:
            if( num-1  in nums_set):
                continue
            else:
                tmp = num+1
                nums_dict[num] = 1
                while(tmp in nums_set):
                    nums_dict[num]+=1
                    if(nums_dict[num]>max_len):
                        max_len = nums_dict[num]
                    tmp += 1
        return max_len
s = Solution()
print(s.longestConsecutive([1,2,3,32,5,256,4]))
