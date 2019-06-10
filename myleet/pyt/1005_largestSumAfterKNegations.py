#思路：
# 先对list进行从小到大排序，求出负数的数量x，以及绝对值最小的数 absmin
# 如果k<=x，取前k个数进行反符号操作 结果=abs(sum(A[0]...A[k-1]))+sum(A[k]...A[len(A)])
# 如果k>x，且k-x是偶数，则abs(sum(A[0]...A[x-1]))+sum(A[x]...A[len(A)])
# k-x是奇数,abs(sum(A[0]...A[x-1]))+sum(A[x]...A[len(A)])-2absmin
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        