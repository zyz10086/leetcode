# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(not nums):
            return 0 
        pre = []
        que_val = nums[0]
        if( len(nums) ==1 ):
            return 1 if que_val == k else 0 
        count = 0
        for i in range(1,len(nums)):
            num = nums[i]
            if( num == k):
                count += 1
            if ( num > k):
                que_val = 
            recude_sum = que_val + num
            if( recude_sum >= k):
                while(len(pre) and que_val+num>k):
                    que_val -= pre.pop()
                size = len(pre)
                if(que_val==k):
                    count+=1
                    while( size>0 ):
                        if(pre[size]==0):
                            count += 1
                            size -= 1
                        else:
                            break
                pre.insert(0,num)
                
            else:
                que_val += num
                pre.insert(0,num)
        return count 

s = Solution()
print(s.subarraySum([100,1,2,3,0,6],6))
