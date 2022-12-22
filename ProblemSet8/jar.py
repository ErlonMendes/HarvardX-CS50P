class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There are not enough cookies to take")
        self.size -= n

    @property  # Getter of capacity
    def capacity(self):
        return self._capacity

    @capacity.setter  # Setter de capacity
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property  # Getter of size
    def size(self):
        return self._size

    @size.setter  # Setter de size
    def size(self, size):
        if size < 0:
            raise ValueError("Invalid size")
        self._size = size
