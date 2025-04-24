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

import math
import tkinter as tk
from tkinter import messagebox
import pygame
import sys
from collections import Counter
import random

import ip_ind_img_chen5047 as func

card_buttons = []
card_images = []
model = []

# 大字 ABCD
# 中發白 EFG
# 筒 T
# 條 I
# 萬 K

# 槓 gang
# 碰 peng
# 吃 chi

# mycards = 1D with all the cards
# mysortedcards = 2D each row with different characters
# items = one row with the same character



# def show_popup():
#     """Creates and displays a pop-up message box."""
#     root.withdraw()
#     response = messagebox.askyesno("Pop-up Title", "Your message here?")
#     if response:
#         print("User clicked Yes")
#     else:
#         print("User clicked No")



# cards should be 2D array
# def isCorrect(cards,mycards, choice):

#     freq1 = Counter(cards[1])
#     freq2 = Counter(cards[2])
#     freq3 = Counter(cards[3])
#     if freq1[choice] == 1 and freq2[choice] == 1 and freq3[choice] == 1:
#         return "Correct!"
    
#     flat_list = [item for row in cards for item in row]

#     freq = Counter(flat_list)




def find3repeat(items, lst): # should input with the same category
    if len(items)<3:
        return items, lst
    char_count = Counter(items)
    most_common_word, count = char_count.most_common(1)[0]
    
    if count >=3:
        lst.append([most_common_word, most_common_word, most_common_word])
        for i in range(3):
            items.remove(most_common_word)
    
    return items, lst


def find3continue(items, lst): # should input with the same category, lst are the sorted ones
    if len(items)<3 or len(items[0])==1:
        return items, lst
    second_chars = [s[1] for s in items]
    nums = sorted(set(second_chars))
    
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])
    
    for i in range(2, len(nums)):
        
        if nums[i-2]+1 == nums[i-1] == nums[i]-1:
            lst.append([items[0][0]+str(nums[i-2]), items[0][0]+str(nums[i-1]), items[0][0]+str(nums[i])])
            items.remove(items[0][0]+str(nums[i-2]))
            items.remove(items[0][0]+str(nums[i-1]))
            items.remove(items[0][0]+str(nums[i]))
            break
    return items, lst

def findMostSet(items, lst):
    itemR, lstR = items[:], lst[:]
    itemR, lstR = find3repeat(itemR, lstR)

    itemC, lstC = items[:], lst[:]
    itemC, lstC = find3continue(itemC, lstC)
    
    if lstR == lst and lstC == lst:
        return items, lst
    
    

    if lstR != lst:
        itemR, lstR = findMostSet(itemR, lstR)
    if lstC != lst:
        itemC, lstC = findMostSet(itemC, lstC)
    
    if len(lstR)>len(lstC):
        return itemR, lstR
    else:
        return itemC, lstC


def sortmycard(mycards): # turn 1D into 2D list
    startid = 0
    endid = 0
    mysortedcards = []
    mycards.sort()
    for i in range(1, len(mycards)):
        if mycards[i-1][0] != mycards[i][0]:
            endid = i
            arr = mycards[startid:endid]
            startid = i
            mysortedcards.append(arr)
    endid = len(mycards)
    arr = mycards[startid:endid]
    mysortedcards.append(arr)
    return mysortedcards

import tkinter as tk
from tkinter import messagebox
def main():

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Congratulations", "Congratulations on your achievement!")
    root.destroy()



    
if __name__ == "__main__":
    main()
