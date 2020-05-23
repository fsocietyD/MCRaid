import os,sys
import colorama
from colorama import init
os.system('clear')
banner = '''
88b           d88    ,ad8888ba,      88888888ba               88           88  
888b         d888   d8"'    `"8b     88      "8b              ""           88  
88`8b       d8'88  d8'               88      ,8P                           88  
88 `8b     d8' 88  88                88aaaaaa8P'  ,adPPYYba,  88   ,adPPYb,88  
88  `8b   d8'  88  88                88""""88'    ""     `Y8  88  a8"    `Y88  
88   `8b d8'   88  Y8,               88    `8b    ,adPPPPP88  88  8b       88  
88    `888'    88   Y8a.    .a8P     88     `8b   88,    ,88  88  "8a,   ,d88  
88     `8'     88    `"Y8888Y"'      88      `8b  `"8bbdP"Y8  88   `"8bbdP"Y8  
                                                            coded by @foxeditor
                                                            channel: @montelisa
                                                                               
'''
print(banner)

token = input('\033[31mВедите токен сообщества--->\033[39m')
id = input('\033[31mЧисловой id группы---->\033[39m')
f = 'raid.py'
n = open(f,"w",encoding='utf-8')
n.write("""import vk_api
from numpy import random
import time
from vk_api.keyboard import *
import traceback
from vk_api.bot_longpoll import *
vk_session = vk_api.VkApi(token='"""+str(token)+"""')
vk = vk_session.get_api()
print('Bot is working ;3')
def start():
    longpoll = VkBotLongPoll(vk_session,'"""+str(id)+"""')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                while True:
                  chat = event.chat_id
                  keyboard = VkKeyboard(one_time=False)     #создаем клавиатуру
                  text1 = random.choice(['[foxy]', '[fsociety]', '[foxeditor]'])    #создаем переменную, в которуй записываем рандомный выбор названия кнопки
                  text2 = random.choice(['[foxeditor]', '[fcociety]', '[foxy]'])
                  text3 = random.choice(['[foxeditor]', '[foxy]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[fsociety]', '[foxeditor]'])
                  col1 = random.choice(['negative','primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative','primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative','primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative','primary', 'positive', 'secondary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[montelisa]', '[foxy]', '[foxeditor]'])
                  text2 = random.choice(['[montelisa]', '[foxy]', '[foxeditor]'])
                  text3 = random.choice(['[montelisa]', '[foxy]', '[foxeditor]'])
                  text4 = random.choice(['[fsociety]', '[foxy]', '[foxy]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1,color=col1)   #добавляем текст в клавиатуру
                  keyboard.add_button(text2,color=col2)
                  keyboard.add_button(text3,color=col3)
                  keyboard.add_button(text4,color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  text2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  ext2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  text2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  text2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  text2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  text2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  keyboard.add_line()
                  text1 = random.choice(['[foxy]', '[montelisa]', '[montelisa]'])
                  ext2 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text3 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  text4 = random.choice(['[foxy]', '[foxeditor]', '[montelisa]'])
                  col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                  col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                  keyboard.add_button(text1, color=col1)
                  keyboard.add_button(text2, color=col2)
                  keyboard.add_button(text3, color=col3)
                  keyboard.add_button(text4, color=col4)
                  vk.messages.send(chat_id=chat,attachment='wall-183805868_12',random_id='0',keyboard=keyboard.get_keyboard())
                  vk.messages.send(chat_id=chat,attachment='wall-183805868_12',random_id='0',keyboard=keyboard.get_keyboard())
                  vk.messages.send(chat_id=chat,message=death,random_id='0',keyboard=keyboard.get_keyboard())
while True:
    try:
        start()
    except Exception as e:
        print('Error cyka', traceback.format_exc)
        """)
n.close()
print('\033[32m[>]Рейд бот готов!\033[39m')
        