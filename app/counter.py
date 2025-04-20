class Counter:
    def __init__(self):
        self.count = 0
        self.open = True

    def add(self):
        if not self.open:
            raise Exception("Counter is closed")
        self.count += 1

    def close(self):
        self.open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open = False
        if self.open:
            raise Exception("Resource is still open")
