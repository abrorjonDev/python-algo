# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix: str = strs[0]
        for i in strs[1:]:
            common_prefix = self.find_common_prefix(common_prefix, i)

        return common_prefix

    def find_common_prefix(self, common_prefix: str, i: str) -> str:
        for j in range(len(common_prefix)):
            if j >= len(i) or common_prefix[j] != i[j]:
                return common_prefix[:j]
        return common_prefix


if __name__ == '__main__':
    a = Solution()

    assert a.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert a.longestCommonPrefix(["dog", "racecar", "car"]) == ""
