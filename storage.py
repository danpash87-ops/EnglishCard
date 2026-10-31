from json import JSONDecodeError
from dataclasses import asdict
import json
from models import Card

def save_all_cards(cards, filename = 'data.json'):
    """Function to save all cards to a json file"""
    if cards is None:
        list_cards = []
    else:
        list_cards = [asdict(card) for card in cards]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(list_cards, f, ensure_ascii=False, indent=4)


def load_all_cards(filename = 'data.json'):
    """Function to load all cards from a json file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            list_cards_json =json.load(f)
            list_cards = [Card(**card) for card in list_cards_json]
            set_categories = sorted(list(set(card.category for card in list_cards)))
            set_categories.insert(0, 'all')

            return [list_cards, set_categories]

    except JSONDecodeError:
        return [[],[]]














