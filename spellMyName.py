import os

def checkSpelling(userInput):
    if userInput == "damian sandhu-franceschi":
        playAudio("yes.mp3")
        print("You win!!! we don't give out prizes though... so please leave")
        quitGame()
    else:
        playAudio("no.mp3")
        print("So close!!! (Just kidding... or am I)")

def playAudio(soundFile):
    os.system("afplay " + soundFile)
def quitGame():
    exit()


print("Welcome to spell my name!\nA game that came from a joke and years of people spelling my name wrong\n\n")

userInput = ""
playAudio("myname.mp3")

while userInput.lower() != 'q':
    userInput = str(input(("Enter L to hear my name again, Q if you want to quit or type a guess and hit enter:\n"))).lower()
    
    if userInput == 'q':
        quitGame()
    elif userInput == 'l':
        playAudio("myname.mp3")
    else:
        checkSpelling(userInput)    
