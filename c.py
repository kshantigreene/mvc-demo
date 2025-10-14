from m import Model_List
class Controller:
    def __init__(self, model):
        self.model = model
    
    def add(self, item):
        self.model.add(item)
    
    def complete(self, item):
        self.model.complete(item)
    