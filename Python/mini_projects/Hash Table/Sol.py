from typing import Any, Optional


class HashTable:
    def __init__(self):
        self.collection: dict[int, dict[str, Any]] = {}

    def hash(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def add(self, key: str, value: Any) -> None:
        hashed_key = self.hash(key)
        
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
            
        self.collection[hashed_key][key] = value

    def remove(self, key: str) -> None:
        hashed_key = self.hash(key)
        
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
            
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    def lookup(self, key: str) -> Optional[Any]:
        hashed_key = self.hash(key)
        
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
            
        return None


if __name__ == "__main__":
    ht = HashTable()
    
    print(f"Hash for 'golf': {ht.hash('golf')}")  
    
    ht.add('golf', 'sport')
    print(f"Collection after adding golf: {ht.collection}")
    
    ht.add('fcc', 'coding')
    ht.add('cfc', 'chemical')
    print(f"Collection after adding fcc and cfc: {ht.collection}")
    
    print(f"Lookup 'golf': {ht.lookup('golf')}")  
    print(f"Lookup 'cfc': {ht.lookup('cfc')}")    
    print(f"Lookup 'fake': {ht.lookup('fake')}") 
    
    ht.remove('cfc')
    print(f"Collection after removing cfc: {ht.collection}")
    
    ht.remove('does_not_exist') 