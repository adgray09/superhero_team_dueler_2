import random

#ABILITY CLASS
class Ability:
    def __init__(self, name, max_damage):
        '''
    Initialize the values passed into this
    method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage
        
        
    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        #Pick a random value between 0 and self.max_damage
        random_value = random.randint(0,self.max_damage)
        return random_value
    
#ARMOR CLASS 
class Armor:
    def __init__(self, name, max_block=0):
        self.name = name
        self.max_block = max_block
        
    def block(self):
        random_value = random.randint(1,20)
        return random_value

#HERO CLASS
class Hero():
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name 
        self.starting_health = starting_health 
        self.current_health = starting_health
    

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())    
    armor = Armor("chestpiece", 20)
    
    print(armor.name)
    print(armor.block())