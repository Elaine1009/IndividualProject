"""
Course Number: ENGR 13300
Semester: Spring 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 5.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
    Date:           e.g. 08/29/2024

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""

from PIL import Image
import pygame



def cropImg(imgTitle): 
    img = Image.open(imgTitle)
    cropped = img.crop((img.width*0.18, 0, img.width*0.82, img.height))
    # Convert to Pygame surface
    mode = cropped.mode
    size = cropped.size
    data = cropped.tobytes()
    pygame_img = pygame.image.fromstring(data, size, mode)
    
    return pygame_img


