from Array import MyArray

class MyDictionary:
    def __init__(self):
        self.keys = MyArray()
        self.values = MyArray()

    def insert(self, key, value):
        if key in self.keys:
            raise KeyError("Key already exists")
        self.keys.append(key)
        self.values.append(value)

    def delete(self, key):
        if key not in self.keys:
            raise KeyError("Key not found")
        index = self.keys.index(key)
        value = self.values[index]
        self.keys.remove(key)
        self.values.remove(value)

    def __str__(self):
        items = ['{}: {}'.format(key, value) for key, value in zip(self.keys, self.values)]
        return '{' + ', '.join(items) + '}'

    def __iter__(self):
        return zip(self.keys, self.values)

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError("Key not found")
        index = self.keys.index(key)
        return self.values[index]
