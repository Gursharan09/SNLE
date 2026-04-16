class HashMap:
    def __init__(self):
        self.size = 16
        self.keys = [None] * self.size
        self.vals = [None] * self.size
        self.count = 0

    def _hash(self, key):
        total = 0
        for c in key:
            total = (total * 31 + ord(c)) % self.size
        return total

    def insert(self, key, val):
        if self.count / self.size > 0.7:
            self._resize()
        i = self._hash(key)
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i + 1) % self.size
        if self.keys[i] is None:
            self.count += 1
        self.keys[i] = key
        self.vals[i] = val

    def get(self, key):
        i = self._hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1) % self.size
        return None

    def delete(self, key):
        i = self._hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.keys[i] = "DELETED"
                self.vals[i] = None
                self.count -= 1
                return True
            i = (i + 1) % self.size
        return False

    def _resize(self):
        old_k = self.keys
        old_v = self.vals
        self.size *= 2
        self.keys = [None] * self.size
        self.vals = [None] * self.size
        self.count = 0
        for k, v in zip(old_k, old_v):
            if k and k != "DELETED":
                self.insert(k, v)