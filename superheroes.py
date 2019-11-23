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
            print(opponent.name + " is the winner!")
            opponent.add_kill(1)
            self.add_death(1)
            
        else:
            print(self.name + " is the winner!")
            self.add_kill(1)
            opponent.add_death(1)
        if (self.is_alive()):
            self.add_kill()
            opponent.add_death()
            print(self.name + ' Won the brawl!')
        elif (opponent.is_alive()):
            self.add_death()
            opponent.add_kill()
            print(opponent.name + ' Won the brawl!')
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
            print("{} Kill/Deaths:{}".format(hero.name, kd))
            
    
    def revive_heroes(self):
        for hero in self.heroes:
            if hero.is_alive() == False:
                hero.current_health = hero.starting_health
    
    def attack(self, other_team):
        
        living_heroes = list()
        living_opponents = list()
        dead_heroes = list()
        dead_opponents = list()
        
        
        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)
    
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero_1 = random.choice(self.heroes)
            hero_2 = random.choice(other_team.heroes)
            if hero_1.is_alive() and hero_2.is_alive():
                hero_1.fight(hero_2)
            while hero in living_heroes:
                if hero_1.is_alive() == False and hero_2.is_alive() == True:
                    dead_opponents.append(hero_2)
            while hero in living_opponents:
                if hero_1.is_alive() == True and hero_2.is_alive() == False:
                    dead_heroes.append(hero_1)
            break

#ARENA CLASS     
class Arena:
    def __init__ (self):
        self.team_one: None
        self.team_two: None
        
    def create_ability(self):
        name = input("What is your ability name?")
        max_damage = input("What is your abailities max damage?")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the your weapons name?")
        max_damage = input("What is the weapons max damage?")
        return Weapon(name, max_damage)
    
    def create_armor(self):
        name = input("What is the name of your armor?")
        max_block = input("What is the armors block strength?")
        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input("Name of hero?")
        new_hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                #TODO add an ability to the hero
                new_hero.add_ability(self.create_ability())
            elif add_item == "2":
                #TODO add a weapon to the hero
                new_hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                #TODO add an armor to the hero
                new_hero.add_armor(self.create_armor())
        return new_hero
    
    def build_team_one(self):
        team_name = input("What is the name of team 1?")
        team_size = int(input("How many heroes are on team 1?"))
        self.team_one = Team(team_name)
        
        for _ in range(0, team_size):
            self.team_one.heroes.append(self.create_hero())
        
    def build_team_two(self):
        team_name = input("What is the name of team 2?")
        team_size = int(input("How many heroes are on team 2?"))
        self.team_two = Team(team_name)
        
        for _ in range(0, team_size):
            self.team_one.heroes.append(self.create_hero())
            
    def team_battle(self):
        self.team_one.attack(self.team_two)
        
    def show_stats(self):
        team_one_kills = 0
        team_one_deaths = 0
        team_two_kills = 0 
        team_two_deaths = 0 
        
        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths +=  hero.deaths
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        try:
            team_1_kd = team_one_kills / team_one_deaths
        except ZeroDivisionError:
            team_1_kd = team_one_kills
        try:
            team_2_kd = team_two_kills / team_two_deaths
        except ZeroDivisionError:
            team_2_kd = team_two_kills
        
        print("Team 1's KD is: {}".format(str(team_1_kd)))
        print("Team 2's KD is: {}".format(str(team_2_kd)))
            
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"{hero.name} from team 1 survived!")
                
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"{hero.name} from team 2 survived!")
                
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()