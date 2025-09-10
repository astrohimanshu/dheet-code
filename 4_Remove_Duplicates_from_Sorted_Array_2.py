class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        for i in range(len(nums)):
            if p < 2:
                p += 1
            else:
                if nums[i] != nums[p - 2]:
                    nums[p] = nums[i]
                    p += 1
                else:
                    continue
        return p
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        for num in nums:
            if p < 2 or num != nums[p - 2]:
                nums[p] = num
                p += 1
        return p
                    
if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    p = solution.removeDuplicates(nums)
    print(nums)
    print(p)

    