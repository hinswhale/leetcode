"""
无重复字符的最长子串
中等
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

### my solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        d = {}
        max_length = 0
        start = 0
        end = 0 
        for i, v in enumerate(s):
            if v in d and d[v] >= start:
                max_length = max(max_length, end - start)
                end = i + 1
                start = d[v] + 1
            d[v] = i
            end  = i + 1
        return max(max_length, end - start)

###### solution from leetcode amazing
class Solution0:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        ans = 0
        start = 0

        for i, v in enumerate(s):
            if m.get(v, 0)!= 0:
                start = max(m[v], start)
            m[v] = i + 1
            ans = max(i-start+1, ans)
        return ans

### Solution1 length
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_length = 0
        length = 0
        for k, v in enumerate(s):
            if v not in d:
                d[v] = k
                length += 1
            else:
                max_length = max(max_length, length)
                length = min(k - d[v], length + 1)
                d[v] = k
        return max(max_length, length)
 
 
