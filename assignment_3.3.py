# 3.3 Write a program to prompt for a scoreInt between 0.0 and 1.0. 
# If the scoreInt is out of range, print an error. 
# If the scoreInt is between 0.0 and 1.0, print a grade using the following table:
# scoreInt Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a scoreInt of 0.85.

score = input("Enter score: ")

try:
    scoreInt = float(score)
    if ( scoreInt > 0.0 and scoreInt < 1.0 ):
        if (scoreInt >= 0.9):
            print('A')

        elif(scoreInt >= 0.8):
            print('B')

        elif(scoreInt >= 0.7):
            print('C')

        elif(scoreInt >= 0.6):
            print('D')

        elif(scoreInt < 0.6):
            print('F')
        else:
            print('input is out of range')            
    else:
        print('input is out of range')

except:
    print('input is invalid')
    exit()