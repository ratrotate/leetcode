class Solution:

    def search(self, nums: List[int], target: int) -> int:
    
        low_border = 0
        high_border = len(nums)-1
        mid = (high_border + low_border) / 2

        while (nums[int(mid)] != target):
            if ((int(high_border) - int(low_border)) <= 1) and (nums[int(high_border)] != target) and (nums[int(low_border)] != target):
                return '-1'
            if nums[int(mid)] > target:
                high_border = int(mid)
            else:
                low_border = mid
            mid = (high_border + low_border) / 2
            
        return int(mid)
