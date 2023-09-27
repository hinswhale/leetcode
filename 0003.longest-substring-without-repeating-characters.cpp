/*
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
*/

class Solution {
public:
int lengthOfLongestSubstring(string s) {
    vector<int> m(128, 0); //ASCII码范围：0-127
    int ans = 0;
    int i = 0;
    for (int j = 0; j < s.size(); j++) {
        if(m[s[j]]!=0)  
        i = max(i, m[s[j]]);
        
        m[s[j]] = j + 1;
        ans = max(ans, j - i + 1);
    }
    return ans;
}
};
