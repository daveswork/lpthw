class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print self.name, self.age

hippo = Animal("Rob", 7)

hippo.description()
