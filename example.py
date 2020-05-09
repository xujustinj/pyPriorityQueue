from priority_queue import PriorityQueue as PQ

# larger values have higher priority
pq = PQ((lambda x, y: x > y), 5, 11, 8, 10)
print(pq.count())   # 4     pq: 11 10 8 5
print(pq.dequeue()) # 11    pq: 10 8 5
print(pq.front)     # 10    pq: 10 8 5
pq.front = 5        #       pq: 8 5 5
print(pq.dequeue()) # 8     pq: 5 5
pq.enqueue(-1)      #       pq: 5 5 -1
print(pq.front)     # 5     pq: 5 5 -1
print(pq.count())   # 3     pq: 5 5 -1
print(pq.dequeue()) # 5     pq: 5 -1
print(pq.dequeue()) # 5     pq: -1
print(pq.front)     # -1    pq: -1
pq.front = 6        #       pq: 6
print(pq.dequeue()) # 6     pq: (empty)
print(pq.front)     # None  pq: (empty)
pq.front = 6        #       pq: (empty)
print(pq.count())   # 0     pq: (empty)
pq.enqueue("Hello") #       pq: Hello
pq.enqueue("World") #       pq: World Hello
pq.enqueue("!")     #       pq: World Hello !
print(pq.dequeue()) # World pq: Hello !
print(pq.dequeue()) # Hello pq: !
print(pq.dequeue()) # !     pq: (empty)
print(pq.dequeue()) # None  pq: (empty)

print()

# smaller values have higher priority
pq = PQ((lambda x, y: x < y), 5, 11, 8, 10)
print(pq.count())   # 4         pq: 5 8 10 11
print(pq.dequeue()) # 5         pq: 8 10 11
print(pq.front)     # 8         pq: 8 10 11
pq.front = 5        #           pq: 5 10 11
print(pq.dequeue()) # 5         pq: 10 11
pq.enqueue(-1)      #           pq: -1 10 11
print(pq.front)     # -1        pq: -1 10 11
print(pq.count())   # 3         pq: -1 10 11
print(pq.dequeue()) # -1        pq: 10 11
print(pq.dequeue()) # 10        pq: 11
print(pq.front)     # 11        pq: 11
pq.front = 6        #           pq: 6
print(pq.dequeue()) # 6         pq: (empty)
print(pq.front)     # None      pq: (empty)
pq.front = 6        #           pq: (empty)
print(pq.count())   # 0         pq: (empty)
pq.enqueue("Hello") #           pq: Hello
pq.enqueue("World") #           pq: Hello World
pq.enqueue("!")     #           pq: ! Hello World
print(pq.dequeue()) # !         pq: Hello World
print(pq.dequeue()) # Hello     pq: World
print(pq.dequeue()) # World     pq: (empty)
print(pq.dequeue()) # None      pq: (empty)

print()

# sorting by key
pq = PQ((lambda x, y: x[0] > y[0]), (42, "Hello"), (0, "World"), (-42, "!"))
print(pq.dequeue()[1])  # Hello
print(pq.dequeue()[1])  # World
print(pq.dequeue()[1])  # !