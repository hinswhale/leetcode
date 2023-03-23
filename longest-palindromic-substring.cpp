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
  
###################################################################
#  Manacher算法 from ChatCPT
class Solution {
public:
    string longestPalindrome(string s) {
        string new_s = "^#";
        for (const char &c: s) {
            new_s += c;
            new_s += "#";
        }
        new_s += "$";
        int n = new_s.size();

        vector<int> v(n, 0);
        int center = 0, maxRight = 0;
        for (int i = 1; i < n; i++) {
            if (i < maxRight) {
                v[i] = min(v[2 * center - i], maxRight - i);
            }
            while (new_s[i + v[i] + 1] == new_s[i - v[i] - 1]) {
                v[i]++;
            }
            if (i + v[i] > maxRight) {
                center = i;
                maxRight = i + v[i];
            }
        }
        int max_len = 0, idx = 0;
        for (int i = 1; i < n; i++) {
            if (v[i] > max_len) {
                max_len = v[i];
                idx = i;
            }
        }

        idx = (idx - max_len) / 2;
        return s.substr(idx, max_len);
    }
};
 

###################################################################

class Solution {
public:
    int Palindrome(int left, int right, string s){
        while(left >=0 && right < s.size() && s[left] == s[right]){
            left--;
            right++;
        }
        return right - left -1;
         
    }

    string longestPalindrome(string s) {
        int n = s.size();
        string ans = "";
        int max_len = 0;
        for(int i=0 ; i < n; i++){
            int len = max(Palindrome(i, i+1, s), Palindrome(i-1, i+1, s));
            if (len > max_len) {
                max_len = len;
                ans = s.substr(i - (max_len - 1) / 2, max_len);
            }
        }
        return ans;
        
    }
};

###################################################################

class Solution {
public:
    string longestPalindrome(string s) {
        string res;
        int n = s.size();
        for(int i=0; i<n; i++){
            int l = i - 1, r = i + 1;
            while(l >= 0 && r < s.size() && s[l] == s[r])  l--, r++;
            if(res.size() < r - l - 1) res = s.substr(l + 1, r - l - 1);

            l = i, r = i + 1;
            while(l >= 0 && r < s.size() && s[l] == s[r]) l --, r ++;
            if(res.size() < r - l - 1) res = s.substr(l + 1, r - l - 1);
                      
        }

        return res;
    }
};
