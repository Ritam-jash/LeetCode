"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Assume the first string is the prefix to start
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Update the prefix until it matches the start of each string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
        