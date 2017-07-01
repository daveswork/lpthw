class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    
    def displayCar(self):
        mpq = str(self.mpg)
        print "This is %s %s with %s" %(self.model, self.color, mpq)
        print str(self.mpg)

myCar = Car("DeLorean", "silver", 88)
print myCar.condition
print myCar.model
print myCar.color
print myCar.mpg
myCar.displayCar
