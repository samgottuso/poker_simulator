# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:17:14 2018

@author: 583185
"""

def check_flush(hand_suit):
    suits=['club','spades','diamonds','hearts']
    for i in suits:
        if hand_suit.count(i) >= 5:
            return True
        return False

def check_straight(hand_value):
    #create a set of values
    set_vals=list(set(hand_value))
    #figure out the lowest 5 cards and highest 5 cards
    if len(set_vals) >=5:
        low_set=set_vals[0:5]
        high_set=set_vals[(len(set_vals)-5):len(set_vals)]
        if (max(low_set)-min(low_set)== 4) or (max(high_set)-min(high_set)==4 ):
            return True
    return False

def check_straightflush(hand_value,hand_suit):
    if check_flush(hand_suit) == True and check_straight(hand_value) == True:
        return True
    return False

def check_fourofakind(hand_value):
    for i in set(hand_value):
        if hand_value.count(i) == 4:
            return True
    return False

def check_fullhouse(hand_value):
    val1=list(set(hand_value))[0]
    val2=list(set(hand_value))[1]
    if (hand_value.count(val1) == 3 or hand_value.count(val2) == 3) and (hand_value.count(val1)==2 or hand_value.count(val2)==2) and val1 != val2:
        return True
    return False

def check_threeofakind(hand_value):
    for i in set(hand_value):
        if hand_value.count(i) == 3:
            return True
    return False

def check_twopair(hand_value):
    vals=list(set(hand_value))
    #need to figure out that I'm able to figure out which hands are the highest
    vals.sort(reverse=True)
    pair_counter=0
    for i in vals:
        if hand_value.count(i) == 2:
            pair_counter +=1
    if pair_counter >= 2:
        return True
    return False

def check_pair(hand_value):
    vals=list(set(hand_value))
    for i in vals:
        if hand_value.count(i) == 2:
            return True
    return False




    
            
    

