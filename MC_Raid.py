# -*- coding: utf-8 -*-
import vk_api
import random
import time
#from threading import *
from vk_api.keyboard import *
#import six
import traceback
from vk_api.bot_longpoll import *
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

token = input('Введите токен Сообщества---->')
id = input('Введите Id Сообщества (ЦИФРОВОЙ)---->')

death = ''' 




g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿h͚̖̜͚̖̜͚̖̜̍̃͐̍̃͐̍̃͐b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅv̪̩̜̜̙̜̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄ͨ̽̄b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅb͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅj͇̗̲̞̪̹̝̫̞͇̗̲̞̪̹̝̫̞͇̗̲̞̪̹̝̫̞ͬ͐̀ͧ̿ͬ͐̀ͧ̿ͬ͐̀ͧ̿g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿f̳͉̼͉̙͔͈̳͉̼͉̙͔͈̳͉̼͉̙͔͈̂̉̂̉̂̉s̪̭̱̼̼̪̭̱̼̼̪̭̱̼̼̉̈́ͪ͋̽̉̈́ͪ͋̽̉̈́ͪ͋̽̚̚̚t̘̟̼̘̟̼̘̟̼̉̈́͐͋͌̊̉̈́͐͋͌̊̉̈́͐͋͌̊g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿v̪̩̜̜̙̜̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄ͨ̽̄c͔͔͔ͣͦ́́͂ͣͦ́́͂ͣͦ́́͂ͅͅͅd̥̝̮͙͈̥̝̮͙͈̥̝̮͙͈͂̐̇ͮ̏̔̀͂̐̇ͮ̏̔̀͂̐̇ͮ̏̔̀̚̚̚ͅͅͅg͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿h͚̖̜͚̖̜͚̖̜̍̃͐̍̃͐̍̃͐b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅv̪̩̜̜̙̜̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄ͨ̽̄b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅb͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅj͇̗̲̞̪̹̝̫̞͇̗̲̞̪̹̝̫̞͇̗̲̞̪̹̝̫̞ͬ͐̀ͧ̿ͬ͐̀ͧ̿ͬ͐̀ͧ̿g͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿f̳͉̼͉̙͔͈̳͉̼͉̙͔͈̂̉̂̉s̪̭̱̼̼̪̭̱̼̼̉̈́ͪ͋̽̉̈́ͪ͋̽̚̚t̘̟̼̘̟̼̉̈́͐͋͌̊̉̈́͐͋͌̊g͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿v̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄c͔͔ͣͦ́́͂ͣͦ́́͂ͅͅd̥̝̮͙͈̥̝̮͙͈͂̐̇ͮ̏̔̀͂̐̇ͮ̏̔̀̚̚ͅͅg͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿h͚̖̜͚̖̜̍̃͐̍̃͐b͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾ͅͅv̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄b͎̣̫͈̥̗͎̣̮͙͈͒͌̃͑̔̾͒͌̃͑̔̾ͅͅg͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿h͚̖̜͚̖̜͚̖̜̍̃͐̍̃͐̍̃͐b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅv̪̩̜̜̙̜̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄ͨ̽̄b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅb͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅj͇̗̲̞̪̹̝̫̞͇̗̲̞̪̹̝̫̞͇̗̲̞̪̹̝̫̞ͬ͐̀ͧ̿ͬ͐̀ͧ̿ͬ͐̀ͧ̿g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿f̳͉̼͉̙͔͈̳͉̼͉̙͔͈̳͉̼͉̙͔͈̂̉̂̉̂̉s̪̭̱̼̼̪̭̱̼̼̪̭̱̼̼̉̈́ͪ͋̽̉̈́ͪ͋̽̉̈́ͪ͋̽̚̚̚t̘̟̼̘̟̼̘̟̼̉̈́͐͋͌̊̉̈́͐͋͌̊̉̈́͐͋͌̊g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿v̪̩̜̜̙̜̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄ͨ̽̄c͔͔͔ͣͦ́́͂ͣͦ́́͂ͣͦ́́͂ͅͅͅd̥̝̮͙͈̥̝̮͙͈̥̝̮͙͈͂̐̇ͮ̏̔̀͂̐̇ͮ̏̔̀͂̐̇ͮ̏̔̀̚̚̚ͅͅͅg͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿h͚̖̜͚̖̜͚̖̜̍̃͐̍̃͐̍̃͐b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗̮͙͈͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅͅg͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿h͚̖̜͚̖̜͚̖̜̍̃͐̍̃͐̍̃͐b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅv̪̩̜̜̙̜̪̩̜̜̙̜̪̩̜̜̙̜ͨ̽̄ͨ̽̄ͨ̽̄b͎̣̫͈̥̗͎̣̫͈̥̗͎̣̫͈̥̗͒͌̃͑̔̾͒͌̃͑̔̾͒͌̃͑̔̾ͅͅͅ

g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿
g͎͚̥͎͔͕͎͚̥͎͔͕͎͚̥͎͔͕ͥ̿ͥ̿ͥ̿h͚̖̜͚̖̜͚̖̜̍̃͐̍̃͐
لُلُصّبُلُلصّبُررً ॣ ॣh ॣ ॣ
冗     
.
'''

vk_session = vk_api.VkApi(token=token)  #создаем переменную с токеном группы
vk = vk_session.get_api()   #подключаемся в вк сессии
print('Bot started!')
def start():
    longpoll = VkBotLongPoll(vk_session,id)
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
                       vk.messages.send(chat_id=chat,attachment='wall-183805868_12',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=chat,attachment='wall-183805868_12',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=chat,message=death,random_id='0',keyboard=keyboard.get_keyboard())
while True:
    try:
        start()
    except Exception as e:
        print('Error cyka', traceback.format_exc())