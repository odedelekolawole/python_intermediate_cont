class Tab:

    menu = {
        
        "wine": 5,
        "beer": 3,
        "sof_drink": 2,
        "chicken": 10,
        "beef": 12,
        "dessert": 6,
    }

    def __init__(self):
        self.total = 0
        self.otem = []

    def add(self, item):
        self.items.append(item)
        self.total =  