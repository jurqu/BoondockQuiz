print("Welcome! Please take this short quiz to see which boondocks character you are.")
userName = input("Please enter your name: ").title()
print("")
print("Question 1: Why does your family not understand you? ")
print("1: Because they won't listen to what I'm trying to tell them even tho I know what the future holds!!")
print("2: Cuz they don't understand what it's like to be king of the streets, know what I mean?")
print("3: Because they won't just follow directions! My orders are plain and simple!")
print("4: Because they don't understand how much going to this concert will mean to me.")
question1 = int(input("Select 1-4 for your answer: ")) 
print("")

print("Question 2: Someone says your're wanted by the police, how do you respond? ")
print("1: Uh yeah. The government thinks I'm a terrorist now but, I'm retired.")
print("2: Man that's kinda cool though you know? Like woah I be like Tony Montana shooting up people like kaplow! kaplow! I'll take this street cred!")
print("3: Oh god! What did I do to deserve this! Oh Jesus why do you play me like this.")
print("4: WHAT. WHO SAID THAT?! I DIDN'T DO ANYTHING! I swear!")
question2 = int(input("Select 1-4 for your answer: "))
print("")

print("Question 3: Someone drank the last of the orange juice, who was it")
print("1: MY BROTHER.")
print("2: Probably someone who WANTS TO DIE!")
print("3: It was me.")
print("4: BOYS!")
question3 = int(input("Select 1-4 for your answer: ")) 
print("")

print("Question 4: Who's your favorite singer ")
print("1: Elton John")
print("2: The Thugnificent")
print("3: Usher")
print("4: Diana Ross")
question4 = int(input("Select 1-4 for your answer: ")) 
print("")

print("Question 5: Which line would you most likely say?")
print("1: Excuse me. Everyone, I have a brief announcement to make. Jesus was black, Ronald Reagan was the Devil, and the government is lying about 9/11. Thank you for your time and good night.")
print("2: If I were to pee on you right now would you A, smile and ask for more; or B, get the hell out of the way?")
print("3: Y'all need to start appreciating your Grandaddy! I went and spent your inheritance on this beautiful house in this neighborhood! And all I ask you to do is act like you got some class!")
print("4: Nowadays people think HO HO HO means Nicole Richie standing next to the Hilton Sisters! But that ain't no HO HO HO! I'm talking about the REAL HO HO HO!!!")
question5 = int(input("Select 1-4 for your answer: ")) 
print("")


while question1 == 1 and question2 == 1 and question3 == 1 and question4 == 1 and question5 == 1:
    print(userName + " you are Huey")
    break
while question1 == 2 and question2 == 2 and question3 == 2 and question4 == 2 and question5 == 2:
    print(userName + " you are Riely")
    break
while question1 == 3 and question2 == 3 and question3 == 3 and question4 == 3 and question5 == 3:
    print(userName + " you are Granddad")
    break

while question1 == 4 and question2 == 4 and question3 == 4 and question4 == 4 and question5 == 4:
    print(userName + " you are Jazmine")
    break
