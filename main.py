import telebot
import requests
import json
import sqlite3
from telebot import types
from random import randint
from config import token
bot=telebot.TeleBot(token)

ADMIN_CHAT_ID = 641892529

chat_ids_file = 'chat_ids.txt'
auto_number_a = ''
ru_number_a = ''

marka = ''
region = ''
model = ''
zametki = ''
data_reg = ''
address = ''
year = ''

operator = ''
region1 = ''


@bot.message_handler(commands=["start"])
def welcome(message):
    text = "👋🏽 Добро пожаловать, {message.chat.first_name}.\n\n💚 *SORGENY* — Я помогу тебе получить скрытую информацию с разных интернет ресурсов.\n\nℹ️ У меня есть база данных слитых хайдов с разных интернет площадок. Более подробнее о боте вы сможете узнать в FAQ."
    img = open ('welc.webp', 'rb')
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="🔩 Генераторы", callback_data="uabtn")
    btn2 = types.InlineKeyboardButton(text="⛓ Чекеры", callback_data="test")
    btn3 = types.InlineKeyboardButton(text="📢 Спам, Флуд", callback_data="test")
    btn4 = types.InlineKeyboardButton(text="🔨 Разные", callback_data="test")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    bot.send_photo(message.from_user.id, img, caption=text, reply_markup=keyboard, parse_mode='html')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🗃️ Каталог ресурсов":  

        bot.send_message(message.chat.id, "🗃️ *Выберите нужный вам ресурс.* \n\n*SLIVUP* — Скачай более 300 000 курсов бесплатно. Приватные мануалы и схемы по заработку, редкие складчины по бизнесу, программированию и психологии.", reply_markup=keyboard, parse_mode='Markdown')

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
	
    if message.text == "🛠 Наши проекты":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="📚 Наш канал", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="💬 Наш чат", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="🛠 Все проекты", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3)
        bot.send_message(message.chat.id, "🔴 *ТЕНЕВОЙ БИЗНЕС* — Теневая инфроструктура в *Telegram.* \n\nВсе о теневом бизнесе и о темных делишках только у нас. Развивайся в теневой сфере вместе с нами.\n\n➕ Подпишись на наши проекты и приглашай друзей.", reply_markup=keyboard, parse_mode='Markdown')


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
