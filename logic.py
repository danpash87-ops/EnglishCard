from models import Card
from random import choices
from built_in_words import BUILT_IN_WORDS

class CardManager:
    def __init__(self):
        self.cards = []
        self.categories = []
        self.load_categories = list(set([card_list[-1] for card_list in BUILT_IN_WORDS]))

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def create_card(self, rus, eng, category):
        for existing_card in self.cards:
            if existing_card.rus == rus or existing_card.eng == eng:
                return
        new_card = Card(rus, eng, category)
        self.add_category(new_card.category)
        self.cards.append(new_card)

    def delete_card(self, card_in):
        if card_in in self.cards:
            self.cards.remove(card_in)
            last_in_category = [card.category for card in self.cards if card.category == card_in.category]
            if not last_in_category:
                self.categories.discard(card_in.category)
        else:
            raise ValueError('Card not found')

    def delete_all_cards(self):
        self.cards = []
        self.categories = set()

    def get_random_card(self, category):
        if category == 'all':
            if not self.cards:
                return None
            return choices(self.cards, weights=[card.level for card in self.cards])[0]
        else:
            in_category_list = [card for card in self.cards if card.category == category]
            if not in_category_list:
                return None
            return choices(in_category_list, weights=[card.level for card in in_category_list])[0]


    def load_category_from_file(self, category):
        for card in BUILT_IN_WORDS:
            if card[-1] == category:
                self.create_card(*card)


















