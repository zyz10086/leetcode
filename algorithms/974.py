#给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

class Solution(object):
    def subarraysDivByK1(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count = 0
        for i in range(len(A)):
            sum = A[i]
            if(sum%K==0):
                count+=1
            for j in range(i+1,len(A)):
                sum += A[j]
                if(sum%K == 0 ):
                    count+=1
        return count
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count_map = {}
        sum = 0
        count = 0 
        for i in range(len(A)):
            sum += A[i]
            es = sum%K
            if(es not in count_map):
                count_map[es] = 1
            else:
                count_map[es] += 1
        for i in count_map.keys():
            if(count_map[i]>1):
                count +=self.plzh(count_map[i])
            if(i==0):
                count += count_map[i]
        return count
    # 排列组合
    def plzh(self,down):
        if(down==3):
            return 3
        x = 1
        while(x<2):
            down *= (down-x)
            x += 1
        return down/2

s = Solution()
print(s.subarraysDivByK([10,-10,-10,10,-7,-8,-6,6,9,-10],5))