"""
LeetCode 242. Valid Anagram
別解：ソート
時間 O(n log n), 空間 O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# --- テスト ---
if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False
    assert sol.isAnagram("a", "a") == True
    assert sol.isAnagram("ab", "a") == False
    print("All tests passed!")
