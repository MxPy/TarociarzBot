import json
import random

def get_cards(how_many = 1):
    cards = []
    
    with open('cards.json', "r", encoding='utf8') as f:
        for cardsJ in json.load(f):
            cards.append({"title": cardsJ['title'], "description": cardsJ['description']})
    return random.choice(cards)
