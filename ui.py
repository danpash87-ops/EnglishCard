def run_console_ui(manager):
    """The main menu of the program."""

    while True:
        print('\n' + '=' * 30)
        print('ГЛАВНОЕ МЕНЮ')
        print('=' * 30)
        print('1. Тренировка')
        print('2. Редактор карт')
        print('3. Выход')
        print('=' * 30)

        choice = input('Выбери пункт (1-3): ').strip()

        if choice == '1':
            list_of_wrongs = training_with_cards(manager)
            if list_of_wrongs:
                work_on_errors(list_of_wrongs)

        elif choice == '2':
            card_redactor(manager)

        elif choice == '3':
            print('~~~ Выход из программы ~~~')
            break

def work_on_errors(list_of_wrongs):
    change = (input('Провести работу над ошибками? "1"-да "0"-нет: '))
    if change == '1':
        while list_of_wrongs:
            for wrong in list_of_wrongs[:]:
                result = checks_word(wrong)
                if result[1] == 'right':
                    list_of_wrongs.remove(wrong)
                    continue
                else:
                    print('Try again!')
    print('Work_on_errors is over')


def training_with_cards(manager):
    if manager.cards:
        continue_with_category = category_change(manager)
        right_word = 0
        wrong_word = []
        while True:
            print('\n' + '=' * 30)
            print('--- ТРЕНИРОВКА ---')

            card = manager.get_random_card(category=continue_with_category)
            if card is None:
                print("В этой категории нет карточек!")
                break

            should_continue = checks_word(card)
            if should_continue[1] == 'right':
                right_word += 1
            elif should_continue[1] == 'wrong':
                wrong_word.append(card)
            print(f'Right words: {right_word}')
            print(f'Wrong words: {len(wrong_word)}')
            if not should_continue[0]:
                print('\n' + '=' * 30)
                print('The session is over! ')
                print('\n' + '=' * 30 + '\n')
                return wrong_word
    else:
        print('Ошибка! Отсутствуют карты!')
        return []



def checks_word(word):
    attempts = 0
    while True:
        word_in = input(f'Word: {word.rus} | Translated: ')

        if word_in == word.eng:
            word.level = max(0.1, word.level - 0.5)
            print('Good!')

            end = input('"1"- продолжить, "0"- остановиться: ')
            if end == '0':
                return [False, 'right']
            elif end == '1':
                return [True, 'right']
        else:
            attempts += 1
            word.level += 1.0

            if attempts == 3:
                print(f'Превышено количество попыток!\nПравильный ответ: {word.eng}')
                return [True, 'wrong']
            print('Incorrect! Try again! attempts: ', attempts)

            end = input('"1"- продолжить, "0"- остановиться: ')
            if end == '0':
                return [False, 'wrong']
            elif end == '1':
                continue


def card_redactor(manager):
    """Card editor menu"""
    list_cards = False
    while True:
        print('\n' + '=' * 30)
        print('--- РЕДАКТОР КАРТ ---')
        print('1. Добавление новой карты')
        print('2. Удаление карты')
        print('3. Удаление всех карт')
        if not list_cards:
            print('4. Показать список карт')
        else:
            print('4. Убрать список карт')
        print('5. Загрузить библиотеки карт')
        print('6. Выход в главное меню')
        print('=' * 30)

        if list_cards:
            word_in_str = 0
            for card in manager.cards:
                if word_in_str < 10:
                    print(card, end = ' | ')
                    word_in_str += 1
                else:
                    print(card, end = '\n')
                    word_in_str = 0

        choice = input('Выбери пункт (1-6): ').strip()

        if choice == '1':
            try:
                rus = input('Введите слово на русском: ')
                eng = input('Введите его перевод на английском: ')
                category = category_change(manager, new_category=True)
                manager.create_card(rus, eng, category)
                print('Карточка успешно создана!')
            except (ValueError, TypeError):
                print('\nОшибка при создании карточки! Возможно вы ввели некорректные символы\nПопробуйте создать карточку заново')

        elif choice == '2':
            delete_card(manager)

        elif choice == '3':
            question = input('Вы уверены, что хотите удалить ВСЕ карты?\n"0"- нет | "1"- да ')
            if question == '0':
                continue
            elif question == '1':
                manager.delete_all_cards()
                print('\n' + '=' * 30)
                print('Все карты удалены!')

        elif choice == '4':
            list_cards = not list_cards

        elif choice == '5':
            load_category(manager)

        elif choice == '6':
            break


def delete_card(manager):
    while True:
        print('\n' + '=' * 30)
        print('УДАЛЕНИЕ КАРТ')
        print('Введите "0" для выхода в меню редактирования')
        for i, card in enumerate(manager.cards, start=1):
            print(f'{i}| {card}')
        num_deleted_card = input('Выберите номер карты для удаления: ')
        if num_deleted_card.isdigit():
            num_deleted_card = int(num_deleted_card)
            if num_deleted_card == 0:
                break
            for i, card in enumerate(manager.cards, start=1):
                if i == num_deleted_card:
                    manager.delete_card(card)
            print('\n' + '=' * 30)
        else:
            print('\n' + '=' * 30)
            print('Введите число!')


def category_change(manager, new_category=False):
    while True:
        print('\n' + '=' * 30)
        print('ВЫБОР КАТЕГОРИИ')
        if new_category:
            print('0| new category')

        if manager.categories:
            for i, category in enumerate(manager.categories, start=1):
                print(f'{i}| {category}')
        category_num = input('Выберите категорию: ')
        if category_num.isdigit():
            category_num = int(category_num)

            if category_num == 0 and new_category:
                manager.add_category(input('Введите название новой категории: '))

            if manager.categories:
                for i, category in enumerate(manager.categories, start=1):
                    if i == category_num:
                        return category
        else:
            print('\n' + '=' * 30)
            print('Введите номер категории из списка!')


def load_category(manager):
    while True:
        print('\n' + '=' * 30)
        print('ЗАГРУЗКА КАТЕГОРИИ')
        print('\n' + '=' * 30)
        print('введите "0" для выхода')
        for i, category in enumerate(manager.load_categories, start=1):
            if category in manager.categories:
                print(f'{i}| {category}'+' -загружено')
            else:
                print(f'{i}| {category}')

        change = input('Выберите категорию для загрузки: ')
        if change.isdigit():
            change = int(change)
            if change == 0:
                break
            for i, category in enumerate(manager.load_categories, start=1):
                if i == change:
                    manager.load_category_from_file(category)
                    print('\n' + '=' * 30)
                    print(f'Категория {category} успешно загружена!')
        else:
            print('\n' + '=' * 30)
            print('Введите число!')
