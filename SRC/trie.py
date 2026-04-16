class Node:
    def __init__(self):
        self.kids = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word.lower():
            if c not in cur.kids:
                cur.kids[c] = Node()
            cur = cur.kids[c]
        cur.end = True

    def autocomplete(self, prefix):
        cur = self.root
        for c in prefix.lower():
            if c not in cur.kids:
                return []
            cur = cur.kids[c]
        results = []
        self._find(cur, prefix, results)
        return results

    def _find(self, node, word, results):
        if node.end:
            results.append(word)
        for c, child in node.kids.items():
            self._find(child, word + c, results)