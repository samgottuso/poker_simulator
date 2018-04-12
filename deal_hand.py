# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:52:33 2018

@author: 583185
"""
#Imports
import numpy as np
import random

def simple_hand(deck,players):       
    #each player gets too cards + 2 for the dealer and 5 for the community
    hand_size=(players*2)+7
    hand=[deck.pop(random.randrange(len(deck))) for _ in range(hand_size)]
    #Need to take them out of the hand completely
    d_hand=[hand.pop(random.randrange(len(hand))) for _ in range(2)]
    d={'dealer_hand':d_hand}
    players_list=[]
    
    for x in range(0,players):
        players_list.append("player{0}".format(x))
        d[players_list[x]]=[hand.pop(random.randrange(len(hand))) for _ in range(2)]
        print(players_list[x],"hand is",vars(d[players_list[x]][0]),'and',vars(d[players_list[x]][1]))
        
    print('dealer hand is', vars(d_hand[0]),'and',vars(d_hand[1]))
    
    flop=[hand.pop(random.randrange(len(hand))) for _ in range(3)]
    draw=[hand.pop(random.randrange(len(hand))) for _ in range(2)]
    
#    print('flop is',vars(flop[0]),vars(flop[1]),vars(flop[2]))
#    print('Draw is',vars(draw[0]),vars(draw[1]))
    
    community={'flop':flop,'draw':draw}
    
    finalized_hand={**d,**community}
    return(finalized_hand)