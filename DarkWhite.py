users = [
    {'username': 'user',
     'password': '123',
     'role': 'user'},
    {'username': 'Egor',
     'password': 'password123',
     'role': 'user'},
    {'username': 'Vlad',
     'password': 'Russia123',
     'role': 'user'},
    {'username': 'Flowey',
     'password': 'Flowey',
     'role': 'user'},

    {'username': 'admin',
     'password': 'qwerty',
     'role': 'admin'},
    {'username': 'hacker',
     'password': 'password',
     'role': 'admin'}]


user_menu = {'1': 'Посмотреть список цветов',
             '2': 'Посмотреть список готовых букетов',
             '3': 'Поиск цветка по названию',
             '4': 'Поиск готового букета по названию',
             '5': 'Поиск готового букета по цветку',
             '6': 'Сортировка цветов по цене',
             '7': 'Сортировка готовых букетов по цене',
             '8': 'Выход'}

admin_menu = {'1': 'Добавить цветок',
              '2': 'Добавить букет',
              '3': 'Удалить цветок',
              '4': 'Удалить букет',
              '5': 'Добавить пользователя',
              '6': 'Удалить пользователей',
              '7': 'Вывести список пользователей',
              '8': 'Выход'
}

flowers = [{'flower_title': 'Роза красная',
            'cost': 150},
           {'flower_title': 'Роза белая',
            'cost': 140},
           {'flower_title': 'Роза розовая',
            'cost': 160},
           {'flower_title': 'Тюльпан желтый',
            'cost': 70},
           {'flower_title': 'Тюльпан красный',
            'cost': 80},
           {'flower_title': 'Лилия белая',
            'cost': 200},
           {'flower_title': 'Гербера',
            'cost': 90},
           {'flower_title': 'Хризантема',
            'cost': 60},
           {'flower_title': 'Орхидея',
            'cost':  250},
           {'flower_title': 'Маргаритка',
            'cost': 50},
           {'flower_title': 'Астры',
            'cost': 55},
           {'flower_title': 'Гвоздика',
            'cost': 75},
           {'flower_title': 'Лаванда',
            'cost': 120},
           {'flower_title': 'Сирень',
            'cost': 85},
           {'flower_title': 'Пионы',
            'cost': 300},
           {'flower_title': 'Нарциссы',
            'cost': 65},
           {'flower_title': 'Фрезия',
            'cost': 110},
           {'flower_title': 'Фиалка',
            'cost': 40},
           {'flower_title': 'Каллы',
            'cost': 220},
           {'flower_title': 'Жасмин',
            'cost': 95}]

bouquets = [{'bouquet_title': 'Белый ангел',
             'cost': 1100,
             'flowers': ['Роза белая', 'Тюльпан желтый', 'Сирень']},
            {'bouquet_title': 'Весенний',
             'cost': 940,
             'flowers': ['Тюльпан желтый', 'Роза белая', 'Сирень']},
            {'bouquet_title': 'Романтика',
             'cost': 1600,
             'flowers': ['Роза красная', 'Гвоздика', 'Лилия']},
            {'bouquet_title': 'Солнечный день',
             'cost': 850,
             'flowers': ['Гербера', 'Тюльпан красный', 'Маргаритка']},
            {'bouquet_title': 'Летний вечер',
             'cost': 2050,
             'flowers': ['Орхидея', 'Лаванда', 'Калла']},
            {'bouquet_title': 'Уют',
             'cost': 700,
             'flowers': ['Хризантема', 'Астра', 'Фрезия']},
            {'bouquet_title': 'Нежность',
             'cost': 1540,
             'flowers': ['Роза розовая', 'Фиалка', 'Пион']},
            {'bouquet_title': 'Свадебный',
             'cost': 2380,
             'flowers': ['Пион', 'Лилия белая', 'Роза белая']},
            {'bouquet_title': 'Осенняя сказка',
             'cost': 780,
             'flowers': ['Нарциссы', 'Сирень', 'Тюльпан желтый']},
            {'bouquet_title': 'Морской бриз',
             'cost': 1585,
             'flowers': ['Жасмин', 'Орхидея', 'Гербера']},
            {'bouquet_title': 'Зимний уют',
             'cost': 1125,
             'flowers': ['Лилия белая', 'Хризантема', 'Гвоздика']},]

def start():
    login = input('Введите имя аккаунта: ')
    for user in users:
        if login == user['username']:
            password = input('Введите пароль: ')
            if password == user['password'] and user['role'] == 'user':
                return menu(user)
            elif password == user['password'] and user['role'] == 'admin':
                return a_menu(user)
            else:
                print('Неверный пароль\n')
                return start()
    print('Нет такого имени аккаунта\n')
    return start()


def menu(user):
    print(f'\n{user["username"].capitalize()}, добро пожаловать в сеть цветочного магазина!\nВыберите действие которое хотите совершить!')
    for number in user_menu:
        print(number, user_menu[number])
    user_input = input()
    if user_input in user_menu.keys():
        if user_input in ['3', '6']:
            do_user_menu[user_input](flowers)
        elif user_input in ['4', '7']:
            do_user_menu[user_input](bouquets)
        else:
            do_user_menu[user_input]()
    else:
        print('Такой команды нет!')
    menu(user)

def list_of_flowers(lst=flowers):
    print('\n', '\n\n'.join(list(map(lambda flower: f'Название цветка - {flower["flower_title"]}\nЦена цветка - {flower['cost']}', lst))), sep='')\

def list_of_bouquets(lst=bouquets):
    print('\n', '\n\n'.join(list(map(lambda bouquet: f'Название букета - {bouquet['bouquet_title']}\nЦена букета - {bouquet['cost']}\nЦветки внутри букета - {', '.join(bouquet['flowers'])}', lst))), sep='')

def search_by_name(parameter):
    if parameter == flowers:
        inp = input('Введите название цвета, который хотите найти: ').lower().strip()
        list_of_flowers(list(filter(lambda x: inp in x['flower_title'].lower(), parameter)))
    else:
        inp = input('Введите название букета, который хотите найти: ').lower().strip()
        list_of_bouquets(list(filter(lambda x: inp in x['bouquet_title'].lower(), parameter)))

def sort_by_cost(parameter):
    if parameter == flowers:
        list_of_flowers(list(sorted(parameter, key=lambda x: x['cost'], reverse=True)))
    else:
        list_of_bouquets(list(sorted(parameter, key=lambda x: x['cost'], reverse=True)))

def search_by_flower():
    inp = input('Введи название цветка, который должен быть в букете: ').lower().strip()
    list_of_bouquets(list(filter(lambda x: inp in list(map(lambda flower: flower.lower(), x['flowers'])), bouquets)))


def a_menu(user):
    print(
        f'\n{user['username'].capitalize()}, добро пожаловать в сеть цветочного магазина!\nВыберите действие которое хотите совершить!')
    for number in admin_menu:
        print(number, admin_menu[number])
    user_input = input()
    if user_input in admin_menu.keys():
        if user_input in ['1', '3']:
            do_admin_menu[user_input](flowers, user)
        elif user_input in ['2', '4']:
            do_admin_menu[user_input](bouquets, user)
        elif user_input in ['5', '6']:
            do_admin_menu[user_input](users, user)
        else:
            do_admin_menu[user_input]()
    else:
        print('Такой команды нет!\n')
    a_menu(user)

def add_to(parameter, cur_user=None):
    if parameter == flowers:
        try:
            flowers.append({'flower_title': input('Введите название цветка: ').capitalize(), 'cost': int(input('Введите цену цветка: '))})
        except ValueError:
            print('Вы ввели не число!')
    elif parameter == 'bouquet':
        try:
            bouquets.append({'bouquet_title': input('Введите название букета: ').capitalize(), 'cost': int(input('Введите цену букета: ')), 'flowers': input('Вводите названия цветков в букете через запятую: ').split(', ')})
        except ValueError:
            print('Вы ввели не число!')
    else:
        inp = input('Введите username нового пользователя: ').strip()
        for user in users:
            if inp == user['username']:
                print('Такой username занят!')
                return
        user_choice = input('Вы хотите создать админа? (да/нет): ').strip().lower()
        if user_choice == 'да':
            users.append({'username': inp, 'password': input('Введите пароль: '), 'role': 'admin'})
        elif user_choice == 'нет':
            users.append({'username': inp, 'password': input('Введите пароль: '), 'role': 'user'})
        else:
            print('Вы ввели что-то другое!')



def delete_from(parameter, cur_user=None):
    if parameter == flowers:
        inp = input('Введите название цветка, который хотите удалить: ').strip().lower()
        for flower in flowers:
            if inp == flower['flower_title'].lower():
                print(f'Цветок под названием <{flower['flower_title']}> был успешно удалён')
                flowers.remove(flower)
                return
        print('Цветок с таким названием не найден!')
    elif parameter == 'bouquet':
        inp = input('Введите название букета, который хотите удалить: ').strip().lower()
        for bouquet in bouquets:
            if inp == bouquet.lower():
                print(f'Букет под названием <{bouquet['bouquet_title']}> был успешно удалён')
                bouquet.remove(bouquet)
                return
        print('Букет с таким названием не найден!')
    else:
        inp = input('Введите username пользователя, которого хотите удалить: ').strip()
        if inp == cur_user['username']:
            print('Вы не можете удалить себя!')
            return
        for user in users:
            if inp == user['username']:
                print(f'Пользователь {user['username']} был успешно удалён')
                users.remove(user)
                return
        print('Пользователь под таким названием не найден!')

def list_of_users():
    print('\n', '\n'.join(list(map(lambda user: f'Имя пользователя - {user["username"]}\nПароль пользователя - {user["password"]}\nРоль пользователя - {user["role"]}\n', users))), sep='')


do_user_menu = {
    '1': list_of_flowers,
    '2': list_of_bouquets,
    '3': lambda x: search_by_name(x),
    '4': lambda x: search_by_name(x),
    '5': search_by_flower,
    '6': lambda x: sort_by_cost(x),
    '7': lambda x: sort_by_cost(x),
    '8': start
}

do_admin_menu = {
    '1': lambda x, y: add_to(x, y),
    '2': lambda x, y : add_to(x, y),
    '3': lambda x, y: delete_from(x, y),
    '4': lambda x, y: delete_from(x, y),
    '5': lambda x, y: add_to(x, y),
    '6': lambda x, y: delete_from(x, y),
    '7': list_of_users,
    '8': start
}


if __name__ == '__main__':
    start()