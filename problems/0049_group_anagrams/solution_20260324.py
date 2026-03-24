"""
LeetCode 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if (key in d):
                d[key].append(strs[i])
            else:
                d[key] = [strs[i]]
        return list(d.values())

# --- テスト ---
if __name__ == "__main__":
    sol = Solution()

    result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    result = [sorted(g) for g in result]
    result.sort()
    assert result == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]

    print("All tests passed!")
