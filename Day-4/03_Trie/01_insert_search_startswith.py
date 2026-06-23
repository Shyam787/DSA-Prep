class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

def insert(root, word):
    node = root

    for ch in word:

        if ch not in node.children:
            node.children[ch] = TrieNode()

        node = node.children[ch]
    
    node.isEnd = True


def search(root, word):
    node = root

    for ch in word:

        if ch not in node.children:
            return False

        node = node.children[ch]
    
    return node.isEnd

def startsWith(root, prefix):
    node = root

    for ch in prefix:

        if ch not in node.children:
            return False
        
        node = node.children[ch]

    return True   

root = TrieNode()

# Insert words
insert(root, "apple")
insert(root, "app")
insert(root, "bat")

# Search tests
print("Search apple:", search(root, "apple"))
print("Search app:", search(root, "app"))
print("Search appl:", search(root, "appl"))

# Prefix tests
print("StartsWith app:", startsWith(root, "app"))
print("StartsWith ba:", startsWith(root, "ba"))
print("StartsWith cat:", startsWith(root, "cat"))