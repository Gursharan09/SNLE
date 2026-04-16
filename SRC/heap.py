class MinHeap:
    def __init__(self):
        self.h = []

    def push(self, cost, node):
        self.h.append((cost, node))
        i = len(self.h) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.h[i][0] < self.h[p][0]:
                self.h[i], self.h[p] = self.h[p], self.h[i]
                i = p
            else:
                break

    def pop(self):
        self.h[0], self.h[-1] = self.h[-1], self.h[0]
        val = self.h.pop()
        i = 0
        while True:
            l, r = 2*i+1, 2*i+2
            m = i
            if l < len(self.h) and self.h[l][0] < self.h[m][0]:
                m = l
            if r < len(self.h) and self.h[r][0] < self.h[m][0]:
                m = r
            if m == i:
                break
            self.h[i], self.h[m] = self.h[m], self.h[i]
            i = m
        return val

    def empty(self):
        return len(self.h) == 0


class MaxHeap:
    def __init__(self):
        self.h = []

    def push(self, pkg):
        self.h.append(pkg)
        i = len(self.h) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.h[i].priority > self.h[p].priority:
                self.h[i], self.h[p] = self.h[p], self.h[i]
                i = p
            else:
                break

    def pop(self):
        self.h[0], self.h[-1] = self.h[-1], self.h[0]
        val = self.h.pop()
        i = 0
        while True:
            l, r = 2*i+1, 2*i+2
            m = i
            if l < len(self.h) and self.h[l].priority > self.h[m].priority:
                m = l
            if r < len(self.h) and self.h[r].priority > self.h[m].priority:
                m = r
            if m == i:
                break
            self.h[i], self.h[m] = self.h[m], self.h[i]
            i = m
        return val

    def peek(self):
        return self.h[0] if self.h else None

    def empty(self):
        return len(self.h) == 0

    def size(self):
        return len(self.h)