class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = int((high+low)/2)
        if target == nums[high]:
            return high
        if target > nums[high]:
            return high+1
        if target <= nums[low]:
            return low

        while (high > mid) or (mid > low):
            if ((nums[mid] < target) and (nums[mid+1] > target)):
                return mid+1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid
                mid = int((high+low)/2)
            else:
                high = mid
                mid = int((high+low)/2)
