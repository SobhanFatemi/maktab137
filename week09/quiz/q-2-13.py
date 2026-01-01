class Publisher:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print("Got update:", message)


pub = Publisher()

obs1 = Observer()
obs2 = Observer()

pub.add_observer(obs1)
pub.add_observer(obs2)

pub.notify("Hello!")
pub.notify("State changed!")