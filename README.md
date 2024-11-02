
# Парсер для сайта Melomania.online

## Описание

Этот скрипт представляет собой парсер для поиска виниловых пластинок, компакт-дисков и DVD/Blu-Ray дисков на сайте [Melomania.online](https://melomania.online). Пользователь вводит имя артиста и выбирает тип носителя, а скрипт выводит список найденных альбомов с их ценами.

## Требования

- Python 3.x
- Установленные модули:
  - `requests`
  - `beautifulsoup4`

### Установка зависимостей

```bash
pip install requests beautifulsoup4
```

## Использование

Запустите скрипт, используя команду:

```bash
python main.py
```

Скрипт предложит вам ввести имя исполнителя и тип носителя для поиска. Для выхода введите `0`.

### Доступные типы носителей

1. Виниловые пластинки
2. Компакт-диски
3. DVD/Blu-Ray музыка
4. Весь каталог

После ввода информации скрипт отправит запрос на сайт и отобразит найденные альбомы и их цены в формате таблицы.

## Описание функций

- **`fetch_page(url)`**: Получает HTML-код страницы по указанному URL.
- **`find_album(page)`**: Ищет и выводит названия альбомов и цены.
- **`display_welcome_message()`**: Выводит приветственное сообщение для пользователя.
- **`get_user_input()`**: Запрашивает у пользователя имя артиста и тип носителя.
- **`main()`**: Основная функция, отвечающая за логику работы парсера.

## Примечания

- Данный парсер предназначен только для образовательных целей. Пожалуйста, соблюдайте условия использования сайта.
