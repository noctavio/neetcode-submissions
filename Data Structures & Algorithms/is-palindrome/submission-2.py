class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a palindrome is a string that can be reversed and will result in the same sequence of chars
        # case in-sensitive means lower/capital does not matter, treat them as if they're the same
            # We must ignore anything not (A-Z, a-z, or 0-9)

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

    def alphaNumeric(self, c: str) -> bool:
        # we can use the ord() to return the ASCII value of a character
        # we need 3 ranges of ASCII values to check if our character is in that range

        return (
            ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
        )
