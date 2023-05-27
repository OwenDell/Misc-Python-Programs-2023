#########################################
#               IMPORTS                 #
#########################################

import random
from inspect import signature

#########################################
#           GLOBAL VARIABLES            #
#########################################

enemies = []
moves_list = {}
test_iteration = 1
running = True

#########################################
#           PLAYER VARIABLES            #
#########################################



#########################################
#               CLASSES                 #
#########################################

class Creature:
    def __init__(self, name, level, XP, maxHP, gold, moves):
        self.name = name
        self.level = level
        self.XP = XP
        self.maxHP = maxHP
        self.health = maxHP
        self.gold = gold
        self.moves = moves
        enemies.append(self)
    
    def __str__(self):
        return f"Lvl: {self.level} {self.name}, with {self.health} HP!"
        
    def creature_attack(self, target):
        possible_moves = self.moves.copy()
        for chance in self.moves:
            if chance[1] >= random.randint(0, sum([possible_moves[i][1] for i in range(len(possible_moves))])):
                move = chance[0]
                move(self, target)
                break
            possible_moves.remove(chance)

#########################################
#          BACK-END FUNCTIONS           #
#########################################
         
def converter(*args):
    args = list(args)
    for index, parameter in enumerate(args):
        if "/O/" in parameter[:3].upper():
            args[index] = globals()[parameter[3:]]
        elif "/I/" in parameter[:3].upper():
            args[index] = int(parameter[3:])
        elif "/F/" in parameter[:3].upper():
            args[index] = float(parameter[3:])
        elif "/L/" in parameter[:3].upper():
            args[index] = parameter[3:].split()
        else:
            pass
    return args
        
def basic_attack(move, user, target, message=f"attacked you"):
    target.health -= move.damage
    if user is player:
        print(f"{message}, dealing {move.damage} damage!")
    elif target is player:
        print(f"The {user.name} {message}, dealing {move.damage} damage!")
    else:
        print(f"The {user.name} attacked the {target.name}, dealing {move.damage} damage!")
    
def heal(target):
    target.health = target.maxHP
    print(f"{target.name} has been fully healed to {target.health} HP!")
    
def run_test(*args):
    global test_iteration
    print(f"Running Test #{test_iteration}...")
    print(args)
    print(f"Test #{test_iteration} complete.")
    test_iteration += 1
    
def end_game():
    global running
    running = False
    print("Ending gameplay loop...")
        
def duel(duelist1, duelist2):
    victor = False
    loser = False
    print(f"A 1v1 Duel begins between the {duelist1.name} and the {duelist2.name}!")
    while duelist1.health > 0 and duelist2.health > 0:
        duelist1.creature_attack(duelist2)
        duelist2.creature_attack(duelist1)
    if duelist1.health <= 0 and duelist2.health <= 0:
        print(f"Both duelists felled each other simultaneously, ending in a draw!")
        victor = False
    elif duelist1.health > 0:
        victor = duelist1
        loser = duelist2
    elif duelist2.health > 0:
        victor = duelist2
        loser = duelist1
    if victor != False:
        victor.gold += loser.gold
        print(f"The {victor.name} has felled the {loser.name} in single combat, earning them {loser.gold} gold!")
        
def player_move(target):
    while True:
        response = input("What do you do? ")
        response = response[0].upper()+response[1:].lower()
        if response == "Options":
            moves_list[response](target)
        elif response in player.moves:
            try:
                moves_list[response](target)
                break
            except Exception as e:
                print(f"An error has occured [2].")
                print(e)
        else:
            print(f"Response \'{response}\' not recognized or unlearnt. Try \'options\' for a list of valid options.")
        
def learn_move(move_name):
    try:
        player.moves[move_name] = moves_list[move_name]
        print(f"You learned {move_name}!")
    except:
        print(f"Unrecognized move: \'{move_name}\'.")
        
#########################################
#          FRONT-END FUNCTIONS          #
#########################################

def f_devcmds():
    try:
        command = globals()[input("Enter a command: ")]
        params_list = str(signature(command).parameters)[13:-2].split(">), (")
        try:
            if params_list != ['']:
                params_count = len(params_list)
            else:
                params_count = 0
            params_response = [input(f"Argument #{i+1}/{params_count}: ") for i in range(params_count)]
            try:
                if params_response[0].upper() == "SET_ARGS":
                    params_count = int(input("How many arguments? "))
                    params_response = [input(f"Argument #{i+1}/{params_count}: ") for i in range(params_count)]
            except:
                pass
            params_response = converter(*params_response)
            command(*params_response)
        except:
            print("An error has occurred [1].")
    except:
        print("Unrecognized command.")
        
def f_commands():
    commands_list = []
    for globals_object in globals():
        if globals_object[:2] == "f_":
            commands_list.append(globals_object[2:])
    print(f"""List of valid commands:\n{", ".join(commands_list[1:])}""")

#########################################
#            CREATURE MOVES             #
#########################################

class Claw:
    def __init__(self):
        self.damage = 10
        
    def __call__(self, user, target):
        basic_attack(self, user, target, f"gouged you with their claws")
        
class Bite:
    def __init__(self):
        self.damage = 20
        
    def __call__(self, user, target):
        basic_attack(self, user, target, f"bit your arm")
        
class Stab:
    def __init__(self):
        self.damage = 30
        
    def __call__(self, user, target):
        basic_attack(self, user, target, f"stabbed you in the torso")

#########################################
#             PLAYER MOVES              #
#########################################

class m_Options:
    def __init__(self):
        self.name = "Options"
        global moves_list
        moves_list[self.name] = self
        player.moves[self.name] = moves_list[self.name]
        
    def __str__(self):
        return f"{self.name}: Returns a list of all available actions you can take during combat."
        
    def __call__(self, target):
        global moves_list
        print("List of valid options:")
        for i in player.moves:
            print(player.moves[i])
        
class m_Punch:
    def __init__(self):
        self.name = "Punch"
        self.damage = 5
        global moves_list
        moves_list[self.name] = self
        player.moves[self.name] = moves_list[self.name]
        
    def __str__(self):
        return f"{self.name}: A swift punch that deals {self.damage} damage."
        
    def __call__(self, target):
        global moves_list
        basic_attack(self, player, target, f"You punched the {target.name} in the face")
        
class m_Flee:
    def __init__(self):
        self.name = "Flee"
        global moves_list
        moves_list[self.name] = self
        player.moves[self.name] = moves_list[self.name]
        
    def __str__(self):
        return f"{self.name}: You attempt to flee combat."
        
    def __call__(self, target):
        global moves_list
        print(f"You fled from the enemy {target.name}!")

#########################################
#               CREATURES               #
#########################################
        
goblin = Creature("Goblin", 1, 10, 50, 35, [[Stab(), 70], [Claw(), 30], [Bite(), 50]])
dog = Creature("Dog", 3, 25, 200, 0, [[Claw(), 150], [Bite(), 80]])
player = Creature("Player", 1, 0, 100, 0, {})

#########################################
#             GAMEPLAY LOOP             #
#########################################

temp_globals = globals().copy() #initializes all the player moves, which add themselves to a list of possible player moves
for globals_object in temp_globals:
    if globals_object[:2] == "m_":
        globals()[globals_object]()

while running == True:
    response = "f_" + input("What would you like to do? ")
    try:
        globals()[response.lower()]()
    except:
        print(f"Response \'{response[2:]}\' not recognized. Try \'commands\' for a list of valid options.")
        
print("Game has ended.")
