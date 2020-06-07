class Solution:
    def sumNums(self, n: int) -> int:
        a = n>0 and ( n+=self.sumNums(n-1) )
        return n

