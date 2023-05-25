# game to use the camera for the user choice

import cv2
from keras.models import load_model
import numpy as np
from time import time
import random as rnd

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


# Get the choice from the computer
def get_computer_choice():
    
    # list of options from which to randomly generate a choice
    options = ["rock", "paper", "scissors"] 

    return rnd.choice(options)

# Get the choice from the user
def get_user_choice():

    classes = ["nothing", "rock", "paper", "scissors"] # complete list of classes for identifying user choice held up to the camera

    # get the numPy array of last snapshot from the camera
    snapshot = get_prediction()

    # find the index of the highest value to identify the choice
    highest = np.argmax(snapshot)
    dprint(highest)
    return classes[highest]


# Use computer and user choices to establish the winner
def get_winner(computer_choice, user_choice):

    global user_wins
    global computer_wins

    # check that the user formed an image to the camera, or that it was identified.
    if user_choice == "nothing":
        return "Cannot identify your choice. Please try again."

    print(f"You: {user_choice}\nMe: {computer_choice}")

    if (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        user_wins += 1
        return "You won!"

    elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
        computer_wins += 1
        return "You lost!"
    else:
        return "It is a tie"


# Play the game by calling the above three functions
def play():

    while True:
        print(get_winner(get_computer_choice(), get_user_choice()))

        # print score so far
        print(f"\nSCORE\nMe: {computer_wins}\nYou: {user_wins}\n")

        # break out if the game has been won
        if user_wins == num_rounds or computer_wins == num_rounds:
            break

        # Give the user the chance to bottle out
        if input("Continue (Y/N)? ").lower() == "n":
            print("Sorry that you didn't want to finish the game. Bye!")
            cleanup()
            return

    # determine who won the game
    if computer_wins > user_wins:
        print("I won the game")
    else:
        print("You won the game")

    cleanup()

# After finishing, release the cap object and destroy all the windows
def cleanup():

    cap.release()
    cv2.destroyAllWindows()


# Catch snapshots of the image and return the list of predictions for each class
def get_prediction():

    count = countdown
    start = time()

    dprint(f"Time is {start}. Starting in {count} seconds...")
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)

        # setup the image to display to the user, complete with text
        setup_image(count, frame)
        
        dprint(f"Current prediction: {type(prediction)} - {prediction}")

        # break if 3 seconds have elapsed
        current = time()
        dprint(f"Time is {current}. Elapsed is {current - start}")
        if (current - start) > 1: # if approximately 1 second has elapsed
            count -= 1
            
            # reset the time to count the next second
            start = time()
            dprint(f"Starting in {count} seconds...")
            if count < cutoff: # give the user a few seconds to form their choice
                break

        cv2.waitKey(1)

    return prediction

def setup_image(count, frame):

    window_name = "Rock, Paper, Scissors" # Window name in which image is displayed
    font = cv2.FONT_HERSHEY_SIMPLEX # font
    org = (50, 50) # location of text
    fontScale = 1 # size of font
    color = (255, 0, 0) # Blue color in BGR
    thickness = 2 # Line thickness of 2 pixels

    if count > 0:
        text = f"Get ready... {str(count)}" # show the countdown
    elif count > cutoff:
        text = "PLAY!"
    else:
        text = "Thank you"
        
    # Use cv2.putText() method
    frame = cv2.putText(frame, text, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)

    # Display the image
    cv2.imshow(window_name, frame)

# print verbosely when __DEBUG__ is set to True
def dprint(line):

    if __DEBUG__:
        print(line)


__DEBUG__ = True # used for generating verbose output
countdown = 5 # number of seconds to count down before play
cutoff = -2 # deadline after countdown reaches zero for forming choice to the camera
num_rounds = 3 # number fo rounds of the game to play
user_wins = 0 # count of user wins
computer_wins = 0 # count of computer wins

# Play the game
print(__name__)
if __name__ == "__main__":
    play()