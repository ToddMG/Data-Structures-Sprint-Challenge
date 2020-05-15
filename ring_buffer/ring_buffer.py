class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = None
        self.size = 0

    def append(self, item):
        # if nothing in storage, set oldest to new
        # append to storage
        if self.size == 0:
            self.storage.append(item)
            self.oldest = item
            self.size += 1

        # if something exists but not over capacity,
        # append to storage
        elif self.size < self.capacity:
            self.storage.append(item)
            self.size += 1

        # if capacity full,
        # replace oldest with newest
        # change oldest to next
        else:
            old_index = self.storage.index(self.oldest)
            self.storage.remove(self.oldest)
            self.storage.insert(old_index, item)
            try:
                self.oldest = self.storage[old_index+1]
            except:
                self.oldest = self.storage[0]

    def get(self):
        return self.storage