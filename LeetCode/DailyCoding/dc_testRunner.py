from dc_5_67_LRUCache import LRUCache

lruCach = LRUCache(3)

lruCach.set('a', 10)
lruCach.set('b', 20)
lruCach.set('c', 30)


lruCach.printList()
print("------------")

lruCach.get('b')
lruCach.printList()