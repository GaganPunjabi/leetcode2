class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        cache = {}
        word_cache = set(words)
        res = 0

        def dfs(word):
            nonlocal cache, word_cache
            max_len = 1

            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in word_cache:
                    if predecessor not in cache:
                        cache[predecessor] = dfs(predecessor) + 1
                    max_len = max(max_len, cache[predecessor])
            return max_len

        for i in range(len(words)):
            res = max(res, dfs(words[i]))
        return res

        
                
                        


