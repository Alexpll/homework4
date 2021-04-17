import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import sqlite3
import random
from datetime import date


def main():
    vk_session = vk_api.VkApi(
        token='34491cf0316ee757f8e92728d5e3813d72e5e11effa74e396f42af4f77d21e4f41f077343f5b3f3d2e9e0')
    vk = vk_session.get_api()
    status_db = False
    status_db_chat = False
    con = sqlite3.connect('recipes.db')
    cursor = con.cursor()
    status_type = False
    status_type_chat = False
    dates = []
    dates_chat = []
    id_today_chat = []
    id_today = []

    longpoll = VkBotLongPoll(vk_session, '203122854')

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Хочу рецепт', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Блюдо дня', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Заказать еду', color=VkKeyboardColor.SECONDARY)
    key_clava = '453c553ee58dec67ee27b06174723bf3d6ff61d3'
    server_clava = 'https://lp.vk.com/wh202300325'
    ts_clava = '132'
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            text_message = event.object.get('message').get('text')
            if event.from_user:
                if 'ку' in text_message.lower() or 'привет' in text_message.lower() or 'хай' in text_message.lower()\
                        or 'хелло' in text_message.lower() or 'хеллоу' in text_message.lower() or 'start' in text_message.lower():
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                        user_id=event.obj.message['from_id'],
                        message='Привет! Чем я могу помочь?',
                        random_id=get_random_id()
                    )
                elif 'спасибо' in text_message.lower():
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                        user_id=event.obj.message['from_id'],
                        message='Не за что! Всегда рад помочь, брат',
                        random_id=get_random_id()
                    )
                elif ('1' == text_message or '2' == text_message or '3' == text_message) and status_db:
                    if '1' == text_message:
                        name = 'завтрак'
                    elif '2' == text_message:
                        name = 'обед'
                    else:
                        name = 'ужин'
                    data = cursor.execute(f"SELECT title FROM list_recipes WHERE type='{name}'").fetchall()
                    data_names = [f'{list(data[x])[0]}' for x in range(len(data))]
                    number = [x for x in range(0, len(data_names))]
                    random.shuffle(number)
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message=f'Отправьте соответствующую цифру: \n 0 - {data_names[number[0]]}'
                                             f'\n 1 - {data_names[number[1]]} \n 2 - {data_names[number[2]]}',
                                     random_id=random.randint(0, 2 ** 64))
                    lst_recipes = [data_names[number[0]], data_names[number[1]], data_names[number[2]]]
                    status_db = False
                    status_type = True
                elif ('0' == text_message or '1' == text_message or '2' == text_message) and status_type:
                    if '0' == text_message:
                        name_2 = lst_recipes[0]
                    elif '1' == text_message:
                        name_2 = lst_recipes[1]
                    else:
                        name_2 = lst_recipes[2]
                    data_2 = list(cursor.execute(f"SELECT * FROM list_recipes WHERE title='{name_2}'").fetchall()[0])
                    data_recipes = data_2[3].split(';')
                    data_ingredients = data_2[4].split(';')
                    for x in range(len(data_recipes)):
                        if '\n' in data_recipes[x]:
                            st = data_recipes[x].split('\n')
                            data_recipes[x] = st[0] + st[1]
                    fraze = ''
                    for i in range(1, len(data_recipes) + 1):
                        fraze += f'{i}.' + data_recipes[i-1] + '\n'
                    for x in range(len(data_ingredients)):
                        if '\n' in data_ingredients[x]:
                            st = data_ingredients[x].split('\n')
                            data_ingredients[x] = st[0] + st[1]
                    fraze_2 = ''
                    for i in range(1, len(data_ingredients) + 1):
                        fraze_2 += f'{i})' + data_ingredients[i-1] + '\n'
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message=f'{data_2[1]} \nКатегория: {data_2[2]} \n{fraze_2} \n{fraze}',
                                     random_id=random.randint(0, 2 ** 64))
                    status_type = False
                elif 'заказать еду' == text_message.lower():
                    vk.messages.send(keyboard=keyboard.get_keyboard(),key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message="https://vk.com/eda",
                                     random_id=random.randint(0, 2 ** 64))
                elif 'блюдо дня' == text_message.lower():
                    if date.today() in dates and event.obj.message['from_id'] in id_today:
                        vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava,
                                         ts=ts_clava,
                                         user_id=event.obj.message['from_id'],
                                         message=f'Блюдо дня уже было определено сегодня',
                                         random_id=random.randint(0, 2 ** 64))
                    else:
                        dates.append(date.today())
                        id_today.append(event.obj.message['from_id'])
                        data_3 = list(cursor.execute(f"SELECT * FROM list_recipes").fetchall())
                        data_new = data_3[random.randint(0, len(data_3))]
                        print(data_new)
                        data_recipes = data_new[3].split(';')
                        data_ingredients = data_new[4].split(';')
                        for x in range(len(data_recipes)):
                            if '\n' in data_recipes[x]:
                                st = data_recipes[x].split('\n')
                                data_recipes[x] = st[0] + st[1]
                        fraze = ''
                        for i in range(1, len(data_recipes) + 1):
                            fraze += f'{i}.' + data_recipes[i - 1] + '\n'
                        for x in range(len(data_ingredients)):
                            if '\n' in data_ingredients[x]:
                                st = data_ingredients[x].split('\n')
                                data_ingredients[x] = st[0] + st[1]
                        fraze_2 = ''
                        for i in range(1, len(data_ingredients) + 1):
                            fraze_2 += f'{i})' + data_ingredients[i - 1] + '\n'
                        vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                         user_id=event.obj.message['from_id'],
                                         message=f'БЛЮДО ДНЯ \n{data_new[1]} \nКатегория: {data_new[2]} \n{fraze_2} \n{fraze}',
                                         random_id=random.randint(0, 2 ** 64))
                elif 'хочу рецепт' == text_message.lower():
                    status_db = True
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message="Для того, чтобы получить рецепт отправьте, пожалуйста, соответствующую цифру:\
                                      \n 1 - завтрак \n 2 - обед \n 3 - ужин",
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     user_id=event.obj.message['from_id'],
                                     message="Я не знаю такую команду:(",
                                     random_id=random.randint(0, 2 ** 64))
            if event.from_chat:
                if 'ку' in text_message.lower() or 'привет' in text_message.lower() or 'хай' in text_message.lower() \
                        or 'хелло' in text_message.lower() or 'хеллоу' in text_message.lower() or 'start' in text_message.lower():
                    if event.from_chat:
                        vk.messages.send(
                            keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                            random_id=get_random_id(),
                            message='Привет! Чем я могу помочь?',
                            chat_id=event.chat_id
                        )
                elif ('[club203122854|мой бесполезный бот] 1' in text_message or '[club203122854|мой бесполезный бот] 2'\
                      in text_message or '[club203122854|мой бесполезный бот] 3' in text_message) and status_db_chat:
                    print(text_message)
                    if '[club203122854|мой бесполезный бот] 1' in text_message:
                        name = 'завтрак'
                    elif '[club203122854|мой бесполезный бот] 2' in text_message:
                        name = 'обед'
                    else:
                        name = 'ужин'
                    data = cursor.execute(f"SELECT title FROM list_recipes WHERE type='{name}'").fetchall()
                    data_names = [f'{list(data[x])[0]}' for x in range(len(data))]
                    number = [x for x in range(0, len(data_names))]
                    random.shuffle(number)
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                        random_id=get_random_id(),
                        message=f'Отправьте соответствующую цифру: \n 0 - {data_names[number[0]]}\n 1 - '
                                f'{data_names[number[1]]} \n 2 - {data_names[number[2]]}',
                        chat_id=event.chat_id
                    )
                    lst_recipes = [data_names[number[0]], data_names[number[1]], data_names[number[2]]]
                    status_db_chat = False
                    status_type_chat = True
                elif ('[club203122854|мой бесполезный бот] 0' in text_message or '[club203122854|мой бесполезный бот] 1'\
                      in text_message or '[club203122854|мой бесполезный бот] 2' in text_message) and status_type_chat:
                    if '[club203122854|мой бесполезный бот] 0' == text_message:
                        name_2 = lst_recipes[0]
                    elif '[club203122854|мой бесполезный бот] 1' == text_message:
                        name_2 = lst_recipes[1]
                    else:
                        name_2 = lst_recipes[2]
                    data_2 = list(cursor.execute(f"SELECT * FROM list_recipes WHERE title='{name_2}'").fetchall()[0])
                    data_recipes = data_2[3].split(';')
                    data_ingredients = data_2[4].split(';')
                    for x in range(len(data_recipes)):
                        if '\n' in data_recipes[x]:
                            st = data_recipes[x].split('\n')
                            data_recipes[x] = st[0] + st[1]
                    fraze = ''
                    for i in range(1, len(data_recipes) + 1):
                        fraze += f'{i}.' + data_recipes[i-1] + '\n'
                    for x in range(len(data_ingredients)):
                        if '\n' in data_ingredients[x]:
                            st = data_ingredients[x].split('\n')
                            data_ingredients[x] = st[0] + st[1]
                    fraze_2 = ''
                    for i in range(1, len(data_ingredients) + 1):
                        fraze_2 += f'{i})' + data_ingredients[i-1] + '\n'
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     random_id=get_random_id(),
                                     message=f'{data_2[1]} \nКатегория: {data_2[2]} \n{fraze_2} \n{fraze}',
                                     chat_id=event.chat_id)
                    status_type_chat = False
                elif 'заказать еду' in text_message.lower():
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                        random_id=get_random_id(),
                        message='https://vk.com/eda',
                        chat_id=event.chat_id
                    )
                elif 'блюдо дня' in text_message.lower():
                    if date.today() in dates_chat and event.chat_id in id_today_chat:
                        vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                         random_id=get_random_id(),
                                         message='Блюдо дня уже было определено сегодня',
                                         chat_id=event.chat_id)
                    else:
                        dates_chat.append(date.today())
                        id_today_chat.append(event.chat_id)
                        data_3 = list(cursor.execute(f"SELECT * FROM list_recipes").fetchall())
                        data_new = data_3[random.randint(0, len(data_3) - 1)]
                        print(data_new)
                        data_recipes = data_new[3].split(';')
                        data_ingredients = data_new[4].split(';')
                        for x in range(len(data_recipes)):
                            if '\n' in data_recipes[x]:
                                st = data_recipes[x].split('\n')
                                data_recipes[x] = st[0] + st[1]
                        fraze = ''
                        for i in range(1, len(data_recipes) + 1):
                            fraze += f'{i}.' + data_recipes[i - 1] + '\n'
                        for x in range(len(data_ingredients)):
                            if '\n' in data_ingredients[x]:
                                st = data_ingredients[x].split('\n')
                                data_ingredients[x] = st[0] + st[1]
                        fraze_2 = ''
                        for i in range(1, len(data_ingredients) + 1):
                            fraze_2 += f'{i})' + data_ingredients[i - 1] + '\n'
                        vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                         random_id=get_random_id(),
                                         message=f'БЛЮДО ДНЯ \n{data_new[1]} \nКатегория: {data_new[2]} \n{fraze_2} \n{fraze}',
                                         chat_id=event.chat_id)
                elif 'хочу рецепт' in text_message.lower():
                    status_db_chat = True
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                        random_id=get_random_id(),
                        message=f'Для того, чтобы получить рецепт отправьте, пожалуйста, соответствующую цифру:\
                                      \n 1 - завтрак \n 2 - обед \n 3 - ужин',
                        chat_id=event.chat_id
                    )
                else:
                    vk.messages.send(keyboard=keyboard.get_keyboard(), key=key_clava, server=server_clava, ts=ts_clava,
                                     random_id=get_random_id(),
                                     message='Я не знаю такую команду:(',
                                     chat_id=event.chat_id)


if __name__ == '__main__':
    main()