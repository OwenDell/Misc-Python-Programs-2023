import random #used for randomly generating the hidden phrase

#Variables:
chosenword = "hello world" #placeholder hidden phrase used for testing.
hangman_stage = 0 #tracks the stage of the hangman so the progress_hangman() function knows what body to draw next, ends the game in a loss if this reaches 7.
speed(10) #left this in the variables section so it's at the top and easiest for me to change while testing.
word_dict = {} #empty dictionary that will fill with each character of the hidden phrase, with the characters position stored as the key.
letters_needed = [] #list of the letters that still need to be guessed in order to win, every time a letter is correctly guessed it will be removed from the list.
guesses = [] #An empty list waiting to be filled, which tracks the players guesses throughout a game for them to check with /guesses command
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] #full alphabet used when the player is guessing to ensure that it's a valid guess.

#List of possible words to be randomly combined to form the hidden phrase, broken up into different categories of words so they can be combined in ways that make at least some amount of grammatical sense:
noun_type1 = ["human", "people", "me", "dog", "game", "food", "cat", "us", "everyone", "potato", "them", "you", "burger", "hat", "beast", "house", "home", "stew", "soup", "hotdog", "donut", "muffin", "horse", "zebra", "bear", "door", "flower", "rose", "cow", "pig", "elephant", "lion", "tiger", "towel", "tower", "nerd", "loser", "teacher", "school", "girl", "boy", "computer", "desk", "chair", "onion", "apple", "orange", "pineapple", "pear", "banana", "map", "rythm", "rhyme", "art", "ant", "animal", "angler", "artist", "age", "boost", "bag", "bass", "bug", "basket", "ball", "chalice", "champion", "chalk", "choice", "cast", "cell", "coop", "coup", "crime", "case", "call", "carp", "cost", "comb", "camp", "dice", "den", "deck", "dose", "dew", "dare", "desk", "egg", "ember", "elk", "echo", "foot", "flood", "fuse", "film", "fable", "fern", "goose", "game", "gum", "germ", "gas", "guess", "hoop", "ham", "hole", "helmet", "heist", "hound", "ice", "igloo", "imp", "joker", "jock", "joke", "judge", "jury", "jug", "jester", "java", "koala", "king", "kid", "kitten", "kiss", "kibble", "lodge", "loser", "lake", "lamp", "lamb", "liquor", "limb", "moon", "mother", "moss", "mask", "maze"]
noun_type2 = ["humans", "people", "we", "dogs", "games", "cats", "they", "you", "potatos", "burgers", "hats", "beasts", "houses", "homes", "stew", "soups", "hotdogs", "donuts", "muffins", "horses", "zebras", "bears", "doors", "flowers", "roses", "cows", "pigs", "elephants", "lions", "tigers", "towels", "towers", "nerds", "losers", "teachers", "schools", "girls", "boys", "computers", "desks", "chairs", "onions", "apples", "oranges", "pineapples", "pears", "bananas", "maps", "art", "ants", "animals", "anglers", "artists", "ages", "rythms", "rhymes", "boost", "bags", "bass", "bugs", "baskets", "balls", "chalices", "champions", "chalk", "choices", "cast", "cells", "coops", "coups", "crimes", "cases", "calls", "carps", "costs", "combs", "camps", "dice", "dens", "decks", "doses", "dew", "dares", "desks", "eggs", "embers", "elk", "echos", "feet", "floods", "fuse", "films", "fables", "ferns", "geese", "games", "gum", "germs", "gas", "guesses", "hoops", "ham", "holes", "helmets", "heists", "hounds", "ice", "igloos", "imps", "jokers", "jocks", "jokes", "judges", "jury", "jugs", "jesters", "java", "koalas", "kings", "kids", "kittens", "kisses", "kibble", "lodges", "losers", "lakes", "lamps", "lambs", "liquor", "limbs", "moons", "mothers", "moss", "masks", "mazes"]
verb_type1 = ["eat", "want", "love", "ask", "like", "hate", "kick", "work", "buy", "fear", "see", "watch", "have", "hurt", "sniff", "break", "fix", "lick", "use", "hire", "hide", "steal", "rob", "help", "make", "catch"]
verb_type2 = ["are", "become", "seem", "feel", "stay", "look", "smell", "taste", "sound"]
adjective = ["dumb", "silly", "smart", "wise", "honest", "modest", "big", "bad", "poor", "quiet", "scary", "long", "short", "tall", "round", "tasty", "smelly", "stinky", "gross", "strong", "weak", "rich", "wide", "hungry", "small", "fat", "skinny", "huge", "fast", "slow", "burnt", "crispy", "fresh"]

#Functions:

def generate_phrase(): #Used to randomly generate the hidden phrase using the list of words in various combinations.
    while True:
        if random.randint(0, 3) > 1: #plural noun + action verb + singular noun
            phrase = noun_type2[random.randint(0, len(noun_type2) - 1)] + " " + verb_type1[random.randint(0, len(verb_type1) - 1)] + " " + noun_type1[random.randint(0, len(noun_type1) - 1)]
        elif random.randint(0, 2) > 0: #plural noun + describing verb + adjective
            phrase = noun_type2[random.randint(0, len(noun_type2) - 1)] + " " + verb_type2[random.randint(0, len(verb_type2) - 1)] + " " + adjective[random.randint(0, len(adjective) - 1)]
        else: #adjective + singular noun
            phrase = adjective[random.randint(0, len(adjective) - 1)] + " " + noun_type1[random.randint(0, len(noun_type1) - 1)]
        if len(phrase) > 12:
            continue
        else:
            return phrase

#The following functions draw a different part of the hangman body, they all have the 'dcolor' parameter to determine what color they should draw in, defaulting to black but will be switched to red for the loss end sequence when the entire hangman is re-traced in red
def draw_head(dcolor="black"):
    setposition(25, 165)
    pendown()
    color(dcolor)
    circle(-30)
    penup()

def draw_body(dcolor="black"):
    setposition(25, 105)
    pendown()
    color(dcolor)
    right(90)
    forward(110)
    penup()
    left(90)
    
def draw_leg_left(dcolor="black"):
    setposition(25, -5)
    pendown()
    color(dcolor)
    right(45)
    forward(50)
    penup()
    left(45)
    
def draw_leg_right(dcolor="black"):
    setposition(25, -5)
    pendown()
    color(dcolor)
    right(135)
    forward(50)
    penup()
    left(135)
    
def draw_arm_left(dcolor="black"):
    setposition(25, 85)
    pendown()
    color(dcolor)
    right(25)
    forward(65)
    penup()
    left(25)
    
def draw_arm_right(dcolor="black"):
    setposition(25, 85)
    pendown()
    color(dcolor)
    right(155)
    forward(65)
    penup()
    left(155)

def draw_eye(size=0):
    right(45)
    forward(10+30*size)
    backward(5+15*size)
    left(90)
    backward(5+15*size)
    forward(10+30*size)
    right(45)
    
def draw_eyes(dcolor="black"):
    setposition(5, 140)
    pendown()
    color(dcolor)
    draw_eye()
    penup()
    setposition(35, 140)
    pendown()
    draw_eye()
    penup()
    setposition(200, -200)
        
#Gallows are to be drawn on startup:
def draw_gallows():
    penup()
    color("brown")
    setposition(0, 50)
    backward(75)
    pendown()
    right(90)
    forward(100)
    left(90)
    forward(50)
    backward(100)
    forward(50)
    left(90)
    forward(240)
    right(90)
    forward(100)
    right(90)
    forward(25)
    color("black")
    left(90)
        
def draw_lines(): #This function draws the lines at the bottom of the UI upon game startup. The function uses the length of the hidden phrase to know how many to draw, and will drop down to the second line if it's more than 6 characters (which it almost always is without interference), and it will leave spaces blank.
    color("black")
    penup()
    for i in range(len(chosenword)):
        if i == 0:
            if len(chosenword) > 5:
                setposition(-(190), -130)
            else:
                setposition(-(len(chosenword)*32), -190)
        if i == 6:
            setposition(-((len(chosenword)-6)*32), -190)
        if chosenword.find(" ", i, i+1) == -1:
            pendown()
            forward(50)
        else:
            forward(50)
        penup()
        forward(15)
      
def convert(string): #splits the hidden phrase into a list of single characters. (This function is obsolete in the final version of my code, but I'm still leaving it here for reference and encase I want to make future changes that require this)
    list1 = []
    list1[:0] = string
    return list1
      
def needing_letters(phrase): #done upon startup that splits the hidden phrase into a dictionary of single characters, with the attached key being the position of each character.
    for i in range(len(phrase)):
        word_dict[i] = phrase[i]
    for letter in alphabet:
        if phrase.find(letter) >= 0:
            letters_needed.append(letter)
      
def letter_check(): #used to check if the players guess is correct. It goes through every spot number in the word_dict and checks if that spot number's associated character is equal to the players guess, in which case that dictionary entry is deleted and the letter is drawn. The letter is also removed from letters_needed which the game uses to determine when the player has won upon said list being empty.
    global word_dict
    global letters_needed
    letters_needed.remove(guess)
    for spot_number in word_dict:
        try:
            if word_dict[spot_number] == guess:
                word_dict.pop(spot_number)
                draw_letter(guess, spot_number)
        except:
            print("Error encountered in: letter_check() [1]")
            continue

def progress_hangman(stage): #references hangman_progress to determine what body part of the hangman to draw, or to end the game in a loss upon reaching stage 7, initiating the end sequence(lose)
    if stage == 1:
        draw_head("gray")
    elif stage == 2:
        draw_body("gray")
    elif stage == 3:
        draw_leg_left("gray")
    elif stage == 4:
        draw_leg_right("gray")
    elif stage == 5:
        draw_arm_left("gray")
    elif stage == 6:
        draw_arm_right("gray")
    elif stage > 6:
        speed(0)
        draw_head("red")
        draw_body("red")
        draw_leg_left("red")
        draw_leg_right("red")
        draw_arm_left("red")
        draw_arm_right("red")
        draw_eyes("red")
        print("The correct phrase was '" + chosenword + "', you lose!")
        end_sequence("lose")
    color("black")
    
def end_sequence(result): #The function for the visual animation end sequence that occurs when the player either empties the letters_needed list, resulting in a win, or reaches hangman_progress 7, resulting in a loss. Uses the "win" or "lose" parameters to determine what colors and shapes to draw at certain points in the sequence.
    speed(3)
    setpos(-190, 190)
    if result == "win":
        color("green")
    else:
        color("red")
    pendown()
    pensize(25)
    speed(9)
    forward(380)
    right(90)
    for i in range(380, 0, -20):
        for k in range(2):
            forward(i)
            right(90)
    pensize(10)
    left(270)
    speed(0)
    if result == "win":
        setpos(-125, 40)
        color("yellow")
        begin_fill()
        for i in range(5):
            forward(250)
            right(144)
        end_fill()
    else:
        setpos(0, -100)
        color("white")
        begin_fill()
        circle(100)
        end_fill()
        color("red")
        pensize(10)
        penup()
        setpos(-60, 50)
        pendown()
        draw_eye(1)
        penup()
        forward(60)
        pendown()
        draw_eye(1)
        penup()
        setpos(-60, -50)
        right(285)
        pendown()
        circle(-60, 150)
    penup()
    setpos(200, -200)

def draw_letter(letter, spotnumber): #Has the code for every letter in the alphabet to be drawn when the player correctly guesses one of the letters.
    if len(chosenword) > 5:
        if spotnumber <= 5: #sets position for drawing on the top row
            setposition(-190+(65*spotnumber), -125)
        else: #sets position for drawing on the bottom row
            setposition(-((len(chosenword)-6)*32)+(65*(spotnumber-6)), -185)
    else: #while technically possible with the right combination of random words (ex: "big me"), this pretty much never happens without manually setting the hidden phrase in the code.
        setposition(-(len(chosenword)*32)+(65*spotnumber), -185)
    pendown()
    if letter == "test": #used for testing purposes, as the name would imply.
        color("green")
        begin_fill()
        circle(25)
        end_fill()
    elif letter == "a":
        penup()
        left(90)
        forward(3)
        right(90)
        pendown()
        left(60)
        forward(50)
        right(120)
        forward(50)
        backward(30)
        right(120)
        forward(20)
        right(180)
    elif letter == "b":
        left(90)
        forward(50)
        backward(25)
        right(90)
        circle(14, 180)
        right(90)
        backward(25)
        right(90)
        circle(-14, 180)
        right(180)
    elif letter == "c":
        penup()
        forward(25)
        right(180)
        pendown()
        circle(-25, 180)
    elif letter == "d":
        circle(25, 180)
        left(90)
        forward(50)
        left(90)
    elif letter == "e":
        for i in range(2):
            forward(50)
            backward(50)
            left(90)
            forward(25)
            right(90)
        forward(50)
    elif letter == "f":
        left(90)
        forward(50)
        right(90)
        forward(50)
        backward(50)
        right(90)
        forward(20)
        left(90)
        forward(50)
    elif letter == "g":
        penup()
        forward(50)
        left(90)
        forward(15)
        right(90)
        left(250)
        pendown()
        circle(-25, 280)
        penup()
        left(30)
        forward(10)
        right(90)
        forward(30)
        right(90)
        pendown()
        forward(20)
        right(180)
    elif letter == "h":
        left(90)
        forward(50)
        backward(25)
        right(90)
        forward(50)
        left(90)
        forward(25)
        backward(50)
        right(90)
    elif letter == "i":
        forward(50)
        backward(25)
        left(90)
        forward(50)
        right(90)
        backward(25)
        forward(50)
    elif letter == "j":
        penup()
        left(90)
        forward(10)
        right(180)
        pendown()
        circle(10, 180)
        forward(40)
        right(90)
        backward(25)
        forward(50)
    elif letter == "k":
        left(90)
        forward(50)
        backward(25)
        right(45)
        forward(35)
        backward(35)
        right(90)
        forward(35)
        left(45)
    elif letter == "l":
        left(90)
        forward(50)
        backward(50)
        right(90)
        forward(30)
    elif letter == "m":
        left(90)
        forward(50)
        right(135)
        forward(35)
        left(90)
        forward(35)
        right(135)
        forward(50)
        left(90)
    elif letter == "n":
        left(90)
        forward(50)
        right(135)
        forward(70)
        left(135)
        forward(50)
        right(90)
    elif letter == "o":
        penup()
        forward(25)
        pendown()
        circle(25)
    elif letter == "p":
        left(90)
        forward(50)
        right(90)
        circle(-15, 180)
        right(180)
    elif letter == "q":
        penup()
        forward(25)
        circle(25, 45)
        pendown()
        circle(25)
        left(90)
        backward(10)
        forward(20)
        right(135)
    elif letter == "r":
        left(90)
        forward(50)
        right(90)
        circle(-15, 180)
        left(135)
        forward(30)
        left(45)
    elif letter == "s":
        penup()
        forward(30)
        left(90)
        forward(15)
        left(180)
        pendown()
        circle(-15, 180)
        penup()
        left(90)
        backward(30)
        right(90)
        pendown()
        left(50)
        forward(30)
        right(50)
        circle(-15, 180)
        left(90)
    elif letter == "t":
        penup()
        forward(25)
        left(90)
        pendown()
        forward(50)
        right(90)
        backward(25)
        forward(50)
    elif letter == "u":
        penup()
        left(90)
        forward(25)
        pendown()
        forward(25)
        backward(25)
        right(180)
        circle(25, 180)
        forward(25)
        right(90)
    elif letter == "v":
        penup()
        forward(25)
        left(120)
        pendown()
        forward(60)
        backward(60)
        right(60)
        forward(60)
        right(60)
    elif letter == "w":
        left(90)
        forward(50)
        backward(50)
        right(45)
        forward(35)
        right(90)
        forward(35)
        left(135)
        forward(50)
        right(90)
    elif letter == "x":
        left(45)
        forward(70)
        backward(35)
        left(90)
        forward(35)
        backward(70)
        right(135)
    elif letter == "y":
        penup()
        forward(25)
        left(90)
        pendown()
        forward(25)
        left(45)
        forward(30)
        backward(30)
        right(90)
        forward(30)
        right(45)
    elif letter == "z":
        forward(50)
        backward(50)
        left(45)
        forward(70)
        left(135)
        forward(50)
        left(180)
    penup() 
    
    
#startup:
chosenword = generate_phrase()
draw_gallows()
draw_lines()
needing_letters(chosenword)

#gameplay loop:
while len(letters_needed) > 0 and hangman_stage < 7: #main gameplay loop continues until the player either wins when the letters_needed list is emptied, or loses when hangman stage reaches 7.
    while True:
        guess = input("Enter your guess of a letter, or do /guesses to view previously guessed letters. ")
        if len(guess) > 1:
            if guess == "/guesses":
                print("Here's a list of already guessed letters for review:")
                print(guesses)
                continue
            else:
                print("Invalid response. Your response must not be longer than a single character.")
                continue
        if guess in alphabet:
            if guess in letters_needed:
                guesses.append(guess)
                letter_check()
            elif guess in guesses:
                print("Already guessed letter detected, please enter a new guess.")
            else:
                guesses.append(guess)
                hangman_stage += 1
                progress_hangman(hangman_stage)
        else:
            print("Invalid response. Your response must be a letter.")
            continue
        break
    setpos(200, -200) #returns the turtle to the bottom right corner so they aren't blocking the players vision or making letters/lines unclear, it also just looks nicer.
if len(letters_needed) < 1: #The 'win' end sequence is protected in an if statement, because the main gameplay while loop will still end and progress to this block of code when the game finishes in either a win or a loss.
    print("Congratulations! You won!")
    end_sequence("win")
