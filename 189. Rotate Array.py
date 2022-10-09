class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def rev(arr, l, r):            
            while l < r:
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
                l += 1
                r -= 1
        
        rev(nums, 0, len(nums)-1)
        print(nums)
        rev(nums, 0, (k%len(nums))-1)
        print(nums)
        rev(nums, k%len(nums), len(nums)-1)
        print(nums)
        
        
        """
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Using rotations
        1. reverse all elements in array
        2. reverse first k elements
        3. reverse last n-k elements
        [7,6,5,4,3,2,1]
        [5,6,7,4,3,2,1]
        [5,6,7,1,2,3,4]
        
        """
        
