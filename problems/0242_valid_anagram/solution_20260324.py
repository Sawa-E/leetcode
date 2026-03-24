"""
LeetCode 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""

import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == len(t)):
            ls = list(s)
            lt = list(t)
            ls_c = collections.Counter(ls)
            ls_t = collections.Counter(lt)
            if (ls_c == ls_t):
                return True
            else:
                return False
        else:
            return False

# --- テスト ---
if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False
    assert sol.isAnagram("a", "a") == True
    assert sol.isAnagram("ab", "a") == False
    print("All tests passed!")
