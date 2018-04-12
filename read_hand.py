# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:01:34 2018

@author: 583185
"""

#Getting rid of our outside betting logic for testing the main play_hand script

#Checking what cards people have
def read_hand(version,hand,players):
    players_list=[]
    players_initial={}
    if version=='players':
        for x in range(0,players):
            players_list.append("player{0}".format(x))
            card1=vars(hand[players_list[x]][0])
            card2=vars(hand[players_list[x]][1])
            max_value=max(card1['value'],card2['value'])
            if (card1['value'])==card2['value']:
#                print("Pair of ",card1['value'])
                players_initial[players_list[x]]={'hand':'pair','value':max_value,'suit':'N/A'}
#            elif (card1['value']-card2['value']==abs(1)):
##                print("Outside straight draw")
#                players_initial[players_list[x]]={'hand':'outside straight','value':max_value,'suit':'N/A'}
        #assuming that a 10 or higher is better than an outside flush draw, might have to revisit it
            elif (card1['value'] >= 10 or card2['value']>=10):
#                print("high card of", max_value)
                players_initial[players_list[x]]={'hand':'high card','value':max_value,'suit':'N/A'}
#            elif (card1['suit']==card2['suit']):
##                print("Flush draw")
#                players_initial[players_list[x]]={'hand':'outside flush','value':max_value,'suit':card1['suit']}   
            else:
#                print (max(card1['value'],card2['value']))
                players_initial[players_list[x]]={'hand':'high card','value':max_value,'suit':'N/A'}
   
    elif version == 'dealer':
    #find if there are any pairs or outside straight draws or flush draws
        for x in range(0,players):
            card1=vars(hand['dealer_hand'][0])
            card2=vars(hand['dealer_hand'][1])
            max_value=max(card1['value'],card2['value'])
            if (card1['value'])==card2['value']:
#                print("Pair of ",card1['value'])
                players_initial['dealer_hand']={'hand':'pair','value':max_value,'suit':'N/A'}
#            elif (card1['value']-card2['value']==abs(1)):
##                print("Outside straight draw")
#                players_initial['dealer_hand']={'hand':'outside straight','value':max_value,'suit':'N/A'}
        #assuming that a 10 or higher is better than an outside flush draw, might have to revisit it
            elif (card1['value'] >= 10 or card2['value']>=10):
#                print("high card of", max_value)
                players_initial['dealer_hand']={'hand':'high card','value':max_value,'suit':'N/A'}
#            elif (card1['suit']==card2['suit']):
##                print("Flush draw")
#                players_initial['dealer_hand']={'hand':'outside flush','value':max_value,'suit':card1['suit']}
            else:
#                print (max(card1['value'],card2['value']))
                players_initial['dealer_hand']={'hand':'high card','value':max_value,'suit':'N/A'}
    
    return(players_initial)
        
        
