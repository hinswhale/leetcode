5. 最长回文子串
https://leetcode.cn/problems/longest-palindromic-substring/description/
  
中等
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。


示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

# 竟然没修改，一次过了，纪念一下，🎉
###################################################################

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        max_substring = ''
        for i in range(length):
            max_substring = max(self.isPalindromic(s, i, i, length), self.isPalindromic(s, i, i + 1, length), max_substring, key=len)
        return max_substring
    
    def isPalindromic(self, s, left, right, length):
        while left >=0 and right < length and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
  
 ###################################################################
 https://segmentfault.com/a/1190000008484167

"""
若center的回文串最右侧是maxRight，j是i的对称点【"｜"处为maxRight位置】则
1. j 的回文串有一部分在 id 的之外， 则i的回文半径p[i] = maxRight - i
*｜--j--*=center=*--i--｜*
2. j 的回文串全部在 id 的里面，则p[i] = p[j], p[i]可否可越过maxRight 否，与p[j]的的回文串范围设定矛盾
｜=--j--==center==--i--=｜=
3. j 的回文串刚刚在 i的回文串左端重合，则p[i]可越过maxRight
｜---j---==center==---i---｜=

so, 1,2: P[i] 的值就等于 min(maxRight - i, P[j])
    3: i >= maxRight, 从 i 开始往两侧扩展，计算出 P[i] 的值 如果更新位置后大于maxRight, maxRight和center
  
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = '#'.join('^{}$'.format(s))
        n = len(s1)

        p = [0] * len(s1)
        maxRight = 0
        center = 0

        for i in range(1, n - 1):
            if i < maxRight:
                p[i] = min(p[2 * center - i], maxRight - i)

            while s1[i - p[i] - 1] == s1[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > maxRight:
                center = i
                maxRight = i + p[i]
        max_len, center_idx = max((p[i], i) for i in range(1, n - 1))
        print(max_len, center_idx )
        start = (center_idx - max_len) // 2
        return s[start: start + max_len]

###################################################################      
      
## leetcode上找的其他解法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(i - len(res)-1 , 0)
            temp = s[start : i +1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
 
###################################################################

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen = len(s)
        # if length of string < 2 or s is palindrome already
        if strlen < 2 or s == s[::-1]:
            return s

        start, maxlen = 0, 1

        for i in range(strlen):
            oddstart  = i - maxlen - 1
            evenstart = i - maxlen
            odd  = s[oddstart:i+1]  # len(odd)  = maxlen + 2
            even = s[evenstart:i+1] # len(even) = maxlen + 1
                #i = 2
                #maxlen = 1
                #start = 0
                #odd = s[2-1-1:3]….bab
                #even = s[1:3]…ab
            if oddstart >= 0 and odd == odd[::-1]:
                start = oddstart
                maxlen += 2
            elif evenstart >= 0 and even == even[::-1]:
                start = evenstart
                maxlen += 1
        return s[start:start+maxlen]

 ###################################################################      
# 这个时间太长了。。。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :param s: str
        :return: str
          a b c b
        a 1 0 0 0
        b   1 0 1
        c     1 0
        b       1
        """
        dp = [[False for col in range(len(s))] for row in range(len(s))]
        length = 0
        max_length = 0
        start = 0
        end = 0
        while length < len(s):
            i = 0
            while i + length < len(s):
                j = i + length
                if length == 1 or length == 0:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and max_length < length + 1:
                    max_length = length + 1
                    start = i
                    end = j
                i += 1
            length += 1

        return s[start:end+1]

###################################################################

class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2
    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]
