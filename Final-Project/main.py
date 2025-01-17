# Kayla Jones
# Final Project

import random


# simulates dealing a card, returns a random number
# between 1-11, representing the cards in Blackjack
def deal_card():
    return random.randint(1, 11)


# calculates the total value of a hand;
# treats aces as 11 if it works in the
# player/dealer's favor
def calculate_hand_value(hand):
    total_value = sum(hand)
    num_aces = hand.count(11)  # count aces (value = 11)

    # adjust ace values from 11 to 1 if the total value exceeds 21
    while total_value > 21 and num_aces > 0:
        total_value -= 10  # change ace value from 11 to 1
        num_aces -= 1

    return total_value


# simulates Blackjack and stores the results
# for each round
def simulate_blackjack(num_hands):
    results_table = {}

    # iterate over each starting hand value from 4 to 22
    for starting_value in range(4, 23):
        results_hit = {'win': 0, 'draw': 0, 'loss': 0}
        results_stand = {'win': 0, 'draw': 0, 'loss': 0}

        for _ in range(num_hands):
            # initialize player's hand with the starting value
            player_hand = [starting_value]
            dealer_hand = [deal_card()]

            # simulate hitting scenario
            while calculate_hand_value(player_hand) < 17:
                player_hand.append(deal_card())
                if calculate_hand_value(player_hand) > 21:
                    results_hit['loss'] += 1
                    break
            else:
                player_value_hit = calculate_hand_value(player_hand)
                dealer_value = calculate_hand_value(dealer_hand)
                if player_value_hit <= 21 and dealer_value < player_value_hit:
                    results_hit['win'] += 1
                elif player_value_hit == dealer_value:
                    results_hit['draw'] += 1
                else:
                    results_hit['loss'] += 1

            # simulate standing scenario
            player_value_stand = calculate_hand_value(player_hand)
            while calculate_hand_value(dealer_hand) <= 16:
                dealer_hand.append(deal_card())
                if calculate_hand_value(dealer_hand) <= 21 and calculate_hand_value(dealer_hand) > player_value_stand:
                    results_stand['win'] += 1
                    break
            else:
                dealer_value = calculate_hand_value(dealer_hand)
                if player_value_stand > dealer_value:
                    results_stand['win'] += 1
                elif player_value_stand == dealer_value:
                    results_stand['draw'] += 1
                else:
                    results_stand['loss'] += 1

        # store results for the current starting value
        results_table[starting_value] = {
            'hit': results_hit,
            'stand': results_stand
        }

    return results_table


# simulate 100,000 hands of Blackjack
num_hands = 100000
results = simulate_blackjack(num_hands)

# display results table
print("Starting Value | Strategy | Wins | Draws | Losses")
print("-------------------------------------------------")
for starting_value in range(4, 23):  # formatting the results table
    for strategy in ['hit', 'stand']:
        res = results[starting_value][strategy]
        print(
            f"{starting_value:<14} | {strategy.capitalize():<8} | "
            f"{res['win']:<5} | {res['draw']:<6} | {res['loss']:<7}")
