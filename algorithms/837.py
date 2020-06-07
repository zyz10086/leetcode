class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        # f(x) = 0.1*f(x+1) + P(f(x))
        if(N-K>W):
            return 0
        if(K==0):
            return 1
        max_v = K-1
        d_v = N-K+1
        if(W<=N and K==1):
            return  d_v/W
        per_v = 1/W
        p_dict = {max_v: d_v/W}
        for i in range(max_v-1,-1,-1):
            i_p = 0 
            if(max_v-i<W):
                tmp = i
                while(max_v-tmp>0):
                    i_p += per_v*p_dict[tmp+1]
                    tmp += 1
                i_p += (W-max_v+i)*per_v * self.P(i,W,K,N,tmp-i)
            else:
                tmp = 0
                while(tmp<W):
                    i_p += per_v*p_dict[i+tmp+1]
                    tmp += 1
            p_dict[i] = i_p
        return p_dict[0]
    def P(self,v,W,K,N,tmp_i):
        val = v+W-K+1
        if v+W>=N:
            val = N-K+1
        return val/(W-tmp_i)

s = Solution()
print(s.new21Game(9811,8776,1096))