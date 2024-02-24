card_stack = []

card_stack.append("Jack of Diamonds")
card_stack.append("two of hearts")
card_stack.append("ten of spades")

top_card = card_stack.pop()
print(top_card)
top_card = card_stack[-1]
print(top_card)

if not card_stack:
  print("card stack is empty")
else:
  print(len(card_stack))