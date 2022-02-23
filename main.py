import telebot
import requests
import json
import sqlite3
import adminka
from telebot import types
from random import randint
from config import token

bot=telebot.TeleBot(token)
ADMIN = 641892529
in_admin = []

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(types.InlineKeyboardButton(text="➕ Добавить в базу"))
kb.add(types.InlineKeyboardButton(text="📥 Новые запросы"))
kb.add(types.InlineKeyboardButton(text="📋 Рассылка"))

@bot.message_handler(commands=["start"])
def welcome(message):
if '/start' == message.text:
if message.chat.username:
if dop.get_sost(message.chat.id) is True: 
with shelve.open(files.sost_bd) as bd: del bd[str(message.chat.id)]
if message.chat.id in in_admin: in_admin.remove(message.chat.id)
if message.chat.id == config.admin_id and dop.it_first(message.chat.id) is True: in_admin.append(message.chat.id)
elif dop.it_first(message.chat.id) is True and message.chat.id not in dop.get_adminlist():
bot.send_message(message.chat.id, 'Бот ещё не готов к работе!\nЕсли вы являетесь его администратором, то войдите из под аккаунту, id которого указали при запуске бота и подготовьте его к работе!')
elif dop.check_message('start') is True:
key = telebot.types.InlineKeyboardMarkup()
key.add(telebot.types.InlineKeyboardButton(text='Перейти к каталогу товаров', callback_data='Перейти к каталогу товаров'))
with shelve.open(files.bot_message_bd) as bd: start_message = bd['start']
start_message = start_message.replace('username', message.chat.username)
start_message = start_message.replace('name', message.from_user.first_name)
bot.send_message(message.chat.id, start_message, reply_markup=key)	
elif dop.check_message('start') is False and message.chat.id in dop.get_adminlist():
bot.send_message(message.chat.id, 'Приветствие ещё не добавлено!\nЧтобы его добавить, перейдите в админку по команде /adm и *настройте ответы бота*', parse_mode='Markdown')

dop.user_loger(chat_id=message.chat.id) #логгирование юзеровs
elif not message.chat.username:
with shelve.open(files.bot_message_bd) as bd: start_message = bd['userfalse']
start_message = start_message.replace('uname', message.from_user.first_name)
bot.send_message(message.chat.id, start_message, parse_mode='Markdown')
			
elif '/adm' == message.text:
if not message.chat.id in in_admin:  in_admin.append(message.chat.id)
adminka.in_adminka(message.chat.id, message.text, message.chat.username, message.from_user.first_name)

elif  message.chat.id in in_admin: adminka.in_adminka(message.chat.id, message.text, message.chat.username, message.from_user.first_name)



@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):  

    if message.text == "⚙️ Инструменты":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🔩 Генераторы", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="⛓ Чекеры", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="📢 Спам, Флуд", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🔨 Разные", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        bot.send_message(message.chat.id, "⚙ *Полезные инструменты которые помогут вам в теневой сфере.*\n\n*Генераторы* — Инструменты которые генерирует информацию, фейковые данные и прочее полезное.\n\n*Чекеры* — Инструменты для чека валидности кредитных карт и других сервисов. \n\n*Спам, флуд* — Инструменты для спама, флуда по SMS, E-mail и других сервисов. \n\n*Разные инструменты* — Инструменты которые не попали по категориям выше.", reply_markup=keyboard, parse_mode='Markdown')
	
    if message.text == "ℹ Информация":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🔩 Генераторы", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="⛓ Чекеры", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="📢 Спам, Флуд", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🔨 Разные", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        bot.send_message(message.chat.id, "🔍 *Выберите нужную вам страну для поиска данных.* \n\n*«Пробив»* — это противоправная услуга, с помощью которой злоумышленники получают из закрытых баз данных информацию о конкретном человеке или организации. Естественно, за деньги. Существование такого предложения было бы невозможно без инсайдеров — сотрудников, у которых есть доступ к нужной информации для выполнения служебных обязанностей.", reply_markup=keyboard, parse_mode='Markdown')
	
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "uabtn":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="📥 Получить информацию", callback_data="uabtn1_1")
            btn2 = types.InlineKeyboardButton(text="📤 Запросить слив", callback_data="uabtn1_2")
            keyboard.add(btn1)
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📌 Выберите нужный вам режим для продолжения работы с ботом.", reply_markup=keyboard, parse_mode='Markdown')

        if call.data == "uabtn1_1":
            uabtn1_1_message = bot.send_message(chat_id=call.message.chat.id, text="📥 *Получить информацию под хайдом.*\n\nℹ️ Введите ID темы на форуме для слива содержимого под хайдом.", parse_mode='Markdown')
            bot.register_next_step_handler(uabtn1_1_message, auto_number_check)
		
        if call.data == "uabtn1_2":
            uabtn1_2_message = bot.send_message(chat_id=call.message.chat.id, text="📤 *Отправить запрос на слив хайда администраторам.*\n\nℹ️ Отправь мне ссылку на нужную вам тему для слива содержимого под хайдом.", parse_mode='Markdown')
            bot.register_next_step_handler(uabtn1_2_message, getcontact)
	
def getcontact(message):
    global ru_number_a
    ru_number_a = message.text
    response1 = requests.get('https://rosreestr.subnets.ru/?get=num&num=' + ru_number_a)
    data1 = response1.json()
    operator = data1["0"]["operator"]
    region1 = data1["0"]["region"]
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="🔍 Новый поиск", callback_data="uabtn1_2")
    keyboard.add(btn1)
    bot.send_message(message.chat.id, "*🚙 Информация по номеру: "+ru_number_a+"\n\n▪️ Оператор: "+operator+"\n▪️ Регион: "+region1, reply_markup=keyboard, parse_mode='Markdown')
		
def auto_number_check(message):
    global auto_number_a
    auto_number_a = message.text
    response = requests.get('https://fakescreen-3d98a1.eu1.kinto.io/ua?num=' + auto_number_a)
    data = response.json()
    region = data["region"]["name"]
    marka = data["vendor"]
    model = data["model"]
    year = data["year"]
    zametki = data["operations"][0]["notes"]
    data_reg = data["operations"][0]["regAt"]
    address = data["operations"][0]["address"]
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="🔍 Новый поиск", callback_data="uabtn1_1")
    keyboard.add(btn1)
    bot.send_message(message.chat.id, "*ℹ Результат по номеру: 🇺🇦 "+auto_number_a+"*\n\n*▪️ Марка автомобиля:* " +marka+ "\n️*▪️ Регион регестрации:* " +region+ "\n▪️ *Модель автомобиля:* " +model+ "\n*▪️ Информация:* " +zametki+ "\n*▪️ Дата последней регистрации:* " + data_reg, reply_markup=keyboard, parse_mode='Markdown')
        
bot.polling(none_stop=True)
