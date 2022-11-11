from typing import List
# TODO: Bad time complexity. Probably should use a trie?

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words: List[str]):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        def is_word_partitionable(word: str, memo: List[str]):
            if word in memo:
                return True
                
            for w in memo:
                partitioned = word.partition(w)
                if partitioned[0] in memo or partitioned[2] in memo:
                    if (is_word_partitionable(partitioned[0],  memo) or len(partitioned[0]) == 0) and (is_word_partitionable(partitioned[2], memo) or len(partitioned[2]) == 0):
                        return True
                    
            return False

        words.sort(key = lambda x: len(x))
        seen_words = []
        approved_words = []
        
        for word in words:
            if is_word_partitionable(word, seen_words):
                approved_words.append(word)
            seen_words.append(word)
        
        return approved_words


        
s = Solution()
print(s.findAllConcatenatedWordsInADict(["a", "b", "ab", "abc"]))
print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
