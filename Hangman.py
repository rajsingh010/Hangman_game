import random

pics = ["""
+-------+ 
        |
        |
        |
       ===""", """
+-------+ 
    O   |
        |
        |
       ===""", """
+-------+ 
    O   |
    |   |
        |
       ===""", """
+-------+ 
    O   |
   /|   |
        |
       ===""", """
+-------+ 
    O   |
   /|\  |
        |
       ===""", """
+-------+ 
    O   |
   /|\  |
   /    |
       ===""", """
+-------+ 
    O   |
   /|\  |
   / \  |
       ==="""]

word_list = '''hangman python start java code compiler indent run console terminal problem game navigate tools help view file project structure stop play '''.split(' ')
print("\t\t\t\t\t=============================\n"
      "\t\t\t\t\t||   Welcome to hangaman   ||\n"
      "\t\t\t\t\t=============================\n\n\n"
      "-------------------------->>>>>>>>>>>>>>THIS GAME IS CREATED BY RAJ SINGH<<<<<<<<<<<<--------------------------- \n"
      "-------------------------->>>>>>>>>>>>>>AND IS FREE TO USE<<<<<<<<<<<<<<<<<<<<<<<<<<<---------------------------"
      "\n\n\t=============================================================================================\n"
      "\t||  To play the game you will be provided some underscores the length of underscores will  ||\n"
      "\t||  give you the length of word you have to guess                                          ||\n"
      "\t============================================================================================="
      "\n\n\n\t\t\tPRESS ENTER TO START THE GAME")
start = input()
index = 0
x = 0
run_guess = True
chance = 0
for game in range(22):
    hang = 0
    run_guess = True
    word = list(random.choice(word_list))
    blanks = []
    for j in range(len(word)):
        blanks.append("_")


    def checker():
        global run_guess, hang, chance
        for indexer, i in enumerate(word):
            if i == aws1:
                blanks[indexer] = aws1
                print('good  -->  ' + ''.join(blanks))
        if aws1 not in word:
            print(f'TRY AGAIN! --> {"".join(blanks)}')
            hang += 1
            print(f'\t\t\t\t\t\t\t\t\t\t {pics[hang]}')
    print(f"The word you have to guess is --> {blanks}")
    while run_guess:
        if blanks == list(word):
            print("\t\t\t\t=========================================\n"
                  "\t\t\t\t|| Well Done! You win this guess       ||\n"
                  "\t\t\t\t|| Let's play again                    ||\n"
                  "\t\t\t\t=========================================")
            run_guess = False
            break
        if hang == 6:
            print(f"The word you have to guess was -->  {word}")
            print("\t\t=========================================\n"
                  "\t\t|| OOPS! TRY AGAIN                     ||\n"
                  "\t\t|| Let's play again                    ||\n"
                  "\t\t=========================================")
            break
        try:
            aws1 = str(input())[0]
            er = "`~<,>.?/:;\"'{[}]|\+=_-)(*&^%$#@!0123456789                       "
            if aws1 in er:
                print('Game takes only one character at a time and it should not be special case or spaces or numbers')
                print('Now enter any alphabet ==> abcdefghijklmnopqrstuvwxyz <==')
                
            else:
                checker()
        except IndexError:
            print("Enter any alphabet")
