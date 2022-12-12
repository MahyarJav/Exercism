"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
from statistics import median, mean


def get_rounds(number):
    return list(range(number, number+3))


def concatenate_rounds(rounds_1, rounds_2):
    return list(rounds_1 + rounds_2)


def list_contains_round(rounds, number):
    return bool(number in rounds)


def card_average(hand):

    return mean(hand)


def approx_average_is_average(hand):
    return (hand[0] + hand[-1]) / 2 == mean(hand) or median(hand) == mean(hand)


def average_even_is_average_odd(hand):
    even_numbers = hand[::2]
    odd_numbers = hand[1::2]
    return mean(even_numbers) == mean(odd_numbers)


def maybe_double_last(hand):
    return hand if hand[-1] != 11 else hand[:-1] + [22]
