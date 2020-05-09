class PriorityQueue():

    def __init__(self, compare, *args):
        self._compare = compare
        self._heap = [item for item in args]
        self._heapify()


    # Index-related methods

    @staticmethod
    def _parent(index):
        return (index - 1) // 2
    @staticmethod
    def _left_child(index):
        return index * 2 + 1
    @staticmethod
    def _right_child(index):
        return index * 2 + 2

    def _begin(self):
        return 0
    def _end(self):
        return len(self._heap)

    def _root(self):
        return self._begin()
    def _last(self):
        return self._end() - 1

    def _is_node(self, index):
        return index in range(self._begin(), self._end())
    def _is_root(self, index):
        return index == self._root()
    def _is_leaf(self, index):
        return not self._is_node(PriorityQueue._left_child(index))


    # Heap maintenance methods

    def _fix_up(self, index): # assumes _is_node(index)
        while not self._is_root(index):
            item = self._heap[index]
            parent = PriorityQueue._parent(index)
            if (self._compare(item, self._heap[parent])):
                self._heap[index] = self._heap[parent]
                self._heap[parent] = item
                index = parent
            else: break # the parent does not violate heap-order

    def _fix_down(self, index): # assumes _is_node(index)
        while True:
            item = self._heap[index]
            left_child = PriorityQueue._left_child(index)
            right_child = PriorityQueue._right_child(index)
            if (self._is_node(right_child)): # both children exist
                if (self._compare(self._heap[left_child], self._heap[right_child])):
                    if (self._compare(self._heap[left_child], item)):
                        self._heap[index] = self._heap[left_child]
                        self._heap[left_child] = item
                        index = left_child
                        continue
                else:
                    if (self._compare(self._heap[right_child], item)):
                        self._heap[index] = self._heap[right_child]
                        self._heap[right_child] = item
                        index = right_child
                        continue
            elif (self._is_node(left_child) and self._compare(self._heap[left_child], item)): # only left child exists
                self._heap[index] = self._heap[left_child]
                self._heap[left_child] = item
                return # the left child is a leaf, no need to continue
            return

    def _heapify(self):
        for index in reversed(range(self._root(), PriorityQueue._parent(self._last()) + 1)):
            self._fix_down(index)


    # Public interface

    def count(self):
        return len(self._heap)

    @property
    def front(self):
        return self._heap[self._root()] if self.count() > 0 else None
    @front.setter
    def front(self, value):
        if self.count() > 0:
            self._heap[self._root()] = value
            self._fix_down(self._root())

    def dequeue(self):
        _front = self.front
        if self.count() > 1:
            self._heap[self._root()] = self._heap.pop()
            self._fix_down(self._root())
        elif self.count() == 1:
            self._heap.clear()
        return _front

    def enqueue(self, item):
        index = self._end()
        self._heap.append(item)
        self._fix_up(index)
