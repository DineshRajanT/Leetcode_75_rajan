class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.childNodes = {}
        # Flag to indicate if the current node represents a complete word
        self.isCompleteWord = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        Time Complexity: O(m), where m is the length of the word.
        Space Complexity: O(m), in the worst case when all characters in the word are unique.
        """
        currNode = self.root
        for ch in word:
            # Get the child node for the current character, or create a new one if it doesn't exist
            node = currNode.childNodes.get(ch, TrieNode())
            currNode.childNodes[ch] = node
            currNode = node  # Update current node to move to the next level
        currNode.isCompleteWord = True  # Mark the last node as representing a complete word

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.
        Time Complexity: O(m), where m is the length of the word.
        Space Complexity: O(1), as it does not use additional space proportional to the input.
        """
        currNode = self.root
        for ch in word:
            # Traverse through the Trie to find the word
            node = currNode.childNodes.get(ch)
            if not node:
                return False  # The word is not present if a character is missing
            currNode = node
        return currNode.isCompleteWord  # Check if the last node represents a complete word

    def startsWith(self, prefix: str) -> bool:
        """
        Check if there is any word in the Trie that starts with the given prefix.
        Time Complexity: O(m), where m is the length of the prefix.
        Space Complexity: O(1), as it does not use additional space proportional to the input.
        """
        currNode = self.root
        for ch in prefix:
            # Traverse through the Trie to find the prefix
            node = currNode.childNodes.get(ch)
            if not node:
                return False  # The prefix is not present if a character is missing
            currNode = node
        return True  # The Trie contains words with the given prefix
