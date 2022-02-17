import telebot
import requests
import json
import sqlite3
from telebot import types
from random import randint
from config import token,otvetstart,idadmin,qiwinumber,token_qiwi,cena,oplatil,neoplatil

​token​​=​'5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'
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


@bot.message_handler(commands = ['start'])
def welcome(message):	
        service = telebot.types.ReplyKeyboardMarkup(True)
        service.row('🔍 Поиск данных', '⚙️ Инструменты')
        service.row('ℹ️ Информация', '🛠 Наши проекты')
        bot.send_message(message.chat.id, "👋🏽 Добро пожаловать, *"+ message.from_user.first_name +".**\n\nТЕНЕВОЙ ПОИСК — Я помогу тебе с поиском информации.*\n\nУ меня есть функции для поиска информации по интернету.\nДанный проект работает на абсолютно бесплатной основе и создан ради того, чтобы помочь вам в поисках лиц.\n\n👤 *По всем вопросам: @resilents*", reply_markup=service, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🔍 Поиск данных":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🇺🇦 Украина", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="🇷🇺 Россия", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="🇰🇿 Казахстан", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🇧🇾 Беларусь", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        bot.send_message(message.chat.id, "🔍 *Выберите нужную вам страну для поиска данных.* \n\n*«Пробив»* — это противоправная услуга, с помощью которой злоумышленники получают из закрытых баз данных информацию о конкретном человеке или организации. Существование такого предложения было бы невозможно без инсайдеров — сотрудников, у которых есть доступ к нужной информации для выполнения служебных обязанностей.", reply_markup=keyboard, parse_mode='Markdown')

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
            btn1 = types.InlineKeyboardButton(text="🚙 Информация о автомобиле", callback_data="uabtn1_1")
            btn2 = types.InlineKeyboardButton(text="📱 Информация о номере", callback_data="uabtn1_2")
            keyboard.add(btn1)
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔍  В данном разделе собраны сервисы для поиска информации по 🇺🇦 *Украине.*\n\nВыберите нужный вам вид поиска.", reply_markup=keyboard, parse_mode='Markdown')

        if call.data == "uabtn1_1":
            uabtn1_1_message = bot.send_message(chat_id=call.message.chat.id, text="🔍 *Получаем информацию о автомобиле по государственному номеру.*\n\n⚠️ Введите номер автомобиля для получения информации.\n\nℹ Пример номера: *AA6666BI*", parse_mode='Markdown')
            bot.register_next_step_handler(uabtn1_1_message, auto_number_check)
		
        if call.data == "uabtn1_2":
            uabtn1_2_message = bot.send_message(chat_id=call.message.chat.id, text="🔍 Поиск информации о автомобиле по гос. номеру:\n\nℹ️ Отправь мне номер авто для проверки, пример номера *AA1234BB.*", parse_mode='Markdown')
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
