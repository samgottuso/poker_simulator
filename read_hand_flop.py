# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:39:20 2018

@author: 583185
"""


#Getting rid of our outside betting logic for testing the main play_hand script

#Checking what cards people have
def read_hand_flop(version,hand,players):
    #importing functions
    from check_hands import check_flush
    from check_hands import check_straight
    from check_hands import check_straightflush
    from check_hands import check_fourofakind
    from check_hands import check_fullhouse
    from check_hands import check_threeofakind
    from check_hands import check_twopair
    from check_hands import check_pair
    
    
    players_list=[]
    players_flop={}
    flop_cards=hand['flop']
    flop_values=[]
    flop_suits=[]
    for i in range(0,3):
        flop_values.append(vars(flop_cards[i])['value'])
        flop_suits.append(vars(flop_cards[i])['suit'])
    if version=='players':
        for x in range(0,players):
            player_value=[]
            player_suit=[]
            players_list.append("player{0}".format(x))
            current_player=players_list[x]
            card1=vars(hand[current_player][0])
            card2=vars(hand[current_player][1])
            max_value=max(card1['value'],card2['value'])
            #creating lists of hands
            player_value.append(card1['value'])
            player_value.append(card2['value'])
            player_suit.append(card1['suit'])
            player_suit.append(card2['suit'])
            
            hand_value=player_value+flop_values
            hand_suit=player_suit+flop_suits
            #I'm gonna break the checks into individual functions, inspired by this script https://github.com/jfilliben/poker-sim/blob/master/pokersim.py
            
            if check_straightflush(hand_value,hand_suit) == True:
                players_flop[current_player]={'hand':'Straight Flush','value':max(player_value),'suit':'N/A'}
            elif check_fourofakind(hand_value) == True:
                players_flop[current_player]={'hand':'Four of a kind','value':max(player_value),'suit':'N/A'}
            elif check_fullhouse(hand_value) == True:
                players_flop[current_player]={'hand':'Full House','value':max(player_value),'suit':'N/A'}
            elif check_flush(hand_suit) == True:
                players_flop[current_player]={'hand':'Flush','value':max(player_value),'suit':player_suit[0]}
            elif check_straight(hand_value) == True:
                players_flop[current_player]={'hand':'Straight','value':max(player_value),'suit':'N/A'}
            #if the hand is not 5 cards, then I should just use the player's highest card, as other cards would be shared with the dealer
            elif check_threeofakind(hand_value) == True:
                players_flop[current_player]={'hand':'Three of a kind','value':max_value,'suit':'N/A'}
            elif check_twopair(hand_value) == True:
                players_flop[current_player]={'hand':'Two pair','value':max_value,'suit':'N/A'}
            elif check_pair(hand_value) == True:
                players_flop[current_player]={'hand':'pair','value':max_value,'suit':'N/A'}
            #I think we actually just need the highest card in the player's hand... everything else will be shared if there's no other hand that can be made between dealer and player
            else:
                players_flop[current_player]={'hand':'high card','value':max_value,'suit':'N/A'}
            
    elif version == 'dealer':
        for x in range(0,players):
            player_value=[]
            player_suit=[]
            card1=vars(hand['dealer_hand'][0])
            card2=vars(hand['dealer_hand'][1])
            max_value=max(card1['value'],card2['value'])
            player_value.append(card1['value'])
            player_value.append(card2['value'])
            player_suit.append(card1['suit'])
            player_suit.append(card2['suit'])
            
            hand_value=player_value+flop_values
            hand_suit=player_suit+flop_suits
            #I'm gonna break the checks into individual functions, inspired by this script https://github.com/jfilliben/poker-sim/blob/master/pokersim.py
            
            if check_straightflush(hand_value,hand_suit) == True:
                players_flop['dealer_hand']={'hand':'Straight Flush','value':max(player_value),'suit':'N/A'}
            elif check_fourofakind(hand_value) == True:
                players_flop['dealer_hand']={'hand':'Four of a kind','value':max(player_value),'suit':'N/A'}
            elif check_fullhouse(hand_value) == True:
                players_flop['dealer_hand']={'hand':'Full House','value':max(player_value),'suit':'N/A'}
            elif check_flush(hand_suit) == True:
                players_flop['dealer_hand']={'hand':'Flush','value':max(player_value),'suit':player_suit[0]}
            elif check_straight(hand_value) == True:
                players_flop['dealer_hand']={'hand':'Straight','value':max(player_value),'suit':'N/A'}
            #if the hand is not 5 cards, then I should just use the player's highest card, as other cards would be shared with the dealer
            elif check_threeofakind(hand_value) == True:
                players_flop['dealer_hand']={'hand':'Three of a kind','value':max_value,'suit':'N/A'}
            elif check_twopair(hand_value) == True:
                players_flop['dealer_hand']={'hand':'Two pair','value':max_value,'suit':'N/A'}
            elif check_pair(hand_value) == True:
                players_flop['dealer_hand']={'hand':'pair','value':max_value,'suit':'N/A'}
            #I think we actually just need the highest card in the player's hand... everything else will be shared if there's no other hand that can be made between dealer and player
            else:
                players_flop['dealer_hand']={'hand':'high card','value':max_value,'suit':'N/A'}
    
    return(players_flop)
        
