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
        self.deaths = 0
        self.kills = 0
    
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

    def add_kill(self, num_kills=1):
        self.kills += num_kills
    
    def add_death(self, num_deaths=1):
        self.deaths += num_deaths
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        
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
        print('A brawl is happening between  ' + self.name + ' and ' +opponent.name + '! Who will be victorious?')
        while self.is_alive() and opponent.is_alive():
            if self.abilities or opponent.abilities:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                print()
            else: 
                print("DRAW!")
        
        if self.current_health <= 0:
            print(opponent.name + " won the battle!")
            self.add_death()
            opponent.add_kill()
        elif opponent.current_health <= 0: 
            print(self.name + " won the battle!")
            self.add_kill()
            opponent.add_death()
        else:
            print("Draw!")
    
#WEAPON CLASS
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
            
        #choosing random number between 1/2 and full of max_damage
        return random.randint(self.max_damage//2, self.max_damage)
    
class Team:
    def __init__ (self, name):
        self.name = name
        self.heroes = list()
    
    def remove_hero(self, name):
        
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
            
    def add_hero(self, hero):
        self.heroes.append(hero)
        
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    
    def revive_heroes(self):
        for hero in self.heroes:
            if hero.is_alive() == False:
                hero.current_health = hero.starting_health
    
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())