import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import sqlite3
import random


def main():
    vk_session = vk_api.VkApi(
        token='34491cf0316ee757f8e92728d5e3813d72e5e11effa74e396f42af4f77d21e4f41f077343f5b3f3d2e9e0')
    vk = vk_session.get_api()
    connection = sqlite3.connect('recipes.db')

    longpoll = VkBotLongPoll(vk_session, '203122854')

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Хочу рецепт', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Блюдо дня', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Заказать еду', color=VkKeyboardColor.SECONDARY)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user == True:
                if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event)\
                        or 'Хеллоу' in str(event):
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            message='Привет)',
                            random_id=get_random_id()
                        )
                elif 'клава' in str(event):
                    print('все пошло по плану')
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(),
                        key=('453c553ee58dec67ee27b06174723bf3d6ff61d3'),
                        server=('https://lp.vk.com/wh202300325'),
                        ts=('132'),
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        message='Держи',
                    )
                elif 'заказать еду' in str(event).lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="https://vk.com/eda",
                                     random_id=random.randint(0, 2 ** 64))
                elif 'блюдо дня' in str(event).lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="вот блюдо дня",
                                     random_id=random.randint(0, 2 ** 64))
                elif 'хочу рецепт' in str(event).lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="Для того, чтобы получить рецепт отправьте, пожалуйста, соответствующую цифру\
                                      \n 1 - завтрак \n 2 - обед \n 3 - ужин",
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="ниче не понятно",
                                     random_id=random.randint(0, 2 ** 64))
            if event.from_chat:
                vk.messages.send(chat_id=event.chat_id,
                                 message="Вас приветствует мой бесполезный бот",
                                 random_id=random.randint(0, 2 ** 64))
            if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(
                    event) or 'Хеллоу' in str(event):
                if event.from_chat:
                    vk.messages.send(
                        key=('453c553ee58dec67ee27b06174723bf3d6ff61d3'),
                        server=('https://lp.vk.com/wh202300325'),
                        ts=('132'),
                        random_id=get_random_id(),
                        message='Привет!',
                        chat_id=event.chat_id
                    )


if __name__ == '__main__':
    main()