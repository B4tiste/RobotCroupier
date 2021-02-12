import random

deck = ["a", "b", "c", "d"]
print("Deck n°1 :")
print(deck)

deck_m = deck
print("Deck_m avant mélange :")
print(deck_m)

deck_m[2] = "Z"

print("\nDeck Z :")
print(deck)
print("Deck_m Z :")
print(deck_m)

"""
#Melange de deck_m
random.shuffle(deck_m)
print()"""