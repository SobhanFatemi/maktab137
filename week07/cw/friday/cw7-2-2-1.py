class Fibonacci:
    def __init__(self, max_count=None, max_value=None):
        self.count = 0
        self.a = 0
        self.b = 1
        self.max_count = max_count
        self.max_value = max_value

        if not max_count and not max_value:
            raise ValueError("You must give a limit!")

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_count is not None and self.count >= self.max_count:
            raise StopIteration

        if self.max_value is not None and self.a > self.max_value:
            raise StopIteration

        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value


fib1 = Fibonacci(max_count=3, max_value=13)

for number in fib1:
    print(number)
