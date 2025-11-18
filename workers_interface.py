from order_interface import Order_Interface
from abc import ABC, abstractmethod

class Worker_Interface(ABC):
    @abstractmethod
    def set_next(self):
        pass

    @abstractmethod
    def handle(self):
        pass

class absent(Worker_Interface):
    def set_next(self, next_worker):
        pass

    def handle(self, item):
        message = "[Sistema]: " + item.get_name() + "no se encuentra disponible."
        print(message)

class Baker(Worker_Interface):
    def __init__(self):
        self.next = absent()
    
    def set_next(self, next_worker):
        self.next = next_worker

    def handle(self, item):
        if item.get_type() == "Reposteria":
            pastry = item.get_name()
            message = "[Pastelero]: Preparo alimento: " + pastry + "."
            print(message)
        else:
            self.next.handle(item)

class Barista(Worker_Interface):
    def __init__(self):
        self.next = absent()
    
    def set_next(self, next_worker):
        self.next = next_worker

    def handle(self, item):
        if item.get_type() == "Reposteria":
            pastry = item.get_name()
            message = "[Barista]: Preparo alimento: " + pastry + "."
            print(message)
        else:
            self.next.handle(item)



        