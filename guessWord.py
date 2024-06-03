import getpass


print ("***********************************************************")
print("*      welcome to Block Fruit guessor                      *")
print("*                                                          *")
print ("***********************************************************")
print("")
print("")
seceret_word = getpass.getpass( "    enter the fruit: ")
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != seceret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("    enter guess: ")
        guess_count +=1 
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses, You lose!")
else:    
    print("you win!")


    
    