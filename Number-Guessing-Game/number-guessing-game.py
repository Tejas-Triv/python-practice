import random

title_line = '=' * 184

print ('Welcome to Number Guessing Game!')
print ('Rules:','You Keep Guessing till you get the correct number')
print ('Guidelines:','Too Low/Too High --> More than 10 Away','Low/High--> Less Than 10 Away',sep='\n')
print (title_line)

while True:

    secret_number = random.randint(1,100)
    num_tries = 0
    
    while True:
        guessed_number = int(input('enter number between 1 and 100 (incl both)'))
        
        if guessed_number < 1 or guessed_number > 100:
            print ('Please Enter Appropriate Number')
            print (title_line)
            
            continue

        num_checker = secret_number - guessed_number
        num_tries += 1
            
        if (num_checker) > 10:
            print ('Too Low')
            print (title_line)
        
        elif (num_checker) > 0:
            print ('Low')
            print (title_line)

        elif (num_checker) < -10:
           print ('Too High')
           print (title_line)

        elif (num_checker) < 0:
            print ('High')
            print (title_line)

        else:
            print ('Congratulations You Win!! You Took',num_tries,'tries.')
            print (title_line)

            while True:
                
                play_again = input('Do You Want To Play Again? (y/n)')
                print (title_line)

                if play_again.lower() not in ['y','n']:
                    print ('Please Enter Correct Response')

                else:
                    break

            break
        
    if play_again.lower()=='n':
        print ('Thanks For Playing!')
        print (title_line)

        break
