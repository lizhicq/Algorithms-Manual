from collections import defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vector = defaultdict(int)

    def get(self, key: int) -> int:
        self.vector
    def put(self, key: int, value: int) -> None: