import time

class NestedTimer:
    depth = 0

    def __init__(self, name):
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.intend= ''
        NestedTimer.depth += 1
        self.start_time = time.time()
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        NestedTimer.depth -= 1
        print(f'{self.intend} [{self.name}]Elapsed time: {elapsed_time} seconds')


#Usage
if __name__ == '__main__':
    with NestedTimer('outer'):
        time.sleep(0.1)

        with NestedTimer('inner'):
            time.sleep(0.05)