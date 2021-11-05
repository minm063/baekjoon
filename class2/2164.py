N=int(input())
card=list(range(N, 0, -1))

while len(card)>1:
    card.pop()
    if len(card)<2:
        break
    card.insert(0, card.pop())

print(card[0])