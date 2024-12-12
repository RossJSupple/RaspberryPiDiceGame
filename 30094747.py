import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setwarnings(False) # turns off warnings at start of program

GPIO.setmode(GPIO.BCM) # sets pins to Broadcomm

leds = [5,6,12,13,16,17] # sets up a list for correct channels for the leds

for x in range (6):
    GPIO.setup(leds[x],GPIO.OUT) # Sets up pins for output

GPIO.setup(18,GPIO.IN) # setting up the buttons for use within the main loop
GPIO.setup(19,GPIO.IN)

print("Press the Red button to play",'\n',"Press the Blue button to exit", sep = "") # give the user instructions on how to start the game

while True: # using a while loop for a continuos program
    
    blue_but = GPIO.input(18) # assigning the buttons to new variables for easier use
    red_but = GPIO.input(19)
    
    if red_but == True:   # if the red button in pressed the program will run
        sleep(0.2)        # debouncing the button
        roll_times = int(input("How many times would you like to roll (1 or 2): "))   # promptin the user to input how many dice they would like to roll
        print()                                     # blank print statement for spacing in the terminal
        if roll_times == 1:                         # if the user choses one dice the program will run through this if statement
            dice = randint(1,6)                     # assigning a random integer to a new variable
            print("You have rolled", dice)          # printing the random number to the user
            for i in range (dice):                  # using a for loop to turn on the LEDs
                GPIO.output(leds[i], GPIO.HIGH)     # the output is dependant on the outome of the random number in the line above
                sleep(0.2)
            sleep(1.5)                              # lights will stay on for 1.5 seconds
            for x in range (6):                     # using another for loop to turn off LEDs with a range of 6 so all LEDs turn off
                GPIO.output(leds[x], GPIO.LOW)      
        elif roll_times == 2:                       # using an elif statement to proceed with two dice rolls
            dice_one = randint(1,6)                 # assigning two random numbers to two different variables for the double dice roll
            dice_two = randint(1,6)
            print("You have rolled", dice_one, "on dice one and", dice_two, "on dice two")  # printing the numbers contained within the dice rolls
            for i in range (dice_one):              # using a for loop to look for dice_one in the same fasion as the one above to turn on LEDs and then turn them off
                GPIO.output(leds[i], GPIO.HIGH)
                sleep(0.2)
            sleep(1.5)
            for x in range (6):
                GPIO.output(leds[x], GPIO.LOW)
            for i in range (dice_two):              # using another for loop to use dice_two the same as above to turn LEDs on and off
                GPIO.output(leds[i], GPIO.HIGH)
                sleep(0.5)
            sleep(1.5)
            for x in range (6):
                GPIO.output(leds[x], GPIO.LOW)
        print()     # empty print statement for spacing to make the terminal look nicer
        print("Press the Red button to play",'\n',"Press the Blue button to exit", sep = "")    # printing intrustions to the user at the end of the loop so they know they can restart the game
    
    if blue_but == True:                    # if the blue button is pressed instead of red then the program will exit
        sleep(0.3)                          # debouncing the button
        for i in range (i):                 # turning all the LEDs off
            GPIO.output(leds[i], GPIO.LOW)  
        print()                             # empty print statement for spacing
        print("Exiting...")                 # print exiting so the user knows whats happening
        quit()                              # using quit to exit the loop and end the program
            
GPIO.cleanup()                              # using GPIO.cleanup to cleanup the channels on the PI for future use
