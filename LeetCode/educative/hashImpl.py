class HashEntry:
    def __init__(self, key, data):
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.next = None


threshold = 0.6


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by deafult all None)
        self.bucket = [None] * self.slots

    # Hepler Functions
    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.get_size() == 0

    # Hash Function
    def getIndex(self, key):
        # hash is a built in function in Python
        hashCode = hash(key)
        index = hashCode % self.slots
        return index

    # Return a value for a given key
    def search(self, key):
        # Find the node with the given key
        b_Index = self.getIndex(key)
        head = self.bucket[b_Index]

        # Search key in the slots
        if head != None:
            while (head != None):
                if (head.key == key):
                    return head.value
            head = head.next
        # If key not found
        else:
            return None

    def insert(self, key, value):
        # Find the node with the given key
        b_Index = self.getIndex(key)
        if self.bucket[b_Index] == None:
            self.bucket[b_Index] = HashEntry(key, value)
        else:
            head = self.bucket[b_Index]
            while head != None:
                if head.key == key:
                    head.value = value
                    break
                elif head.next == None:
                    head.next = HashEntry(key, value)
                    break
                head = head.next
        self.size += 1
        load_factor = float(self.size) / float(self.slots)
        # Checks if 60% of the entries in table are filled, threshold = 0.6
        if load_factor >= threshold:
            self.resize()

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for i in range(0, len(self.bucket)):
            head = self.bucket[i]
            while head != None:
                new_index = self.getIndex(head.key)
                if new_bucket[new_index] == None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node != None:
                        if node.key == head.key:
                            node.value = head.value
                            node = None
                        elif node.next == None:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                        head = head.next
        self.bucket = new_bucket
        self.slots = new_slots

    # Remove a value based on a key
    def delete(self, key):
        # Find index
        b_Index = self.getIndex(key)
        head = self.bucket[b_Index]

        # First key in the bucket
        if (head.key == key):
            self.bucket[b_Index] = head.next
            self.size -= 1
            print(str(key) + " deleted!")
            return self

        # Find the key in slots
        prev = head
        head = head.next
        while (head != None):
            # If key exists
            if (head.key == key):
                # Remove key
                prev.next = head.next
                # Decrease size
                self.size -= 1
                print(str(key) + " deleted!")
                return self
            # Else keep moving in chain
            prev = prev.next
            head = head.next

        # If key does not exist
        print("Key not found!")
        return None


table = HashTable()  # Create a HashTable
print(table.isEmpty())
table.insert("This", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Driver", 5)
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))