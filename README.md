# Computer Vision RPS

## Milestone 2 - New files and directories:

### New directory: images, containing images to be used by model:

        nothing.jpg
        paper_1.jpg
        paper_2.jpg
        paper_3.jpg
        rock_1.JPG
        rock_2.jpg
        rock_3.jpg
        scissors_1.jpg
        scissors_2.jpg
        scissors_3.jpg

### New files:

        keras_model.h5 - the model generated from Teachable Machine
        labels.txt - the names of the classes

### Experience so far

Being completely new to all this, I find it intriguing.
The model will clearly be used to interpret images in the game, but, I have no idea how it will do this.
The code can be executed from a Python script, so, I look forward to writing it.

### Modification:

Previous push used images, as I did not have a webcam.
Now that I have one, I have taken pictures from it and removed the images.
A class has been created for images of me holding up the three rock, paper and scissors hand shapes.
A fourth, nothing class has been created that shows me holding up nothing.
The model reads each image and determines which one it is.

## Milestones 3 and 4 - Environment setup and code for playing game
New Conda environment "ComputerVision" setup and the following packages installed:

        opencv-python
        tensorflow
        ipykernel

New file: requirements.txt - contains the output from the "pip list" command to record environment setup

New file: manual_rps.py

        Code for playing the rock, paper, scissors game, consisting of four functions:

        get_computer_choice     - returns randomly generates a choice from the list of three options of rock, paper and scissors
        get_user_choice         - returns user's choice of the three options.
        get_winner              - uses computer and user choices to establish the winner
        play                    - Calls the get_winner function with the arguments returned from the first two.

## Modification to manual_rps.py
list of choices is now placed inside the get_computer_choice function, which was not indicated in original requirement

## Milestone 5 - Completed version of project.

New file: camera_rps.py

        Code for playing the Rock. Paper. Scissors game using images from the user held up to the webcam, consisting of the following functions:

        get_computer_choice():
                Randomly generate a choice from the list of options of rock. paper and scissors

        get_user_choice():
                Calls get_prediction() to get the list of predictions from the webcam.

        get_prediction():
                Enters a while loop to continually capture snaphots from the camera until the countdown
                reaches 0 and the final snapshot is obtained to return to the calling function.

        get_winner(computer_choice, user_choice):
                Uses computer and user choices to establish the winner.

        play():
                Main driver function.
                Continually loops until user decides to end ot one of the players has won three rounds.

        cleanup():
                Ensures objects and windows required for the model are destroyed.

        setup_image(count, frame):
                Sets up the text to display on the image, showing the countdown to start the game and
                capture the user's choice.
                Uses the cv2.putText() class method for this purpose.

        dprint(line):
                If __DEBUG__ is set to True, this function will print out additional information on the program's progress.

### Further development:

        At the moment, the only information displayed on the image is the countdown towards capturing the user's choice, whilst the display of the computer's choice, the score and the opporturtunity to continue the game are displayed on the terminal.

        I would develop this further to display everything on the image, so that user can play the whole
        game without needing to look at the terminal output.
        This could be achieved by seperating out the image-capturing functionality in get_prediction into individual functions. When the while loop in the get_prediction() function is terminated and the prediction is returned for the call to get_winner(), another while loop can be entered into to enable further calls to cv2.putText, to display the score and the prompt for the user to continue. Any entry would then terminate this loop and either end the whole game or return to the top of the loop in the play() function and begin another round.


