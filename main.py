import requests
from bs4 import BeautifulSoup as Bs


def fetch_page(url):
    """Извлекает содержимое страницы по указанному URL-адресу"""
    response = requests.get(url)
    response.raise_for_status()  # Отбрасывает ошибку при плохом запросе
    return Bs(response.text, 'html.parser')


def find_album(page):
    """Находит и выводит названия альбомов и цены на них с указанной страницы"""
    all_names = page.findAll(class_='uss_shop_name')
    all_prices = page.findAll(class_='price_class')

    print('╔' + '═' * 64 + '╗')
    for name, price in zip(all_names, all_prices):
        formatted_name = (name.text[:47] + '..') if len(name.text) > 47 else name.text
        formatted_price = price.text
        print(f'║ {formatted_name.ljust(50)}{formatted_price.rjust(8)} руб ║')
    print('╚' + '═' * 64 + '╝')


def display_welcome_message():
    """Выводит сообщение для пользователя"""
    print('╔' + '═' * 65 + '╗')
    print('║' + ' ' * 6 + 'Добро пожаловать на сервис поиска виниловых пластинок' + ' ' * 6 + '║')


def get_user_input():
    """Запрашивает у пользователя имя исполнителя и тип носителя"""
    print('╔' + '═' * 65 + '╗')
    print('║' + ' ' * 10 + 'Введите имя артиста и тип носителя для поиска' + ' ' * 10 + '║')
    print('║' + ' ' * 10 + 'виниловых пластинок на сайте Melomania.online' + ' ' * 10 + '║')
    print('║' + ' ' * 21 + '(для выхода введите 0)' + ' ' * 22 + '║')
    print('╚' + '═' * 65 + '╝')

    singer = input('Имя артиста (для выхода - 0): ')
    if singer == '0':
        return None, None

    type_music = int(input('Тип носителя:\n'
                           ' 1. Виниловые пластинки\n'
                           ' 2. Компакт диски\n'
                           ' 3. DVD/Blu-Ray музыка\n'
                           ' 4. Весь каталог\n'
                           'Введите номер типа носителя: '))
    if type_music != 4:
        type_music += 13520
    else:
        type_music = 0

    return singer, type_music


def main():
    """Основная функция для запуска парсера"""
    display_welcome_message()

    while True:
        singer, type_music = get_user_input()
        if singer is None:
            break

        url = f'https://melomania.online/sitesearch/?search={singer}&search_category={type_music}'
        page = fetch_page(url)
        page_count_element = page.find(class_='uss_page_count')

        if page_count_element is None:
            print('╔' + '═' * 65 + '╗')
            print('║' + ' ' * 2 + "Такой исполнитель на таком носителе не найден, попробуйте ещё" + ' ' * 2 + '║')
            print('╚' + '═' * 65 + '╝')
            continue

        page_count = int(page_count_element.text.replace('Всего: ', ''))

        for i in range(1, (page_count // 21) + 2):
            print('Страница:', i)
            page_url = f'https://melomania.online/sitesearch/?search={singer}&search_category={type_music}&page={i}'
            find_album(fetch_page(page_url))


if __name__ == '__main__':
    main()