class MyClass:
    
    def __init__(self, name = 'yongguang', age = 33):
        self.__name = name
        self.age = age
        
    def walk(self):
        print('i am walking')
    
object1 = MyClass()
object1._MyClass__name = 'hahaha'
print(object1._MyClass__name, object1.age)
object1.walk()