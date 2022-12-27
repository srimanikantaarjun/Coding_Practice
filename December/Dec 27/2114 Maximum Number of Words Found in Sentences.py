"""
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = []
        for sent in sentences:
            max_words.append(len(sent.split()))
        return max(max_words)


# A more pythonic solution and is O(1) space

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_count = 0
        temp = 0
        
        for i in sentences:
            temp = len(i.split())
            if temp>max_count:
                max_count = temp
            temp=0
                
        return max_count
        
