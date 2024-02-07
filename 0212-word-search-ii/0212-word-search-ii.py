class TrieNode:
    def __init__(self):
        # Each TrieNode has a dictionary to store its children nodes,
        # where the key is the character and the value is the corresponding TrieNode.
        self.children = {}
        # Boolean flag to indicate whether the current node represents the end of a word.
        self.isWord = False
    
    def addWord(self, word):
        # Method to add a word to the Trie.
        curr = self
        for ch in word:
            # Traverse the Trie, creating nodes as needed for each character in the word.
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        # Mark the last node as the end of a word.
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Initialize Trie and add words to it
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        # Depth-first search function
        def dfs(r, c, node, word):
            # Base cases for invalid positions or characters
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                board[r][c] not in node.children or (r, c) in visit):
                return

            # Mark current position as visited
            visit.add((r, c))
            # Add the current character to the current word
            word += board[r][c]
            # Move to the next node in the Trie
            node = node.children[board[r][c]]

            # Check if the current path forms a valid word
            if node.isWord:
                res.add(word)

            # Explore adjacent positions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack: remove the current position from visited set
            visit.remove((r, c))

        # Iterate through the board and initiate DFS from each cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
            
        # Convert set of valid words to list and return
        return list(res)

# Time Complexity: O(M * N * 4^L), where M and N are the dimensions of the board,
# and L is the maximum length of words. The 4^L factor comes from the number of
# directions (up, down, left, right) we explore in the DFS.
# Space Complexity: O(W * L), where W is the number of words and L is the average length
# of the words. This is the space used by the Trie.
