class Node:
    def __init__(self, isWord=False):
        self.children = [False] * 26
        self.isWord = isWord


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie
        for c in word:
            index = ord(c) - 97
            if not root.children[index]:
                root.children[index] = Node()
            root = root.children[index]
        root.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.trie
        for c in word:
            index = ord(c) - 97
            if not root.children[index]:
                return False
            root = root.children[index]

        if not root.isWord:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie
        for c in prefix:
            index = ord(c) - 97
            if not root.children[index]:
                return False
            root = root.children[index]

        return True


from collections import defaultdict


class Node:
    def __init__(self, isWord=False):
        self.children = defaultdict(Node)
        self.isWord = isWord


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie
        for c in word:
            index = ord(c) - 97
            if index not in root.children:
                root.children[index] = Node()
            root = root.children[index]
        root.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.trie
        for c in word:
            index = ord(c) - 97
            if index not in root.children:
                return False
            root = root.children[index]

        if not root.isWord:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie
        for c in prefix:
            index = ord(c) - 97
            if index not in root.children:
                return False
            root = root.children[index]

        return True