
from m import Model_List
from c import Controller
from v import SimpleGUI

def addItems(model):
    m.add("Buy groceries")
    m.add("Walk the dog")
    m.add("Read a book")
    m.add("0. Kshanti item")
    m.add("Item: 1 Caleb")
    m.add("Item: 2 Cian go to work")
    m.add("Item: 3 David")

if __name__ == '__main__':
    print("mvc")
    m = Model_List() 
    c = Controller(m)
    v = SimpleGUI(c)
    addItems(m)
    v.show(m.items)
    v.run()
    m.save("./items.txt")
    