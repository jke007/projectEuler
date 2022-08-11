import csv
from collections import Counter

file = 'Difficulty10/Poker/Poker.csv'

hands = []

def faceToInt(hand):
    temp = []
    for card in hand:
        if card[0] == 'T':
            temp.append('10'+ card[-1])
        elif card[0] == "J":
            temp.append('11'+ card[-1])
        elif card[0] == 'Q':
            temp.append('12'+ card[-1])
        elif card[0] == 'K':
            temp.append('13'+ card[-1])
        elif card[0] == 'A':
            temp.append('14'+ card[-1])
        else:
            temp.append(card)
    return temp

with open(file, newline = '\n') as pokercsv:
    reader = csv.reader(pokercsv, delimiter=' ')
    for round in reader:
        deal = []
        temp1 =[]
        temp2 =[]
        for i in range(0,5):
            temp1.append(round[i])
        for j in range(5,10):
            temp2.append(round[j])
        player1 = faceToInt(temp1)
        player2 = faceToInt(temp2)
        deal.append(player1)
        deal.append(player2)    
        hands.append(deal)

def checkFlush(hand):
    flush = False
    suits = [h[-1] for h in hand]
    if len(set(suits)) ==1:
        flush = True
    else: return False
    if flush: 
        return 6
    else: return 0

def checkStraight(hand):
    temp = []
    for card in hand: 
        temp.append(int(card[:-1]))
    temp.sort()
    if temp[-1] - temp[0] == 4:
        return 5
    else: return 0

def checkStraightFlush(hand): 
    if checkFlush(hand)==6 and checkStraight(hand) == 5:
        return 9
    else: return 0

def checkRoyalFlush(hand):
    royal = False
    for card in hand: 
        if card[:-1] == '14':
            royal = True
    if royal and checkStraightFlush(hand) == 9:
        return 10
    else: return 0

def checkPair(hand): 
    faces = [f[:-1] for f in hand]
    types = set(faces)
    pairs = [f for f in types if faces.count(f) == 2]
    if len(pairs)!=1: 
        return 0
    else: return 2

def checkTriple(hand): 
    faces = [f[:-1] for f in hand]
    types = set(faces)
    if len(types)!= 3: 
        return 0
    for f in types: 
        if faces.count(f) == 3: 
            return 4
    else: return 0

def checkTwoPair(hand): 
    faces = [f[:-1] for f in hand]
    types = set(faces)
    pairs = [f for f in types if faces.count(f) == 2]
    if len(pairs)!=2: 
        return 0
    else: return 3

def checkFour(hand): 
    faces = [f[:-1] for f in hand]
    types = set(faces)
    if len(types)!=2: 
        return 0
    for f in types:
        if faces.count(f) == 4:
            return 8
    else: return 0

def checkHouse(hand): 
    faces = [f[:-1] for f in hand]
    types = set(faces)
    if len(types) != 2: 
        return 0 
    if len(types) == 2 and checkFour(hand) == 0:
        return 7

def handValue(hand):
    value = 1
    if checkPair(hand)!= 0: 
        value = checkPair(hand)
    if checkTwoPair(hand)!= 0: 
        value = checkTwoPair(hand)
    if checkTriple(hand) != 0:
        value = checkTriple(hand)
    if checkStraight(hand) != 0: 
        value = checkStraight(hand)
    if checkFlush(hand) != 0: 
        value = checkFlush(hand)
    if checkHouse(hand) != 0: 
        value = checkHouse(hand)
    if checkFour(hand) != 0: 
        value = checkFour(hand)
    if checkStraightFlush(hand) != 0: 
        value = checkStraightFlush(hand)
    if checkRoyalFlush(hand) != 0:
        value = checkRoyalFlush(hand)
    return value

def getPairTripleFourHouseValue(hand):
    temp = [card for cards, c in Counter(hand).most_common() for card in [cards] * c]
    pairValue = int(temp[0][:-1])
    return pairValue

def pairTiebreak(deal):
    p1Hand = []
    p2Hand = []
    for card in deal[0]:
        p1Hand.append(card[:-1])
    for karte in deal[1]:
        p2Hand.append(karte[:-1])
    p1Hand.sort()
    p2Hand.sort()
    temp1 = [card for cards, c in Counter(p1Hand).most_common() for card in [cards] * c]
    temp2 = [card for cards, c in Counter(p2Hand).most_common() for card in [cards] * c]
    for i in range(-1, -3, -1): 
        if temp1[i] == temp2[i]:
            continue
        if int(temp1[i]) > int(temp2[i]):
            return "P1"
        else: return "P2"

def highCard(deal):
    #determine winner between two high-card hands is the same 
    # procedure of determining winner between two flush hands.
    p1Hand = [] 
    for card in deal[0]:
        p1Hand.append(int(card[:-1]))
    p2Hand = []  
    for card in deal[1]:
        p2Hand.append(int(card[:-1]))
    p1Hand.sort()
    p2Hand.sort()
    for i in range(-1, -5, -1): 
        if p1Hand[i] == p2Hand[i]:
            continue
        if p1Hand[i] > p2Hand[i]:
            return "P1"
        else: return "P2"

def getStraightHigh(hand): 
    top = 0
    for card in hand:
        check = int(card[:-1])
        if check > top: 
            top = check

def getTwoPairValues(hand):
    temp = []
    for card in hand: 
        temp.append(int(card[:-1]))
    temp.sort()
    sorted = [card for cards, c in Counter(hand).most_common() for card in [cards] * c]
    lowPair = sorted[0]
    highPair = sorted[2]
    tieBreak = sorted[4]
    return (highPair, lowPair, tieBreak)

def getWinner(deal):
    winner = ""
    p1Score = handValue(deal[0])
    p2Score = handValue(deal[1])
    if p1Score > p2Score:
        winner = "P1"
    elif p2Score > p1Score:
        winner = "P2"
    
    else:
        if p1Score == 1 or p1Score == 6:
            winner = highCard(deal)
        elif p1Score == 2 or p1Score == 4 or p1Score == 7 or p1Score ==8:
            p1Val = getPairTripleFourHouseValue(deal[0])
            p2Val = getPairTripleFourHouseValue(deal[1])
            if p1Val > p2Val: 
                winner = "P1"
            elif p2Val > p1Val: 
                winner = "P1"
            else: 
                winner = pairTiebreak(deal)
        elif p1Score == 3:
            p1Values = getTwoPairValues(deal[0])
            p2Values = getTwoPairValues(deal[1])

            if p1Values[0]> p2Values [0]: 
                winner = "P1"
            elif p1Values[0] < p2Values [0]:
                winner = "P2"
            else:
                if p1Values[1] > p2Values[1]:
                    winner = "P1"
                elif p1Values[1] < p2Values [1]:
                    winner = "P2"
                else: 
                    if p1Values[2] > p2Values[2]: 
                        winner = "P1"
                    else: winner = "P2"
    return winner

def countWins(hands):
    count = 0
    for deal in hands: 
        w =getWinner(deal)
        if w == "P1":
            count +=1
    
    print(count)
    

countWins(hands)