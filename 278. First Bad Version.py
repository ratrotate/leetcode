class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n
        low = 0
        mid = (high + low) / 2

        while (isBadVersion(int(mid)) != True) or (isBadVersion(int(mid-1)) != False):
            if isBadVersion(int(mid)) == True:
                high = mid
                mid = (high + low) / 2
            if isBadVersion(int(mid)) == False:
                low = mid 
                mid = (high + low) / 2
        return int(mid)
