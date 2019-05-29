from pygame import mixer

def checkSpelling(userInput):
	if userInput == "damian sandhu-franceschi":
		print("You win!!! we don't give out prizes though... sooooo please leave")
		quitGame()
	else:
		print("So close!!! (Just kidding... or am I)")

def playAudio(times):
	mixer.music.play(times, 0)
def quitGame():
	exit()


print("Welcome to spell my name!\nA game that came from a joke and years of people spelling my name wrong\n\n")

userInput = ""
mixer.init()
mixer.music.load("myname.mp3")
playAudio(2)

while userInput.lower() != 'q':
	userInput = str(input(("Enter L to hear my name again, Q if you want to quit or type a guess and hit enter:\n"))).lower()
	
	if userInput == 'q':
		quitGame()
	elif userInput == 'l':
		playAudio(1)
	else:
		checkSpelling(userInput)    
