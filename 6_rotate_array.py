class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # copy last k elements in a separate array
        size = len(nums)
        k = k % size
        copy = [0] * k
        for i in range(k):
            copy[i] = nums[size - 1 - i]

        # shift all elements to right one time
        j = size - 1
        for i in range(size - k - 1, -1, -1):
            nums[j] = nums[i]
            j -= 1

        # copy first k elements back to array
        for i, j in enumerate(range(k - 1, -1 ,-1)):
            nums[j] = copy[i]


class Solution2: #optimized using cycles
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        g = gcd(n,k)
        for start in range(g):
            src = start
            copy_src = nums[src]
            while True:
                dest = (src + k) % n
                copy_dest = nums[dest]
                nums[dest] = copy_src
                copy_src = copy_dest

                src = dest
                if start == src:
                    break


class Solution3: #using extra list
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = n * [0]
        for i in range(n):
            print(f"{i} --> {(i + k)%n}")

        for i in range(n):
            temp[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = temp[i]

# wrong solution       
class Solution4: #optimized using cycles        # wrong solution
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        g = gcd(n,k)
        src_id = 0
        steps = int(n/g)
        src_cp = nums[src_id]

        for _ in range(steps):
            dest_id = (src_id + k) % n
            print(f"{src_id} --> {dest_id}")
            dest_cp = nums[dest_id]
            nums[dest_id] = src_cp

            src_id = dest_id
            src_cp = dest_cp

class Solution5: #using reversal trick thrice
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def reverse(start, end):
            while start < end:
                nums[start] , nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)



if __name__ == '__main__':
    nums = [-1,-100,3,99]
    #nums = [-1]
    k  = 2
    sol = Solution5()
    sol.rotate(nums, k)
    print(nums)