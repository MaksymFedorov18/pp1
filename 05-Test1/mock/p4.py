
def f(card_number):
    masked_card= card_number[:2] + '*' * 12 + card_number[-4:]
    return masked_card

print(f('5290312400019022'))