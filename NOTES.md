алидации `Card`
```python
def __post_init__(self):
    if not isinstance(self.rus, str) or not self.rus:
        raise ValueError("rus must be non-empty string")
```

---

## Общие советы по пет-проекту

1. **Начни с простого, добавляй по шагам.** Не пытайся сразу GUI, БД, авторизацию.
2. **Используй Git с первого дня.**
   ```bash
   git init
   git add .
   git commit -m "First version"
   ```
3. **README.md с описанием** — что за проект, как запустить, что умеет.
4. **Тесты** — хотя бы простые, через `pytest`.
5. **Не бойся рефакторить.** Первый код всегда плохой. Переписывай.
6. **Смотри чужой код** на GitHub. Копируй идеи, не код.
7. **Веди список TODO** — в файле или в коде через `# TODO:`.

---

## Что сделать прямо сейчас

1. [ ] Исправить баги: `raise 'string'`, `category.add_card` на строке, `in_words[1]` без проверки.
2. [ ] Обернуть в `main()` + `if __name__ == '__main__'`.
3. [ ] Разделить на файлы (`models.py`, `ui.py`, `main.py`).
4. [ ] Добавить сохранение в JSON.
5. [ ] Закоммитить в Git.
6. [ ] Продолжать добавлять функции по одной.

---

## Идеи на будущее

- [ ] GUI на Tkinter / Flet / PySide6
- [ ] Режим тренировки (показ слова → ввод перевода)
- [ ] Статистика (сколько выучено, сколько ошибок)
- [ ] Интервальное повторение (spaced repetition)
- [ ] Импорт/экспорт CSV
- [ ] Несколько наборов карточек

---

## Полезные ссылки (заполнить самому)

- Документация `dataclasses`: https://docs.python.org/3/library/dataclasses.html
- Документация `json`: https://docs.python.org/3/library/json.html
- PEP 8 (стиль кода): https://peps.python.org/pep-0008/