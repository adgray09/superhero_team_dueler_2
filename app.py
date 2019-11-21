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
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name 
        self.starting_health = starting_health 
        self.current_health = starting_health
    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks. 
        return: total_damage:Int'''
        # start our total out at 0
        total_damage = 0
            # loop through all of our hero's abilities
        for ability in self.abilities:
                # add the damage of each attack to our running total
            total_damage += ability.attack()
            # return the total damage
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for block in self.armors:
            total_block += block.block()
        return total_block
            
    def take_damage(self, damage):
        defense = self.defend()    
        self.current_health -= damage - defense
    
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    
    def fight(self, opponent):
        
    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())