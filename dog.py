class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
        
    def bark(self):
        print(f"{self.name} goes woof!")
        
    def sit(self):
        print(f"{self.name} sits")

    def rolls(self):
        print(f"{self.name} rolls over")

