import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    vk_session = vk_api.VkApi(
        token='34491cf0316ee757f8e92728d5e3813d72e5e11effa74e396f42af4f77d21e4f41f077343f5b3f3d2e9e0')

    longpoll = VkBotLongPoll(vk_session, '203122854')
    order_food = 'заказать еду'

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            if event.obj.message['text'].lower() == order_food:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="https://vk.com/eda",
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Спасибо, что написали нам. Мы обязательно ответим",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()