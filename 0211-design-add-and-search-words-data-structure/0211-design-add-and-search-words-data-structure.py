class TrieNode:
    def __init__(self):
        # Initialize a dictionary to store child nodes and a flag for complete words
        self.childNodes = {}
        self.isCompleteWord = False

class WordDictionary:

    def __init__(self):
        # Initialize the root node of the Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root

        # Traverse the Trie to add each character of the word
        for ch in word:
            node = currNode.childNodes.get(ch, TrieNode())
            currNode.childNodes[ch] = node
            currNode = node

        # Mark the last node as a complete word
        currNode.isCompleteWord = True

    def search(self, word: str) -> bool:

        def customSearch(node, idx):
            # Recursive function to search for a word in the Trie

            # If we have reached the end of the word, check if the current node is a complete word
            if idx == len(word):
                return node.isCompleteWord

            # If the current character is '.', iterate through all child nodes
            if word[idx] == '.':
                for child in node.childNodes.values():
                    if customSearch(child, idx + 1):
                        return True

            # If the current character is a specific letter, traverse to the corresponding child node
            if word[idx] in node.childNodes:
                return customSearch(node.childNodes[word[idx]], idx + 1)

        # Start the search from the root node
        return customSearch(self.root, 0)

# Time complexity: O(M), where M is the length of the word being searched
# Space complexity: O(N), where N is the total number of characters in all words added to the Trie
