#program that uses a dictionary as a deck of cards

#imports
import random

def main():
    deck = create_deck()

    deal_cards(deck)


def create_deck():
    deck = {"Ace of Spades":1, '2 of Spades':2, '3 of Spades':3,'4 of Spades':4,
            '5 of Spades':5, '6 of Spades':6,'7 of Spades':7, '8 of Spades':8,
            '9 of Spades':9,'10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,'4 of Hearts':4,
            '5 of Hearts':5, '6 of Hearts':6,'7 of Hearts':7, '8 of Hearts':8,
            '9 of Hearts':9,'10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,'4 of Clubs':4,
            '5 of Clubs':5, '6 of Clubs':6,'7 of Clubs':7, '8 of Clubs':8,
            '9 of Clubs':9,'10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}
    return deck

def deal_cards(deck):
    p1_hand = 0
    p2_hand = 0
    ace = "Ace"

        
    print("Let's Play!")
    print()
    for count in range(len(deck)):
        while p1_hand < 21 and p2_hand < 21:
            card1 = random.choice(list(deck))
            card2 = random.choice(list(deck))
            value2 = deck.pop(card2)
            value1 = deck.pop(card1)
            print(f"P1: " + card1)
            print(f"P2: " + card2)
            print()
            p1_hand += value1
            p2_hand += value2
            if ace in card1 or ace in card2:
                if ace in card1:
                    p1_hand -= value1
                    if p1_hand + 11 > 21:
                        p1_hand += 1
                    else:
                        p1_hand += 11
                elif ace in card2:
                    p2_hand -= value2
                    if p2_hand + 11 > 21:
                        p2_hand += 1
                    else:
                        p2_hand += 11
                    
    print(f"P1 Hand: {p1_hand}")
    print(f"P2 Hand: {p2_hand}")
        

    if p1_hand == 21 or p2_hand == 21:
        if p1_hand == 21 and (p2_hand < 21 or p2_hand > 21):
            print("Player 1 wins")
        elif p2_hand == 21 and (p1_hand < 21 or p1_hand > 21):
            print("Player 2 wins")
    
    elif p1_hand > 21 and p2_hand < 21:
        print("Player 2 wins")
    elif p2_hand > 21 and p1_hand < 21:
        print("Player 1 wins")
    elif p1_hand > 21 and p2_hand > 21:
        print("Neither player wins")
        
    return


if __name__ == "__main__":
    main()
