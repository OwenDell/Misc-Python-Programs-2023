#Variables:
hangmanprog = 0 #Tracks the stage of the hangman
speed(10)
correct = "false" #bool that tracks if the users guess was correct, so the program knows when not to progress the hangman
correctscore = 0 #Tracks how many letters the user has gotten correct throughout the game, so it knows when the player has won.
guesses = [] #An empty list waiting to be filled, which tracks the players guesses throughout a game for them to check with /guesses command

#Functions:
#The following functions are instructions to draw the hangman body as the game progresses.
def drawhead(dcolor):
    setposition(25, 125)
    pendown()
    color(dcolor)
    circle(-30)
    penup()

def drawbody(dcolor):
    setposition(25, 65)
    pendown()
    color(dcolor)
    right(90)
    forward(110)
    penup()
    left(90)
    
def drawlleg(dcolor):
    setposition(25, -45)
    pendown()
    color(dcolor)
    right(45)
    forward(50)
    penup()
    left(45)
    
def drawrleg(dcolor):
    setposition(25, -45)
    pendown()
    color(dcolor)
    right(135)
    forward(50)
    penup()
    left(135)
    
def drawlarm(dcolor):
    setposition(25, 45)
    pendown()
    color(dcolor)
    right(25)
    forward(65)
    penup()
    left(25)
    
def drawrarm(dcolor):
    setposition(25, 45)
    pendown()
    color(dcolor)
    right(155)
    forward(65)
    penup()
    left(155)

def draweye():
    right(45)
    forward(10)
    backward(5)
    left(90)
    backward(5)
    forward(10)
    right(45)
    
def draweyes(dcolor):
    setposition(5, 100)
    pendown()
    color(dcolor)
    draweye()
    penup()
    setposition(35, 100)
    pendown()
    draweye()
    penup()
    setposition(200, -200)

def hangman(progress): #This function uses the progression stage of the hangman to know what body part to draw next. When it reaches the final stage it redraws over the whole body in red and ends the game as a loss.
    if progress == 1:
        drawhead("gray")
    elif progress == 2:
        drawbody("gray")
    elif progress == 3:
        drawlleg("gray")
    elif progress == 4:
        drawrleg("gray")
    elif progress == 5:
        drawlarm("gray")
    elif progress == 6:
        drawrarm("gray")
    elif progress > 6:
        speed(0)
        drawhead("red")
        drawbody("red")
        drawlleg("red")
        drawrleg("red")
        drawlarm("red")
        drawrarm("red")
        draweyes("red")
        print("The correct word was " + chosenwordprint + ", you lose!")
        
#This function receives data on which letter is to be drawn and in what spot whenever the player guesses correctly. It then runs through the code for how to draw every possible letter.
def drawletter(letter, spotnumber):
    setposition(-175+(75*spotnumber), -185)
    pendown()
    if letter == "test":
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
    
#String splitting method obtained from geeksforgeeks.org. This is necessary for splitting the chosenword from a string into a list so the individual characters are modifiable.
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
        
#This function checks to see if the players guess has any correct letters in the right spot in the 'Word' gamemode, and then returns the relevent data if so.
def wordcheck():
    global correctscore
    global correct
    for i in range(5):
        if chosenword[i] == response.lower()[i]:
            #print("correct")
            correct = "true"
            correctscore += 1
            color("black")
            drawletter(chosenword[i], i)
            #drawletter("z", charnum)
            chosenword[i] = "~" #This changes the letter to a tilde when correctly guessed so that it does not get recounted every time the player guesses it correctly again.
        #else:
            #print("incorrect")
        
#Very similar to the wordcheck function, just for the 'Classic' gamemode where the player guesses individual letters instead of full words.
def lettercheck():
    global correctscore
    global correct
    for i in range(5):
        if chosenword[i] == response.lower():
            correct = "true"
            correctscore += 1
            color("black")
            drawletter(chosenword[i], i)
            chosenword[i] = "~"

#Similar to wordcheck, but for the "Wordle" gamemode based off the popular NYT browser-based puzzle game where when you guess a correct letter but in the wrong spot it will tell you so.
def wordlecheck(difficulty):
    global correctscore
    global correct
    global wordlecounted
    wordlearray = ["false", "false", "false", "false", "false"] #this tracks the accuracy of each letter in every guess. Completely wrong letters are written in red, correct letters in the wrong spot are in yellow, and fully correct letters are in green.
    penup() #This is to erase the prior guess once a new one is entered so they don't overlap.
    setposition(-200, -188)
    begin_fill()
    color("white")
    pendown()
    forward(400)
    left(90)
    forward(70)
    left(90)
    forward(400)
    left(90)
    forward(70)
    left(90)
    end_fill()
    color("black")
    penup()
    for i in range(5):
        for u in range(5):
            if chosenword[u] == response.lower()[i]:
                wordlearray[i] = "half"
    for i in range(5):
        if chosenword[i] == response.lower()[i]:
            if (wordlecounted[i] != "true") and (difficulty != "hard"):
                correct = "true"
            wordlearray[i] = "true"
            wordlecounted[i] = "true"
    for i in range(5):
        if wordlearray[i] == "false":
            color("red")
        elif wordlearray[i] == "half":
            color("yellow")
        elif wordlearray[i] == "true":
            color("green")
        else:
            color("black")
        drawletter(response.lower()[i], i)
    if wordlearray == ["true", "true", "true", "true", "true"]: #If every letter is correct in the correct spot, they are given the full score and win.
        correctscore = 5
    for i in range(len(guesses)): #This allows users to review prior guesses without penalty.
        if guesses[i] == response.lower():
            correct = "true"
            print("Already guessed word detected; displaying for review with no penalty incurred.")
    
    
#Base setup and picking word from library:
import random
words = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis", "Beach", "Birth", "Block", "Blood", "Board", "Brain", "Bread", "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest", "Chief", "Child", "Claim", "Class", "Clock", "Coach", "Coast", "Court", "Cover", "Cream", "Crime", "Cross", "Crowd", "Crown", "Cycle", "Dance", "Death", "Depth", "Doubt", "Draft", "Drama", "Dream", "Dress", "Drink", "Drive", "Earth", "Enemy", "Entry", "Error", "Event", "Faith", "Fault", "Field", "Fight", "Final", "Floor", "Focus", "Force", "Frame", "Front", "Fruit", "Glass", "Grant", "Grass", "Green", "Group", "Guide", "Heart", "Horse", "Hotel", "House", "Image", "Index", "Input", "Issue", "Judge", "Knife", "Layer", "Level", "Light", "Limit", "Lunch", "Major", "March", "Match", "Metal", "Model", "Money", "Month", "Motor", "Mouth", "Music", "Night", "Noise", "North", "Novel", "Nurse", "Offer", "Order", "Other", "Owner", "Panel", "Paper", "Party", "Peace", "Phase", "Phone", "Piece", "Pilot", "Pitch", "Place", "Plane", "Plant", "Plate", "Point", "Pound", "Power", "Press", "Price", "Pride", "Prize", "Proof", "Queen", "Radio", "Range", "Ratio", "Reply", "Right", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Scope", "Score", "Sense", "Shape", "Share", "Sheep", "Sheet", "Shift", "Shirt", "Shock", "Sight", "Skill", "Sleep", "Smile", "Smith", "Smoke", "Sound", "South", "Space", "Speed", "Spite", "Sport", "Squad", "Staff", "Stage", "Start", "State", "Steam", "Steel", "Stock", "Stone", "Store", "Study", "Stuff", "Style", "Sugar", "Table", "Taste", "Theme", "Thing", "Title", "Total", "Touch", "Tower", "Track", "Trade", "Train", "Trend", "Trial", "Trust", "Truth", "Uncle", "Union", "Unity", "Value", "Video", "Visit", "Voice", "Waste", "Watch", "Water", "While", "White", "Whole", "Woman", "World", "Youth"]
chosenwordprint = words[random.randint(0, len(words) - 1)]
chosenword = Convert(chosenwordprint.lower()) #chosenword is stored separately from chosenwordprint; as the chosenword variable is edited throughout the game while chosenwordprint is maintained for console feedback purposes.
wordlecounted = ["false", "false", "false", "false", "false"] #this keeps track of whether each letter in the word has already been guessed correctly so that for future guesses it is not re-counted as correct.
#print(chosenword)
print("Welcome to hangman! What gamemode would you like to play? (Classic, Word, Wordle, or Hard Wordle)")
response = input()
#Gamemode selection, asks the player if they want to play Classic mode, in which the player guesses 1 letter at a time, or 'Word' gamemode, where the player guesses full 5 letter words with correct letters being filled in.
if response.lower() == "classic":
    gamemode = "Classic"
    print("Classic gamemode selected, in this version you'll guess individual letters until the full word is filled in.")
elif response.lower() == "word":
    gamemode = "Word"
    print("Word gamemode selected, in this version you'll guess full 5 letter words and any letters in the correct spot will be filled in.")
elif response.lower() == "wordle":
    gamemode = "Wordle"
    print("Wordle gamemode selected, in this version your guesses will be drawn out and show either red letters for completely incorrect guesses, green for correct, and yellow if it's a correct letter in the wrong spot. Guess in full 5 letter words. If you want to review a prior guess you can re-enter the same guess with no penalty.")
elif response.lower() == "hard wordle":
    gamemode = "Wordle2"
    print("Wordle (Hard) gamemode selected, this version is almost identical to standard Wordle, except every guess progresses the hangman regardless of guess accuracy for added challenge.")
else:
    gamemode = "Classic"
    print("Response not recognized; defaulting to Classic gamemode.")

#Gallows are drawn on startup:
penup()
color("brown")
backward(75)
pendown()
right(90)
forward(100)
left(90)
forward(50)
backward(100)
forward(50)
left(90)
forward(250)
right(90)
forward(100)
right(90)
forward(25)
color("black")

#Blank letter dashes are drawn at the bottom on startup:
penup()
setposition(-175, -190)
left(90)
for i in range(5):
    pendown()
    forward(50)
    penup()
    forward(25)
    
#Player is prompted to guess the word and outcome is determined:
while ((hangmanprog <= 6) and (correctscore <= 4)):
        print("Enter your guess of the word/letter. You can also use '/guesses' to check what words you've already guessed, or '/speed' to change the game speed.")
        response = input()
        correct = "false"
        if response == "/speed": #Command to allow the player to adjust the speed at which the turtle operates
            print("What would you like to set the game speed to? (0 - 10)")
            speed(int(input()))
        elif response == "/guesses": #Command to allow the player to view their past guesses
            print("List of words already guessed:")
            print(guesses)
        else:
            if gamemode == "Word":
                while len(response) != 5: #Ensures that the players guess is 5 characters long, otherwise they are prompted to enter a new response
                    print("Your guess must be 5 letters long and contain no numbers, please enter a new guess.")
                    response = input()
                wordcheck()
            elif gamemode == "Classic":
                while len(response) != 1: #Ensures that the players guess is 1 character long, otherwise they are prompted to enter a new response
                    print("Your guess must be a single letter and contain no numbers, please enter a new guess.")
                    response = input()
                lettercheck()
            elif gamemode == "Wordle":
                while len(response) != 5:
                    print("Your guess must be 5 letters long and contain no numbers, please enter a new guess.")
                    response = input()
                wordlecheck("easy")
            elif gamemode == "Wordle2":
                while len(response) != 5:
                    print("Your guess must be 5 letters long and contain no numbers, please enter a new guess.")
                    response = input()
                wordlecheck("hard")
            guesses.append(response) #Adds the players guess to the list of guesses for them to check with the /guesses command
            if (correct != "true") and (correctscore != 5): #Progresses the stage of the hangman if there was not a new correct letter guessed
                hangmanprog += 1
                hangman(hangmanprog)
            if correctscore > 4: #The player wins if they get all letters correct.
                print("The word was " + chosenwordprint + ", you won!")
