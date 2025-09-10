class Solution:   # Time :O(N) Space: O(N)
    def majorityElement(self, nums: list[int]) -> int:
        unique_elements = {}
        cap = len(nums) // 2
        for num in nums:
            if num not in unique_elements.keys():
                unique_elements[num] = 1
                if unique_elements[num] > cap:
                    return num
            elif num in unique_elements.keys():
                unique_elements[num] += 1
                if unique_elements[num] > cap:
                    return num
                

class Solution_Efficient: # Time O(N)   Space O(1)
    def majorityElement(self, nums: list[int]) -> int:
        vote = 0
        major = nums[0]
        for num in nums:
            if vote == 0:
                major = num
            if num == major:
                vote += 1
            if num != major:
                vote -= 1
    
        return major


if __name__ == '__main__':
    solution = Solution_Efficient()
    nums = [1]*5000 + [2]*3000 + [1]*2001
    print(solution.majorityElement(nums))