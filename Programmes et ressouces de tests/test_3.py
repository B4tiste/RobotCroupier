 

deck = ["a", "b", "c", "d"]
deck_m = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]

print(len(deck_m))

print("Deck n°1 :")
print(deck)

print("Deck n°2 :")
print(deck_m)

length = len(deck)

for i in range(length):
    deck_m[i] = deck[i]

print("\nDeck et deck_m apres deck_m=deck, case par case")
print(deck)
print(deck_m)

deck_m[2] = "e"

print(deck_m[4])


print(deck)
print(deck_m)