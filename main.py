from storage import load_all_cards, save_all_cards
from logic import CardManager
from ui import run_console_ui

def main():
    print('Запуск EnglishCard')

    loaded_cards = load_all_cards('data.json')


    manager = CardManager()
    manager.cards = loaded_cards[0]
    manager.categories = loaded_cards[1]



    print(f'Загружено карточек: {len(manager.cards)}')

    run_console_ui(manager)

    save_all_cards(manager.cards, 'data.json')
    print('Данные сохранены. До свидания!')

if __name__ == '__main__':
    main()






