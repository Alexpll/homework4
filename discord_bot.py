import discord
import requests
import sqlite3
import random

TOKEN = 'ODMyOTc2ODU0Mzc3NTYyMTIy.YHroJg.HEoRCtctivRZMjPPmY4ImalF7Q0'
client = discord.Client()
con = sqlite3.connect('recipes.db')
cursor = con.cursor()


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
        if message.author != self.user and "!" in message.content.lower():
            if "привет" in message.content.lower():
                await message.channel.send("И тебе привет! Для того, чтобы узнать, что я могу, отправьте: '!инструкция'")
            elif "блюдосекунды" in message.content.lower():
                await message.channel.send("")
            elif "совет" in message.content.lower():
                await message.channel.send("")
            elif "хочурецепт" in message.content.lower():
                await message.channel.send("Для того, чтобы получить рецепт отправьте, пожалуйста, соответствующую цифру:\
                \n !1 - завтрак \n !2 - обед \n !3 - ужин")
            elif "!1" in message.content.lower():
                await message.channel.send("")
            elif "!2" in message.content.lower():
                await message.channel.send("")
            elif "!3" in message.content.lower():
                await message.channel.send("")
            elif "инструкция" in message.content.lower():
                await message.channel.send("!блюдосекунды - бот скинет рецепт, актуальный в эту секунду \n"
                                           "!совет - бот пришлет полезный совет для кухни \n"
                                           "!хочурецепт - бот подберет вам подходящий рецепт")
            else:
                await message.channel.send("Я не знаю такую команду:(")


client = YLBotClient()
client.run(TOKEN)