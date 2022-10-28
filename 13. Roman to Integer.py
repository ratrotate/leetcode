class Solution:
    def romanToInt(self, s: str) -> int:
        final_num = 0

        for ind in range(0, len(s)):
            if s[ind] == 'I':
                final_num += 1
                if (ind < len(s)-1):
                    if (s[ind+1] == 'V'):
                        final_num -= 2
                if (ind < len(s)-1):
                    if (s[ind+1] == 'X'):
                        final_num -= 2
            if s[ind] == 'V':
                final_num += 5
            if s[ind] == 'X':
                final_num += 10
                if (ind < len(s)-1):
                    if (s[ind+1] == 'L'):
                        final_num -= 20
                if (ind < len(s)-1):
                    if (s[ind+1] == 'C'):
                        final_num -= 20
            if s[ind] == 'L':
                final_num += 50
            if s[ind] == 'C':
                final_num += 100
                if (ind < len(s)-1):
                    if (s[ind+1] == 'D'):
                        final_num -= 200
                if (ind < len(s)-1):
                    if (s[ind+1] == 'M'):
                        final_num -= 200
            if s[ind] == 'D':
                final_num += 500
            if s[ind] == 'M':
                final_num += 1000

        return final_num
