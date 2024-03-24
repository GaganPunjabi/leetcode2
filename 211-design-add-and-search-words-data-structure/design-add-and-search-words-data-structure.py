class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.match = [self.root]

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.EOW = True

    def search(self, word: str) -> bool:
        
        def dfs(root, suffix):
            if not suffix and root.EOW:
                return True
            elif not suffix:
                return False
            elif suffix[0] == "." and root.children:
                for child in root.children.values():
                    if dfs(child, suffix[1:]):
                        return True
            elif suffix[0] in root.children.keys():
                return dfs(root.children[suffix[0]], suffix[1:])
            return False
        return dfs(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)