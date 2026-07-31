class Solution:
    def isPalindrome(self, s: str) -> bool:
        # you are given a string s, you must return a boolean 
        # a palindrome is a string that reads the same forwards and backwards. 
            # AND is case-insensitive (a-z) 
            # It can be length 1-1000, and is made up of ASCII characters'

        # sol1. reverse the string using pythons built in string reversal and compare to 's'
            # this does not work since white-spaces are present the order is different and it doesn't  
            # ignore non-alphanumeric characters (ex. ?, !, $)
         
        # ord() in python returns the ASCII value of a character (if it has one)

        left = 0
        right = len(s) - 1 
        while left < right:
            while left < right and not self.alphaNumeric(s[left]):
                left += 1
            while right > left and not self.alphaNumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True

    # takes some input and checks if its ASCII value falls between 3 ranges
    def alphaNumeric(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

        