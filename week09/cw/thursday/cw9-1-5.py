import time
class cache:
    def __init__(self):
        self.results={}
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"final status: len({self.results}")
        for key in self.results:
            print(f"key: {key}, value: {self.results[key]}")
    def run(self, func, *args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in self.results:
            print(f"result for {key} is in cache")
            return self.results[key]
def slow_func(x):
    time.sleep(1)
    return x
if __name__ == "__main__":
    with cache() as cache:
        print(cache.run(slow_func, 10))
        print(cache.run(slow_func, 10))
        print(cache.run(slow_func, 20))
        print(cache.run(slow_func))