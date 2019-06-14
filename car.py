class Car:
    def __init__(
            self,
            color = 'gray',
            max_speed = 220,
            make = 'toyota',
            model = 'rav4',
            current_speed = 100):
        
        self.color = color
        self.max_speed = max_speed
        self.make = make
        self.modle = model
        self.current_speed = current_speed
        
    def Accelerate(self):
        self.current_speed += 1
        print('current speed is ', self.current_speed)
        
    def Stop(self):
        self.current_speed = 0
        print('current speed is 0')
        
    def turnRight(self):
        print('Turned Right')
        
    def turnLeft(self):
        print('Turned Left')

car = Car(make = 'Ford', model = 'Focus')
print(car.make, car.modle)
car.Accelerate()
car.Stop()
car.turnRight()
car.turnLeft()
        