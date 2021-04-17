import discord
import requests
import sqlite3
import random

TOKEN = 'ODMyOTc2ODU0Mzc3NTYyMTIy.YHroJg.KIoxhrcqtARxxhdhs-wr6wSWO5s'
client = discord.Client()
con = sqlite3.connect('recipes.db')
cursor = con.cursor()
status_db = False
status_type = False
lst_recipes = []


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})'
            )

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        global status_db
        global status_type
        global lst_recipes
        text = message.content.lower()
        if message.author != self.user and "!" in text:
            if "привет" in text:
                await message.channel.send("И тебе привет! Для того, чтобы узнать, что я могу, отправьте: '!инструкция'")
            elif "блюдосекунды" in text:
                data_3 = list(cursor.execute(f"SELECT * FROM list_recipes").fetchall())
                data_new = data_3[random.randint(0, len(data_3) - 1)]
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
                await message.channel.send(f'БЛЮДО СЕКУНДЫ \n{data_new[1]} \nКатегория: {data_new[2]} \n{fraze_2} \n{fraze}')
            elif "совет" in text:
                data_advices = list(cursor.execute("SELECT name_advice FROM advices").fetchall())
                advice = data_advices[random.randint(0, len(data_advices) - 1)]
                await message.channel.send(f"СОВЕТ!\n{advice[0]}")
            elif "хочурецепт" in text:
                await message.channel.send("Для того, чтобы получить рецепт отправьте, пожалуйста, соответствующую цифру:\
                \n !1 - завтрак \n !2 - обед \n !3 - ужин")
                status_db = True
            elif ("!1" == text or "!2" == text or "!3" == text) and status_db:
                if '!1' == text:
                    name = 'завтрак'
                elif '!2' == text:
                    name = 'обед'
                else:
                    name = 'ужин'
                data = cursor.execute(f"SELECT title FROM list_recipes WHERE type='{name}'").fetchall()
                data_names = [f'{list(data[x])[0]}' for x in range(len(data))]
                number = [x for x in range(0, len(data_names))]
                random.shuffle(number)
                await message.channel.send(f'Отправьте соответствующую цифру: \n 0 - {data_names[number[0]]}'
                                             f'\n 1 - {data_names[number[1]]} \n 2 - {data_names[number[2]]}')
                lst_recipes = [data_names[number[0]], data_names[number[1]], data_names[number[2]]]
                status_db = False
                status_type = True
            elif ("!0" == text or "!1" == text or "!2" == text) and status_type:
                if '0' == text:
                    name_2 = lst_recipes[0]
                elif '1' == text:
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
                    fraze += f'{i}.' + data_recipes[i - 1] + '\n'
                for x in range(len(data_ingredients)):
                    if '\n' in data_ingredients[x]:
                        st = data_ingredients[x].split('\n')
                        data_ingredients[x] = st[0] + st[1]
                fraze_2 = ''
                for i in range(1, len(data_ingredients) + 1):
                    fraze_2 += f'{i})' + data_ingredients[i - 1] + '\n'
                await message.channel.send(f'{data_2[1]} \nКатегория: {data_2[2]} \n{fraze_2} \n{fraze}')
                status_type = False
            elif "инструкция" in text:
                await message.channel.send("!блюдосекунды - бот скинет рецепт, актуальный в эту секунду \n"
                                           "!совет - бот пришлет полезный совет для кухни \n"
                                           "!хочурецепт - бот подберет вам подходящий рецепт")
            else:
                await message.channel.send("Я не знаю такую команду:(")


client = YLBotClient()
client.run(TOKEN)