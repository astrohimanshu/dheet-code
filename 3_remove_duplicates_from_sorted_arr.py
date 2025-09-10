class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_element_index = 0
        scanner_for_unique_element = 1
        unique = 1
        size = len(nums)
        while scanner_for_unique_element < size and current_element_index < size:
            if nums[scanner_for_unique_element] != nums[current_element_index]:
                unique = unique + 1
                current_element_index = current_element_index + 1
                nums[current_element_index] = nums[scanner_for_unique_element]
                scanner_for_unique_element = scanner_for_unique_element + 1
            else:
                scanner_for_unique_element = scanner_for_unique_element + 1

        return unique
    

# less cluttered without while
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_index = 1
        for unique in range(1, len(nums)):
            if nums[unique_index - 1] != nums[unique]:
                nums[unique_index] = nums[unique]
                unique_index += 1
        return unique_index
    
class Solution3:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for num in nums:
            if k < 1:
                k += 1
            elif num != nums[k - 1]:
                nums[k] = num
                k += 1
        return k
class Solution4:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for num in nums:
            if k < 1 or num != nums[k - 1]:
                nums[k] = num
                k += 1
        return k


if __name__ == '__main__':
    solution = Solution4()
    nums = [0,0,1,1,1,2,2,3,3,4]
    a = solution.removeDuplicates(nums)
    print(a) 
    print(nums)