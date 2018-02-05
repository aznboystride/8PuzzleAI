class Heap:
    def __init__(self,root=None):
        self.lst = list([None])
        if root is not None:
            self.lst.append(root)
    def items(self):
        return list(map(lambda x: x.get_Heuristic(), self.lst[1:]))
    def empty(self):
        return len(self.lst) is 1
    def size(self):
        if self.empty():
            return 1
        else:
            return len(self.lst) - 1
    def pop(self):
        if self.empty():
            print('Heap is empty')
            return
        else:
            self.lst[1], self.lst[-1] = self.lst[-1], self.lst[1]
            deleted = self.lst[-1]
            del self.lst[-1]
            self.downheap(1)
        return deleted
    def front(self):
        if self.empty():
            print('Heap is empty')
        else:
            return self.lst[1]
    def push(self, item):
        self.lst.append(item)
        self.upheap(self.size())
    def upheap(self, i):
        if i <= 1:
            return
        else:
            try:
                if self.lst[i//2*2].get_Heuristic() <= self.lst[i//2*2+1].get_Heuristic():
                    if self.lst[i//2*2].get_Heuristic() < self.lst[i//2].get_Heuristic():
                        self.lst[i//2*2], self.lst[i//2] = self.lst[i//2], self.lst[i//2*2]
                else:
                    if self.lst[i//2*2+1].get_Heuristic() < self.lst[i//2].get_Heuristic():
                        self.lst[i//2*2+1], self.lst[i//2] = self.lst[i//2], self.lst[i//2*2+1]
                self.upheap(i//2)
            except:
                if self.lst[i].get_Heuristic() < self.lst[i//2].get_Heuristic():
                    self.lst[i], self.lst[i//2] = self.lst[i//2], self.lst[i]
                self.upheap(i//2)
    def downheap(self, i):
        try:
            try:
                if self.lst[i*2].get_Heuristic() <= self.lst[i*2+1].get_Heuristic():
                    if self.lst[i*2].get_Heuristic() < self.lst[i].get_Heuristic():
                        self.lst[i*2], self.lst[i] = self.lst[i], self.lst[i*2]
                    self.downheap(i*2)
                else:
                    if self.lst[i*2+1].get_Heuristic() < self.lst[i].get_Heuristic():
                        self.lst[i*2+1], self.lst[i] = self.lst[i], self.lst[i*2+1]
                    self.downheap(i*2+1)
            except:
                if self.lst[i*2].get_Heuristic() < self.lst[i].get_Heuristic():
                    self.lst[i*2], self.lst[i] = self.lst[i], self.lst[i*2]
                self.downheap(i*2)
        except:
            return
heaps = Heap()
