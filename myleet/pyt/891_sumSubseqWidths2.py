class Solution:
    def sumSubseqWidths(self,A):
        MOD = 10**9 + 7
        res, n = 0, len(A)
        A.sort()
        print(A)
        pow2=[1]
        for i in range(1,n):
            print(i,pow2)
            pow2.append(pow2[-1] * 2 % MOD )

        for i, x in enumerate(A):
            print(i, x, res)
            res -= x * pow2[n-1-i] % MOD
            res += x * pow2[i] % MOD

        return res % MOD


Solution().sumSubseqWidths([2,1,3,5,6,8,4,23,3,4,33,45,111])