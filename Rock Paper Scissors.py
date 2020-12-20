#!/usr/bin/env python
# coding: utf-8

# In[1]:


def takePlayerInput():
    player = "blank"
    while not( player.lower() == "r" or player.lower() == "p" or player.lower() == "s") :
        player = input("Please Enter your input out of - R | P | S = ")
    return player.lower()


# In[4]:


takePlayerInput()


# In[5]:


import random


# In[6]:


def getBotInput():
    lst = ['r','s','p']
    return random.choice(lst)


# In[7]:


getBotInput()


# In[8]:


def checkWinner(player,bot):
    if player == 'r' and bot == "r":
        return "draw"
    elif player == "r" and bot == "p":
        return "bot"
    elif player == "r" and bot == "s":
        return "player"
    elif player == "p" and bot == "s":
        return "bot"
    elif player == "p" and bot == "r":
        return "player"
    elif player == "p" and bot == "p":
        return "draw"
    elif player == "s" and bot == "r":
        return "bot"
    elif player == "s" and bot == "p":
        return "player"
    elif player == "s" and bot == "s":
        return "draw"
    else:
        return "draw"


# In[10]:


checkWinner(player= "r",bot= "s")


# In[11]:


def rockPaperScissor():
    endTheGame = "n"
    player_score = 0 
    bot_score = 0
    while endTheGame.lower() != "y":
        ply = takePlayerInput()
        bt = getBotInput()
        print('Bot Entered - ', bt)
        print(" ")
        winner = checkWinner(player = ply, bot = bt)
        print(" Winner is - ", winner)
        print(" ")
        if winner == "player":
            player_score += 2
        elif winner == "bot":
            bot_score += 2
        else :
            player_score += 1
            bot_score += 1
            
        print("----Score board ----")
        print("---PLAYER -----",player_score)
        print("---Bot --------",bot_score)
        print(" ")
        endTheGame = input("You want to end Y/N - ")
        


# In[12]:


rockPaperScissor()


# In[ ]:




