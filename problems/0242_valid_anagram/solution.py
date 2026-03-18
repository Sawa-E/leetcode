"""
LeetCode 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


# --- テスト ---
if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False
    assert sol.isAnagram("a", "a") == True
    assert sol.isAnagram("ab", "a") == False
    print("All tests passed!")
