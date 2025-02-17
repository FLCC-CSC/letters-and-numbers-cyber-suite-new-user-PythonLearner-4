# FILE NAME: cyber_suite_new_user.py

# NAME: Michael Orcutt
# DATE: 2/17/2025
# BRIEF DESCRIPTION:  A program to make a new user



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience


# HINT: Tackle this one step at a time. First, just ask the name and the ID number
#       and then print those out. Once you get that working, add in the password.
#
#       Think about how to get the length of the password
#       Then, think about how to print out the Xs. Perhaps you can use string multiplication?



########## ENTER YER CODE BELOW THIS LINE ##########


def new_user():
    from getpass import getpass
    name = input( "Please enter your name: ")
    user_id = input( "Please enter your user id: ")
    password = input( "Please enter your password: ")

    print(f'\nWelcome, {name}. Your ID is {user_id}.\n')

    hidden_password = "X" * len(password)
    
    print(f'PASSWORD: \n{hidden_password}')
    
new_user()


########### END YER CODE ABOVE THIS LINE ###########
    


########################################
#          SAMPLE OUTPUT
########################################

'''
Please enter your name: Dave
Please enter your user id: 12345
Please enter your password: abc123

Welcome, Dave. Your ID is 12345.

PASSWORD: 
XXXXXX
'''

'''
Please enter your name: Katie
Please enter your user id: 13090
Please enter your password: PCT2024

Welcome, Katie. Your ID is 13090.

PASSWORD: 
XXXXXXX
'''

'''
Please enter your name: John
Please enter your user id: 10008
Please enter your password: TheOtherDayISawABearAGreatBigBear

Welcome, John. Your ID is 10008.

PASSWORD: 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''
1. This project has a bit of a speed bump (converting the password to XXXXs). What was your thought process?


My first thought was to use character multiplication. However, to do so, I needed to know the length of the input password each time it was entered. I ran a quick search and found the len( ) method on geeks for geeks and worked with that. It took me a few to times to put it together correctly but I eventually got it.


'''
