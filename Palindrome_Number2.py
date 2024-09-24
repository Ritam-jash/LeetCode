""" Given an integer x, return true if x is a 
palindrome and false otherwise. """

class solution(object):
    def isPalindrome(self, x):
        return str(x) == ''.join(reversed(str(x)))
    



# Try another way
class solution(object):
    def isPalindrome(self, x):
        new_num = str(x)
        if new_num == new_num[::-1]:
            return True
        else:
            return False