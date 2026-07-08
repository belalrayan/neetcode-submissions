class Node:
    def __init__(self,key):
        self.key=key
        self.ptrs={}
class PrefixTree:

    def __init__(self):
        self.head=Node(-1)
        

    def insert(self, word: str) -> None:
        node=self.head
        while len(word)>0:
            c=word[0]
            word=word[1:]
            node.ptrs[c]=node.ptrs.get(c,Node(c))
            node=node.ptrs[c]
        node.ptrs["$"]=Node("$")    



    def search(self, word: str) -> bool:
        node=self.head
        while len(word)>0:
            c=word[0]
            word=word[1:]
            if c not in node.ptrs:
                return False
            node=node.ptrs[c]
        if "$" in node.ptrs:
            return True

        return False             

        

    def startsWith(self, prefix: str) -> bool:
        node=self.head
        while len(prefix)>0:
            c=prefix[0]
            prefix=prefix[1:]
            if c not in node.ptrs:
                return False
            node=node.ptrs[c]
        return True    
        
        