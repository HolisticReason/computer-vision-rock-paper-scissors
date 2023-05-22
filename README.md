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

### Milestones 3 and 4 - Environment setup and code for playing game
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

### Modification to manual_rps.py
list of choices is now placed inside the get_computer_choice function, which was not indicated in original requirement