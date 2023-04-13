#Ariann Decker
#CIT241-02
#Magic 8 Ball

import random
 
 #Function
def question_func():
# Accept User question Input
    quest = input('Ask the Magic 8 Ball a Question!\n')
 #Shake 
    print("(Shaking...)")
 #Create Responses
    response_list = ["It is certain.","Without a Doubt.","Signs point to yes.","Yes.","Outlook good.",
                "Better not tell you now", "Reply hazy, Ask again later.","No.","Don't count on it.","My sources say no."]

#Generate and print a random response
    random_num = random.choice(response_list)
    print(str(random_num))
# Allow user to ask another question or quit the game
# use if statement

    playagain = input('Ask another question or type quit to exit.\n')

    if(playagain == 'quit'):
        print("Goodbye for now.")

    else: 
        random_num = random.choice(response_list)
        print(str(random_num))

    
question_func()