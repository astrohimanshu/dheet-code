class Solution1:
    def removeElement(self, nums: list[int], val: int) -> int:
        last_ptr = len(nums) - 1
        k = 0
        i = 0
        while i <= last_ptr:
            if nums[i] == val:
                k = k + 1
                # check for swap position available from last
                while last_ptr > i:
                    if val != nums[last_ptr]:
                        # swap
                        nums[last_ptr], nums[i] = nums[i], nums[last_ptr]
                        break
                    else: last_ptr -= 1       
            i = i + 1
        return len(nums) - k
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # pointer for placing non val elements
        place = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[place] = nums[i]
                place = place + 1
        return place
            
# note : solution1 keeps the elements same by swapping, solution (more efficient) keeps non val elements same
# however both has O(n) complexity

if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = sol.removeElement(nums, val)
    print(nums, k)
