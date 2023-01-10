"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    match card:
        case "J"|"Q"|"K":
            return 10
        case "A":
            return 1
        case _:
            return int(card)
def higher_card(card_one, card_two):
    if (value_of_card(card_one) > value_of_card(card_two)):
        return card_one
    if (value_of_card(card_one) < value_of_card(card_two)):
        return card_two
    return card_one, card_two
def value_of_ace(card_one, card_two):
    sum_of_cards = value_of_card(card_one) + value_of_card(card_two)
    if card_one != "A" != card_two and sum_of_cards < 11:
        return 11
    return 1
def is_blackjack(card_one, card_two):
    return bool(card_one == "A" and value_of_card(card_two) == 10 or card_two == "A" and value_of_card(card_one) == 10)
def can_split_pairs(card_one, card_two):
    return bool(value_of_card(card_one) == value_of_card(card_two))
def can_double_down(card_one, card_two):
    final_value = value_of_card(card_one)+value_of_card(card_two)
    return bool(12 > final_value > 8)
