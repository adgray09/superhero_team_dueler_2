class Animal:
    def __init__ (self, name, sleep_duration):
        self.name = name 
        self.sleep_duration = sleep_duration
        
    def sleep(self):
        print(f"{self.name} sleeps for {self.sleep_duration} hours")
        
class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
        
    def bark(self):
        print(f"{self.name} goes woof!")
        
    def sit(self):
        print(f"{self.name} sits")

    def rolls(self):
        print(f"{self.name} rolls over")
        
        
        
my_dog = Dog("Romeo", 12)
my_dog.sleep()
