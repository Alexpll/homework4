import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import random


def main():
    vk_session = vk_api.VkApi(
        token='34491cf0316ee757f8e92728d5e3813d72e5e11effa74e396f42af4f77d21e4f41f077343f5b3f3d2e9e0')
    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, '203122854')
    order_food = 'заказать еду'

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Фильм секунды', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Картиночка секунды', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Герой Наруто', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=183415444")

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user == True:
                if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(
                    event) or 'Хеллоу' in str(event):
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
                else:
                    print(event)
                    print('Новое сообщение:')
                    print('Для меня от:', event.obj.message['from_id'])
                    print('Текст:', event.obj.message['text'])
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="Какая-то неадекватная дичь, romАЧКА такое не понимает",
                                     random_id=random.randint(0, 2 ** 64))
            if event.from_chat:
                print(event)
                print('Новое сообщение:')
                print('Для меня от:', event.chat_id)
                print('Текст:', event.obj.message['text'])
                vk.messages.send(chat_id=event.chat_id,
                                 message="Вас приветствует romАЧКА:ЗЗЗ",
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
            if 'Клавиатура' in str(event):
                if event.from_chat:
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(),
                        key=('453c553ee58dec67ee27b06174723bf3d6ff61d3'),
                        server=('https://lp.vk.com/wh202300325'),
                        ts=('132'),
                        random_id=get_random_id(),
                        message='Держи',
                        chat_id=event.chat_id
                    )

















    '''for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard()
            )
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()

            if event.obj.message['text'].lower() == order_food:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="https://vk.com/eda",
                                 random_id=random.randint(0, 2 ** 64))
            ''''''else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Спасибо, что написали нам. Мы обязательно ответим",
                                 random_id=random.randint(0, 2 ** 64))'''''''
        if 'Клавиатура' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard=keyboard.get_keyboard(),
                    key=('453c553ee58dec67ee27b06174723bf3d6ff61d3'),
                    server=('https://lp.vk.com/wh202300325'),
                    ts=('132'),
                    random_id=get_random_id(),
                    message='Держи',
                    chat_id=event.chat_id
                )'''


if __name__ == '__main__':
    main()