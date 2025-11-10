from abc import ABC, abstractmethod

class Order_Interface(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Order_Component(Order_Interface):
    def __init__(self, type, name):
        self.type = type
        self.name = name     

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

class Order_Composite(Order_Interface):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.components = []
    
    def get_type(self):
        return self.type
    
    def get_name(self):
        name = self.name

        if (len(self.components) == 0):
            return name
        
        name += ' con '

        for i in range(len(self.components) - 1):
            name += self.components[i].get_name()
            name += ', '

        if (len(self.components) != 1):
            name += "y "

        name += self.components[len(self.components) - 1].get_name()

        return name
    
    def get_components(self, component):
        return self.components

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, index):
        self.components.pop(index)
