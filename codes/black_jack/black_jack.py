import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing  = True

class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try: 
            chips.bet = int(input('How many chips would you like to bet ? '))
        except ValueError:
            print('Your bet must be an integer! Try again.')
        else:
            if chips.bet > chips.total or chips.bet<=0:
                print('Your bet cannot exceed your balance and you have to enter a positive bet! Your current balance is: ', chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter '1' or '0' ")

        if x.lower() == '1':
            hit(deck,hand)
        
        elif x.lower() == '0':
            print('You chose to stand. Dealer will hit.')

        else:
            print('Wrong input, please try again.')
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" { hidden card }")
    print('', dealer.cards[1])
    print("\nYour Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer`s Hand:", *dealer.card, sep='\n ')
    print("Dealer`s Hand =", dealer.value)
    print("\nYour Hand:", *player.cards, sep='\n ')
    print("Your Hand=", player.value)

def player_busts(player, dealer, chips):
    print("Your are BUSTED !")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("You are the winner!")
    chips.win_bet()

def dealer_busts(player,dealer, chips):
    print("Dealer has BUSTED !")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer is the winner!")
    chips.lose_bet()

def push(player, dealer):
    print("The match is tie !")



while True:
    print("Hello player")
    print("\t              **********************************************************")
    print("\t                       Welcome to the game Casino - BLACK JACK !                                                     ")
    print("\t              **********************************************************")
    print("\t                                   ***************")
    print("\t                                   * A           *")
    print("\t                                   *             *")
    print("\t                                   *      *      *")
    print("\t                                   *     ***     *")
    print("\t                                   *    *****    *")
    print("\t                                   *     ***     *")
    print("\t                                   *      *      *")
    print("\t                                   *             *")
    print("\t                                   *             *")
    print("\t                                   ***************")


    print('\nRULES: Get as close to 21 as you can but if you get more than 21 you will lose!\n  Aces count as 1 or 11.')

    deck = Deck()
    deck.shuffle()

    player_hand = hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = chips

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

        if player_hand.value <= 21:
            # In Blackjack, the rule for the dealer's play is that they must "hit" (take an additional card) until their hand's value reaches at least 17. 
            # Once the dealer's hand is 17 or higher, they must "stand" (stop taking cards).
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            
            elif dealer_hand.value > player_hand:
                dealer_wins(player_hand, dealer_hand, player_chips)
            
            else:
                push(player_hand, dealer_hand)
    
    print("\nYour current balance stands at", player_chips.total)

    if player_chips.total > 0:
        new_game = input("Would you like to play another hand? Enter '1' for Yes or '0' for No: ")
        if new_game == '1':
            playing = True
            continue
        else:
            print("Thanks for playing!\n"
                "\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                "\t      Congratulations! You won {} coins!\n"
                "\t$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n".format(player_chips.total))
            break
    else:
            print("Oops! You have bet all your chips and we are sorry you can't play more.\n"
                "Thanks for playing! Do come again to Casino BLACK JACK!")
            break
