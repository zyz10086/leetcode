class Solution:
    def myPow1(self, x: float, n: int) -> float:
        flag = False if n < 0 else True
        n = abs(n)
        if(n == 0):
            return 1
        if(n == 1):
            return x if flag else 1/x
        val = []
        n_tmp = n
        while n_tmp > 0:
            val.append(n_tmp)
            n_tmp = int(n_tmp/2)
        val1 = [x, x, 0]
        val.reverse()
        i = 1
        while i < len(val):
            j = val[i]
            if(j % 2 == 0):
                val1[2] = val1[1]*val1[1]
            else:
                val1[2] = val1[1]*val1[1]*val1[0]
            val1[1] = val1[2]
            i += 1
        return val1[2] if flag else 1/val1[2]


    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        if(n==1):
            return x
        if(n<0):
            return  1/self.myPow(x,-n)
        if(n%2==0):
            return  self.myPow(x,int(n/2))*self.myPow(x,int(n/2))
        return self.myPow(x,int(n/2))*self.myPow(x,int(n/2))*x
s = Solution()
# print(s.myPow(0.00001,2147483647))
print(s.myPow(2,10))

