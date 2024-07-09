import time

time.sleep

print("Hello, Stranger!")
time.sleep(4)
print ("I don't know you, So lets change that, Shall we ?")
time.sleep(4)
print("I have got some questions for you, If you don't mind ?")
time.sleep(4)
name = input("Whats is your first name? ")
time.sleep(4)
print("Ahh.. Hey there",name, ".. Nice to meet you")
time.sleep(4)
print ("My name is Alice, I am a chatbot from the future ... well I like to think so. Anyway")
time.sleep(4)
print("So",name, "..... Hmm, What a Great Name, It's a nice family name" )
print("Sorry to ask you this but....")
time.sleep(8)
age = int(input("How old are you? "))

# Calculation of how old you are in days
days = int(age) * 365.25

if age > 21:

  print("Really .. That doesn't sound right")
  time.sleep(4)
  print("You don't look a day over 21, But I am sure you get told that all the time... ")
else:
  print("Really, Wow so young. Does your parents know your using this app?.")
  time.sleep(4)

print("Did you know that you have been on this planet for" ,days, "days ? ")
time.sleep(4)
print("That doesn't sound like a lot of days, does it?")
time.sleep(4)
print("Well I have a little fun fact for you")
time.sleep(4)
weight = input("How much do you weigh in pounds? ")
time.sleep(4)

# How much you would weigh on the moon calculation
moon = round((int(weight)/9.81 * 1.622), 4)

print("On the moon you would only weigh ", moon,"lbs")
time.sleep(4)
print("One big sneeze or One sneeky silent but violent fart and you'll fly off into space ... byeeeeee!!")
time.sleep(4)
print("Hmm, I wonder how much I would weigh on the moon..... Anyway! ")
time.sleep(4)

def myheight():
  yourheight = int(input("How tall are you in centimeters? "))
  if yourheight > 170:
    print("Wow, you are taller than me, I don't think I like that, well at least you can reach things on the top self. ")
  else:
    print("Aww .. Your a little shorty like a leprechaun, awww sorry .. I guess!! ")

myheight()
time.sleep(4)
print("Did you know, The average height worldwide is 5'7 or 170cm ... Aint that interesting")
time.sleep(4)

print("So I have learned quite alot about you. I am really happy we can be friends. Thanks for taking part in this test.")
time.sleep(4)
print("I have one last question before I give you your final fun fact....")
time.sleep(4)
print("What did you think about this program. A lot of work went into it. Let my creator know if you found the experince 'Good' or 'Bad'. ")
time.sleep(6)
print("OK OK ... Last fun fact, Did you know that the fear of long words is Hippopotomonstrosesquippedaliophobia, I know right!. Feel free to google it. ")
time.sleep(4)
print("Anyway ... it was very nice meeting you and I hope to see you again soon. Goodbye. ")
exit()