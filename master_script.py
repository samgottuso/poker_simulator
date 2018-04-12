# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:13:16 2018

@author: 583185
"""
#Imports
import numpy as np
from numpy import random

#Set up cards
class Card:
    def __init__ (self,value,suit):
        self.value=value
        self.suit=suit
suits=['heart','diamond','spade','club']
card_value=[2,3,4,5,6,7,8,9,10,11,12,13,14]
#and the deck
deck=[Card(value,suit) for value in card_value for suit in suits]

#Should be in play_hand now

##Deal a sample hands
#
#from deal_hand import simple_hand
#
#test_hand=simple_hand(deck,5)

##tell us what those hands are
#from read_hand import read_hand
##player hands
#test_initial=read_hand('players',test_hand,5)
#
##dealer hand
#dealer_initial=read_hand('dealer',test_hand,1)

#Create cash and play a hand

from play_hand import play_hand

play_hand(5,200,100)

    
    
    
    
    