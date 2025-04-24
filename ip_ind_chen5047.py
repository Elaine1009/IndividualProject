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


import tkinter as tk
from tkinter import messagebox
import pygame
import sys
from collections import Counter
import random

import ip_ind_img_chen5047 as func

#card_buttons = []
card_images = []
model = []
screenX = 900
screenY = 700

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

def sortmycard(random_item): # turn 1D into 2D list
    startid = 0
    endid = 0
    mysortedcards = []
    mycards = random_item[:]
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


def updateCardButton(x, y, card_size, random_items, ishand):
    #global card_buttons
    if len(random_items) == 0:
        return []
    x0 = x
    card_buttons = []
    
    for i in range(0, len(random_items)-1):
        txt = random_items[i]
        id = model.index(txt)
        img = card_images[id]
        scaled_img = pygame.transform.scale(img, card_size)
        rect = scaled_img.get_rect(bottomleft=(x, y))
        
        card_buttons.append((scaled_img, rect))

        x += card_size[0]
        if(x>=(screenX-x0)):
            y+=1.5*card_size[1]
            x = x0
        
    if ishand:
        x += 20
    txt = random_items[len(random_items)-1]
    id = model.index(txt)
    img = card_images[id]        
    scaled_img = pygame.transform.scale(img, card_size)
    rect = scaled_img.get_rect(bottomleft=(x, y))
    card_buttons.append((scaled_img, rect))
    
    return card_buttons

def checkWin(unpairCards, setList):

    if len(setList) != 5:
        return 0

    flat_list = [item for sublist in unpairCards for item in sublist]

    if flat_list[0] == flat_list[1]:
        return 1

    return 0

def displayButtonsMessage(screen, font, message, confirm_button, quit_button):
    screen.fill((30, 120, 30))  # green background
    
    msg_surface = font.render(message, True, (255, 255, 255))
    msg_rect = msg_surface.get_rect(center=(screenX/2, screenY*0.15))
    screen.blit(msg_surface, msg_rect)

    pygame.draw.rect(screen, (70, 130, 180), confirm_button)   # steel blue
    text = font.render("Confirm", True, (255, 255, 255))
    text_rect = text.get_rect(center=confirm_button.center)
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, (255, 0, 0), quit_button)   # red color for the quit button
    quit_text = font.render("Quit", True, (255, 255, 255))
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    screen.blit(quit_text, quit_text_rect)


def main():

    pygame.init()
    past_cards = []
    # # Get full screen size
    # display_info = pygame.display.Info()
    # screen_width = display_info.current_w
    # screen_height = display_info.current_h

    # # Calculate 80% size
    # screenX = int(screen_width * 0.8)
    # screenY = int(screen_height * 0.8)

    pygame.display.set_caption("Card Display")
    global card_images
    cardset = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    global model
    model = ['T', 'I', 'K']
    card_buttons = []
    
    for element in cardset:
        imgtemp = "icons/"+element+".png"
        card_images.append(func.cropImg(imgtemp))

    for i in range(3):
        for j in range(9):
            temp = model[i] +str(j+1)
            cardset.append(temp)
            imgtemp = "icons/"+temp+".png"
            
            card_images.append(func.cropImg(imgtemp))
    
    model = cardset[:]
    cardset = cardset*4
    random_items = random.sample(cardset, 16)
    random_items = sorted(random_items)
    
    for element in random_items:
        cardset.remove(element)
    
    screen = pygame.display.set_mode((screenX, screenY))
    card_size = (48, 75)
    x, y = 30, screenY*0.75
    font = pygame.font.SysFont(None, 30)
    message = "Welcome to Mahjong Practice"
    correct = True

    for j in range(60):
        lst = []
        confirm_button = pygame.Rect(screen.get_width() - 150, screen.get_height() - 60, 120, 40)

        quit_button = pygame.Rect(30, screen.get_height() - 60, 120, 40)
        
        if correct:
            txt = random.sample(cardset, 1)
            random_items.sort()
            random_items.append(txt[0])
            card_buttons = updateCardButton(x, screenY*0.75, card_size ,random_items, 1)
            mycards = sortmycard(random_items)
            checkArray =[]
            for i in range(len(mycards)):
                item, lst = findMostSet(mycards[i], lst)
                checkArray.append(item)
            if checkWin(checkArray,lst):
                print("congrats")
                # root = tk.Tk()
                # messagebox.showinfo("Congratulations", "Congratulations on your achievement!")
                # root.destroy()
                break
        
        pastcard_button = updateCardButton(x, screenY*0.4, (32,50), past_cards, 0)
        
        running = True
        selected_card = 100
        while running:
            
            displayButtonsMessage(screen, font, message, confirm_button, quit_button)
            for id, (img, rect) in enumerate(pastcard_button):
                screen.blit(img, rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    j = 100
                    break

                # Detect mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = False
                    pos = pygame.mouse.get_pos()

                    if confirm_button.collidepoint(pos):
                        
                        if selected_card != 100:
                            running = False
                            clicked = True
                            break
                        
                    elif quit_button.collidepoint(pos):
                        running = False
                        j = 100
                        clicked = True
                        break
                     
                    for idx, (_, rect) in enumerate(card_buttons):
                        if rect.collidepoint(pos):
                            clicked = True   
                            if idx == selected_card:
                                selected_card = 100
                            elif selected_card == 100:
                                selected_card = idx
                            else: 
                                a = random_items[idx]
                                random_items[idx] = random_items[selected_card]
                                random_items[selected_card] = a
                                card_buttons = updateCardButton(30, screenY*0.75, card_size, random_items,1)
                                selected_card = 100
                            break
                    
                    if clicked == False:
                        selected_card = 100
                    
                for id, (img, rect) in enumerate(card_buttons):
                    screen.blit(img, rect)
                    if id == selected_card:
                        pygame.draw.rect(screen, (255, 215, 0), rect, 3)
                pygame.display.flip()

        new_items = random_items[:]
        del new_items[selected_card]
        
        mynewcards = sortmycard(new_items)
        playerlst = []

        for i in range(len(mynewcards)):
            item, playerlst = findMostSet(mynewcards[i], playerlst)
            
        if len(playerlst) < len(lst):
            message = "You might deleted ready set, try again"
            correct = False

        else:
            message = "great move!"
            past_cards.append(random_items[selected_card])
            random_items = new_items[:]
            correct = True

        displayButtonsMessage(screen, font, message, confirm_button, quit_button)
        for id, (img, rect) in enumerate(pastcard_button):
            screen.blit(img, rect)

        for id, (img, rect) in enumerate(card_buttons):
            screen.blit(img, rect)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
