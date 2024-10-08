import telebot
from telebot import types
# import random
import requests as rq
from bs4 import BeautifulSoup as BS


# token = '6945752229:AAH2OT9l-Waaoir_NjytADPSBKBeHxYUcCc'
# bot = telebot.TeleBot(token)
url = 'https://my-calend.ru/holidays'
responce = rq.get(url)
soup = BS(responce.text,'html.parser')
b_day = soup.find_all('ul', class_="birthday-horoscope-stars")
for i in b_day:
    print(i.text)
# @bot.message_handler(commands=['start'])
# def start(message):
#     global holidays_index, event_index, holidays, events, b_days, bday_index
#     url = 'https://my-calend.ru/holidays'
#     responce = rq.get(url)
#    soup = BS(responce.text,'html.parser')
#     ul = soup.find('ul', class_='holidays-items')
#     holidays = ul.find_all('li')
# section = soup.find('section', class_='holidays-name-days')
    # events = soup.find_all('div', class_="holidays-day-info-events")
# b_days = soup.find_all('ul', class_="birthday-horoscope-stars")
    # holidays_index = 0
    # bday_index = 0
    # event_index = 0
    # for i in holidays:
    #     i = i.text.split('  ')[0]
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     holiday_button = types.KeyboardButton('Праздники')
#     event_button = types.KeyboardButton('События в этот день')
#     b_days_button = types.KeyboardButton('Родились в этот день')
#     markup.add(holiday_button,event_button,b_days_button)
#     bot.send_message(message.chat.id,'Добро пожаловать! Я подскажу тебе,какие праздники сегодня!',reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def info_holidays(message):
#     global event_index,holidays_index, holidays, event
#     if message.text == 'Праздники':
#         holiday = holidays[holidays_index]
#         holidays_index += 1
#         if holidays_index == len(holidays):
#             holidays_index = 0
#         bot.send_message(message.chat.id, holiday)
#     elif message.text == 'События в этот день':
#         event = events[event_index]
#         event_index += 1
#         if event_index == len(events):
#             event_index = 0
#         bot.send_message(message.chat.id, event)
#     elif message.text == 'Родились в этот день':
        # b_day = soup.find('ul', class_="birthday-horoscope-stars").text
#         bot.send_message(message.chat.id, "Я этого еще не умею.")

# bot.polling(none_stop=True)



# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button_rock = types.KeyboardButton('камень')
#     button_paper = types.KeyboardButton('бумага')
#     button_scissors = types.KeyboardButton('ножницы')
#     markup.add(button_rock, button_paper, button_scissors)
#     bot.send_message(message.chat.id,'Добро пожаловать!') 
#     bot.send_message(message.chat.id,'Сделай ход', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def game_process(message):
#     a = ['камень', 'ножницы', 'бумага']
#     comp = random.choice(a)
#     bot.send_message(message.chat.id,f'Компьютер выбрал: {comp}')
#     if message.text == comp:
#      bot.send_message(message.chat.id,'Ничья')
#     elif (message.text == 'камень' and comp == 'ножницы') or (message.text == 'бумага' and comp == 'камень') or (message.text == 'ножницы' and comp == 'бумага'):
#      bot.send_message(message.chat.id,'Вы победили')
#     else:
#      bot.send_message(message.chat.id,'Вы проиграли')
# bot.polling(none_stop=True)



