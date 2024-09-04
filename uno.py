import random

# define the UNO deck
colors = ['Red', 'Yellow', 'Green', 'Blue']
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
deck = [f'{color} {value}' for color in colors for value in values] * 2
deck += ['Wild', 'Wild Draw Four'] * 4

# shuffle the deck
random.shuffle(deck)

# draw initial hands for two players
def draw_initial_hand(deck):
    return [deck.pop() for _ in range(7)]

player1_hand = draw_initial_hand(deck)
player2_hand = draw_initial_hand(deck)

# func to display player's hand
def display_hand(player, hand):
    print(f"{player}'s Hand: {', '.join(hand)}")

# draw a card
def draw_card(hand, deck):
    hand.append(deck.pop())

# play a card from hand
def play_card(hand, card):
    hand.remove(card)
    return card

# func to check if a play is valid
def is_valid_play(top_card, card):
    if 'Wild' in card or top_card.split()[0] in card or top_card.split()[1] in card:
        return True
    return False

# func to take a turn
def take_turn(player, hand, deck, top_card):
    display_hand(player, hand)
    valid_moves = [card for card in hand if is_valid_play(top_card, card)]

    if valid_moves:
        chosen_card = random.choice(valid_moves)
        print(f'{player} plays {chosen_card}')
        return play_card(hand, chosen_card)
    else:
        print(f'{player} has no valid moves, drawing a card.')
        draw_card(hand, deck)
        return top_card

# main game loop
def main():
    top_card = deck.pop()
    print(f"Starting card: {top_card}")

    while True:
        top_card = take_turn('Player 1', player1_hand, deck, top_card)
        if not player1_hand:
            print('Player 1 wins!')
            break

        top_card = take_turn('Player 2', player2_hand, deck, top_card)
        if not player2_hand:
            print('Player 2 wins!')
            break

if __name__ == '__main__':
    main()
