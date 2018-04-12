# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 21:16:34 2018

@author: 583185
"""

#Make bets on our intial hands and see if we won

def play_hand(players,starting_money,hands):
    from deal_hand import simple_hand
    from read_hand import read_hand
    
    #we want these things to move from hand to hand
    
    #Set up cards
    class Card:
        def __init__ (self,value,suit):
            self.value=value
            self.suit=suit
        
    suits=['heart','diamond','spade','club']
    card_value=[2,3,4,5,6,7,8,9,10,11,12,13,14]

    players_list=[]
    players_money={}
    hands_played=0
    #create a dictonary that holds all of the poker hand rankings
    poker_hands={'high card':1,'pair':2,'Two pair':3,'Three of a kind':4,'Striaght':5,'Flush':6,'Full House':7,'Four of a kind':8,'Straight Flush':9,'Royal Flush':10}

    for h in range(0,hands):
        #set up initial money
        if hands_played==0:
            for x in range(0,players):
                players_list.append("player{0}".format(x))
                players_money[players_list[x]]=starting_money
        #Not sure why I need to re-initialize the deck everytime 
        deck=[Card(value,suit) for value in card_value for suit in suits]
        hand=simple_hand(deck,players)
        #player hands
        players_hand=read_hand('players',hand,players)
        #dealer hand
        dealers_hand=read_hand('dealer',hand,1)
        
        #re-initialize bets and hands
        
        bets={}
        final_hand={}
        
        #put the dealer's hand into the final results so we can do everything in the next for loop
        
        final_hand['dealer']={'hand':dealers_hand['dealer_hand']['hand'],'value':dealers_hand['dealer_hand']['value'],'hv':poker_hands[dealers_hand['dealer_hand']['hand']]}

        for x in range(0,players):
            current_player=players_list[x]
            #ante bet
            bets[current_player]=+5
            players_money[current_player]-=5
            #Initial cards bet
            #this loop is just looking at our own cards, no knowledge of other players
            if players_hand[current_player]['hand']=='pair':
                bets[current_player]+=20
                players_money[current_player]-=20
            elif players_hand[current_player]['hand']=='high card' and players_hand[current_player]['value']>=12:
                bets[current_player]+=15
                players_money[current_player]-=15
            #Assign our final values
            final_hand[current_player]={'hand':players_hand[current_player]['hand'],'value':players_hand[current_player]['value'],'hv':poker_hands[players_hand[current_player]['hand']]}
            #striaght win
            if final_hand[current_player]['hv'] > final_hand['dealer']['hv']:
                print(current_player,"won")
                #need to figure out bet payout in more deal, with variable payouts, qualifying etc.
                players_money[current_player]+=(bets[current_player]*2)
            #tie, player wins tie breaker
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] > final_hand['dealer']['value']:
                print(current_player,'won')
                players_money[current_player]+=(bets[current_player]*2)
            #tie, player ties tie breaker
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] == final_hand['dealer']['value']:
                print(current_player,'tie')
                players_money[current_player]+=(bets[current_player])
            #tie, player losses tie breaker
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] < final_hand['dealer']['value']:
                players_money[current_player]=players_money[current_player]
            #loss
            elif final_hand[current_player]['hv'] < final_hand['dealer']['hv']:
                players_money[current_player]=players_money[current_player]

        print(final_hand)
        print(players_money)
        hands_played+=1
        

        
    
            
    
        
