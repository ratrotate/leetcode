class Solution:
    def isPalindrome(self, x: int) -> bool:
        counter = 0
        buff = x

        if x < 0:
            return False
        while x > 0:
            counter = counter * 10 + x % 10
            x //= 10
        print(counter, buff)
        if counter == buff:
            return True
