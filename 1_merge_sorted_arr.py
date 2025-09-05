class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        k = m + n - 1

        while p1 >= 0 and p2 >= 0 :
            if nums2[p2] > nums1[p1]:
                nums1[k] = nums2[p2]
            else:
                nums1[k] = nums1[p1]
            k = k - 1

        while p2 >= 0:
            nums1[k] = nums2[p2]
            p2 = p2 - 1
            k = k - 1


if __name__ == '__main__':
    solution = Solution()
    a = [0,0]
    m = 0
    b = [1,2]
    n = 2
    solution.merge(a,m,b,n)
    print(a)