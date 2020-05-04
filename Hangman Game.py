print(
"""

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝@MrBeast-Anirban
                                                                

""")


import random


WORD = open("Word_list.txt")
content = WORD.read()
word_list = content.lower().splitlines()
assert word_list != content.splitlines(), "This list should be in lower case"
encoded_word, encoded_list = "", []


# Getting user level and turns to guess the word
level = int(input("Please enter the word length greater than 2 that u want to guess :- "))
turns = int(input("\nPlease enter the number of guess you want to make :- "))




#Check wheather the guess is correct or not
def is_guess_correct(target, encoded_list, num):
    # encoded_list is the list of *
    # target is the actual random word
    # num is the actual lenght of the random word

    flag = 0
    dummy_target = [x for x in target]
    #print (dummy_target)
    for i in range (turns):
        alpha_guess = str(input("\nPlease enter your choice --> "))
        if alpha_guess in dummy_target and alpha_guess != '$':
            location = dummy_target.index(alpha_guess)
            
            dummy_target[location] = '$'
            #print(dummy_target)
            
            encoded_list[location] = alpha_guess
            flag += 1
            print(' '.join(encoded_list))
            #flag can only be less or equal to the length of string
            if(flag == num):
                print("\nCongratulations, You Won")
                break
            
        else:
            print("Sorry! You made the wrong choice")
    #print(flag)
    #flag can only be less or equal to the length of string
    if(flag != num):
        print("\nSorry! You Lose\n The word is:- ",target)
            



# word generation and encryption of the words
def generation_of_words(num):
    global encoded_word, encoded_list
    level_word_list = [word for word in word_list if (len(word) == num)]   # list of words as inputted length!
    target = random.choice(level_word_list)   # A random choice from the list of words
    print(target)
    encoded_word = "*" * len(target)  # For making the word look encoded multiply '*' with the length of the word
    encoded_list = [astric for astric in encoded_word]  # List of astric '*'
    # print(encoded_list)
    print(encoded_word)
    if (turns < num):
        print("Please make Number of turns Greater than or Equal to word length")
        exit
    else:
        is_guess_correct(target, encoded_list, num)




#Calling the starting function
generation_of_words(level)



