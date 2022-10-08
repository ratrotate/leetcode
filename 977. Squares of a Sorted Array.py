class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final_arr = []
        first_ind = 0
        last_ind = len(nums)-1

        while last_ind >= first_ind:
            if nums[last_ind]*nums[last_ind] > nums[first_ind]*nums[first_ind]:
                final_arr.insert(0, nums[last_ind]*nums[last_ind])
                last_ind -= 1
            else:
                final_arr.insert(0, nums[first_ind]*nums[first_ind])
                first_ind += 1
        return final_arr
