class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_palindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start >= len(s):
                res.append(part[:])
                return
            
            for end in range(start, len(s)):
                # אם תת-המחרוזת מ-start ועד end היא פלינדרום
                if is_palindrome(s, start, end):
                    part.append(s[start:end+1])
                    backtrack(end + 1)
                    part.pop()

        backtrack(0)
        return res