class MyArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.element = 0
        self.data = [None] * capacity

    def __getitem__(self, index):
        if index < 0 or index >= self.element:
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.element:
            raise IndexError("Index out of range")
        self.data[index] = value

    def __str__(self):
        return str(self.data[:self.element])

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.element):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.element == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.element] = value
        self.element += 1

    def remove(self, value):
        index = None
        for i in range(self.element):
            if self.data[i] == value:
                index = i
                break
        if index is None:
            raise ValueError("Element not found in array")
        for i in range(index, self.element - 1):
            self.data[i] = self.data[i + 1]
        self.element -= 1
        if self.element < self.capacity // 4:
            self.resize(self.capacity // 2)

    def index(self, value):
        for i in range(self.element):
            if self.data[i] == value:
                return i
        raise ValueError("Element not found in array")
