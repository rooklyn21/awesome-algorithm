class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        self.nums = nums
        self.target = target

        diff = []
        for i in range(0, len(nums)):
            diff.append(target - nums[i])

        # print(nums)
        # print(diff)

        for i in range(0, len(nums)):
            for j in range(i+1,len(diff)):
                try:
                    k=diff[j:].index(nums[i])
                    # print([i,j+k])
                    return([i,j+k])
                except Exception as e:
                    # print(e)
                    break

if __name__=="__main__":
    Solution().twoSum([1,3,2,4,9,11],6)