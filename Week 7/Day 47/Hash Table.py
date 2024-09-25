# Hash Table implementation using Python dictionary

class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, "Key not found")

    def remove(self, key):
        if key in self.table:
            del self.table[key]
        else:
            print("Key not found")

    def display(self):
        print(self.table)

# Example usage
ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.get("name"))
ht.remove("age")
ht.display()
