
class Model_List:
    def __init__(self): 
        self.items=[]
        self.done=[]
    
    def add(self, item): 
        self.items.append(item)

    def complete(self, item): 
        if item not in self.items:
            return False
        self.items.remove(item)
        self.done.append(item)

    def save(self,fileName):
        with open(fileName,"w") as f:
            for item in self.items:
                f.write(item+"\n")
        f.close()

if __name__ == '__main__':
    print("Model_List")
    