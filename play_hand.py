# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 21:16:34 2018

@author: 583185
"""

#Make bets on our intial hands and see if we won

def play_hand(players,starting_money,hands,table_min):
    from deal_hand import simple_hand
    from read_hand import read_hand
    from read_hand_flop import read_hand_flop
    from read_hand_river import read_hand_river
    
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
    poker_hands={'high card':1,'pair':2,'Two pair':3,'Three of a kind':4,'Straight':5,'Flush':6,'Full House':7,'Four of a kind':8,'Straight Flush':9,'Royal Flush':10}
    #Here's how payouts work. You make 1:1 on your ante and playbets. Your blind (which = ante) pays out at these ratios.
    payout_value={'high card':-1,'pair':-1,'Two pair':-1,'Three of a kind':-1,'Straight':1,'Flush':1.5,'Full House':3,'Four of a kind':10,'Straight Flush':50,'Royal Flush':500}

    for h in range(0,hands):
        #set up initial money
        if hands_played==0:
            for x in range(0,players):
                players_list.append("player{0}".format(x))
                players_money[players_list[x]]=starting_money
        #Not sure why I need to re-initialize the deck everytime 
        deck=[Card(value,suit) for value in card_value for suit in suits]
        hand=simple_hand(deck,players)
        #player initial hands
        players_hand=read_hand('players',hand,players)
        
        #player flop hands
        players_hand_flop=read_hand_flop('players',hand,players)
        
        #player final hand
        players_hand_final=read_hand_river('players',hand,players)
        
        #dealer hand
        dealers_hand=read_hand_river('dealer',hand,players)
        
        #re-initialize bets and hands
        
        bets={}
        final_hand={}
        flop_hand={}
        
        #put the dealer's hand into the final results so we can do everything in the next for loop
        
        final_hand['dealer']={'hand':dealers_hand['dealer_hand']['hand'],'value':dealers_hand['dealer_hand']['value'],'hv':poker_hands[dealers_hand['dealer_hand']['hand']]}

        for x in range(0,players):
            current_player=players_list[x]
            #ante and blind bets
            bets[current_player]=(2*table_min)
            players_money[current_player]-=(2*table_min)
            
            
            
            #Initial cards bet
            #this loop is just looking at our own cards, no knowledge of other players
            if players_hand[current_player]['hand']=='pair':
                bets[current_player]+=(4*table_min)
                players_money[current_player]-=(4*table_min)
            elif players_hand[current_player]['hand']=='high card' and players_hand[current_player]['value']>=12:
                bets[current_player]+=(3*table_min)
                players_money[current_player]-=(3*table_min)
                
            
            #Assign flop hand values
            flop_hand[current_player]={'hand':players_hand_flop[current_player]['hand'],'value':players_hand_flop[current_player]['value'],'hv':poker_hands[players_hand_flop[current_player]['hand']]}
            
            #Assign final hand values
            final_hand[current_player]={'hand':players_hand_final[current_player]['hand'],'value':players_hand_final[current_player]['value'],'hv':poker_hands[players_hand_final[current_player]['hand']]}
            
            #new loop for community bets
            if bets[current_player] == 0 and flop_hand[current_player]['hv']> 1:
                bets[current_player]+=(2*table_min)
                players_money[current_player]-=(2*table_min)
                
            #Loop for final bets
            if bets[current_player] == 0 and final_hand[current_player]['hv'] > 1:
                bets[current_player]+=(table_min)
                players_money[current_player]-=(table_min)
            
            #Deciding the winners and calculating payouts
            
            #straight win and qualifies
            if final_hand[current_player]['hv'] > final_hand['dealer']['hv'] and final_hand['dealer']['hv']>1:
                print(current_player,"won")
                #payout = 1:1 for ante (if qualify) and play bets. Blind can either push or payout to above
                players_money[current_player]+=((bets[current_player]*2)+(payout_value[final_hand[current_player]['hand']]*table_min))
            #straight win not qualifies
            elif final_hand[current_player]['hv'] > final_hand['dealer']['hv'] and final_hand['dealer']['hv']<2:
                print(current_player,"won")
                #need to figure out bet payout in more deal, with variable payouts.
                players_money[current_player]+=(((bets[current_player]*2)+(payout_value[final_hand[current_player]['hand']]*table_min))-table_min)
            #tie, player wins tie breaker qualifies
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] > final_hand['dealer']['value'] and final_hand['dealer']['value']>1:
                print(current_player,'won')
                players_money[current_player]+=((bets[current_player]*2)+(payout_value[final_hand[current_player]['hand']]*table_min))
            #tie, player wins tie braker not qualifies
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] > final_hand['dealer']['value'] and final_hand['dealer']['value']<2:
                print(current_player,'won')
                players_money[current_player]+=(((bets[current_player]*2)+(payout_value[final_hand[current_player]['hand']]*table_min))-table_min)
            #tie, player ties tie breaker --- this case isn't right for high cards
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] == final_hand['dealer']['value']:
                print(current_player,'tie')
                players_money[current_player]+=(bets[current_player])
            #tie, player losses tie breaker dealer qualifies
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] < final_hand['dealer']['value'] and final_hand['dealer']['value']>1:
                players_money[current_player]=players_money[current_player]
            #tie, player losses tie breaker not qualifies
            elif final_hand[current_player]['hv']== final_hand['dealer']['hv'] and final_hand[current_player]['value'] < final_hand['dealer']['value'] and final_hand['dealer']['value']<2:
                players_money[current_player]=(players_money[current_player]+table_min)
            #loss qualifies
            elif final_hand[current_player]['hv'] < final_hand['dealer']['hv'] and final_hand['dealer']['value']>1:
                players_money[current_player]=players_money[current_player]
            #loss not qualifies
            elif final_hand[current_player]['hv'] < final_hand['dealer']['hv'] and final_hand['dealer']['value']<2:
                players_money[current_player]=(players_money[current_player]+table_min)

        print(final_hand)
        print('Flop was',vars(hand['flop'][0]),vars(hand['flop'][1]),vars(hand['flop'][2]),'Draw was',vars(hand['draw'][0]),vars(hand['draw'][1]))
        print(players_money)
        hands_played+=1
        

        
    
            
    
        
