import telebot
import requests
import json
import sqlite3
from telebot import types
from random import randint
from config import token

bot=telebot.TeleBot(token)
ADMIN = 1938749145
idcanal = 1001418408821

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=["start"])
def welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_main1 = types.KeyboardButton(text="📩 Получить хайд")
    btn_main2 = types.KeyboardButton(text="📤 Новый запрос")
    btn_main3 = types.KeyboardButton(text="🏠 Главное меню")
    keyboard.add(btn_main1, btn_main2)
    keyboard.add(btn_main3)
    bot.send_message(message.chat.id, '🏠 Добро пожаловать в главное меню.',parse_mode='HTML', reply_markup=keyboard)

    userid = str(message.chat.id)
    text = "<b>SORGENY</b> — Я помогу тебе получить скрытую информацию с разных интернет ресурсов.\n\nУ меня есть база данных слитых хайдов с разных интернет площадок. Более подробнее о боте вы сможете узнать в разделе информация."
    img = open ('welc.webp', 'rb')
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="📩 Получить хайд", callback_data="getlink3")
    btn2 = types.InlineKeyboardButton(text="ℹ️ Информация", callback_data="test")
    btn3 = types.InlineKeyboardButton(text="💭 Наш чат", callback_data="uabtn")
    btn4 = types.InlineKeyboardButton(text="📢 Наш канал", callback_data="test")
    btn5 = types.InlineKeyboardButton(text="📊 Статистика", callback_data="test")
    btn6 = types.InlineKeyboardButton(text="👥 Поддержка", callback_data="test")

    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    keyboard.add(btn5, btn6)
    bot.send_photo(message.from_user.id, img, caption=text, reply_markup=keyboard, parse_mode='html')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):  
    if message.text == "admin666":
        if message.from_user.id == ADMIN:
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="🔗 Новый пост", callback_data="go_to_db")
            btn2 = types.InlineKeyboardButton(text="📥 Запросы", callback_data="test")
            btn3 = types.InlineKeyboardButton(text="📃 Рассылка", callback_data="test")
            keyboard.add(btn1, btn2)
            keyboard.add(btn3)
            bot.send_message(message.chat.id, "Добро пожаловать в админ панель.", reply_markup=keyboard, parse_mode='Markdown')
        
    if message.text == "📩 Получить хайд":
        global link_idm
        link_idm = message.text
        msg = bot.send_message(message.chat.id, f'''🔍  <b>Введите ссылку для поиска в базе данных.</b>
	
⚠️  <b>ВНИМАНИЕ!</b> Если вы отправите ссылку с не актуальным доменом то <b>БОТ</b> не сможет найти запись в базе данных.
        
🟢  <b>Актуальные домены:</b>
 — slivup.cc
 — s1.slivup.net''',parse_mode='HTML')
        bot.register_next_step_handler(msg, getlinkm)

def getlinkm(message):
        global link_coment, link_text, sql, link_id
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        link_coment = ""
        link_text = ""
        link_id = message.text
        sql = "SELECT * FROM links WHERE link_id =?"
        result = cursor.fetchall()
        for row in cursor.execute(sql, ([link_id])):
                if  result.fetchone() is None: 
                      bot.send_message(message.chat.id, "test")
                else:
            link_id = list(row)[0]
            link_coment = list(row)[1]
            link_text = list(row)[2]
        bot.send_message(message.chat.id, f'''🔍  <b>Результат по вашему запросу:</b>

🔗  <b>Ссылка вашего запроса: </b>
{link_id}

🔐  <b>Скрытое содержимое: </b>
{link_text}

''', parse_mode='HTML')

def add1(message):
        global m1
        m1 = message.text
        msg = bot.send_message(message.chat.id, '➕ Введите коментарии к посту.',parse_mode='HTML')
        bot.register_next_step_handler(msg, add2)

def add2(message):
        global m2
        m2 = message.text
        msg = bot.send_message(message.chat.id, '➕ Введите скрытое содержимое.',parse_mode='HTML')
        bot.register_next_step_handler(msg, add3)

def add3(message):
        global m3
        m3 = message.text
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='✅ Опубликовать пост',callback_data=f'принятьзаявку_{message.chat.id}'))
        bot.send_message(message.chat.id, f'''Предпросмотр публикации:

◾ Ссылка: {m1}
◾ Содержимое скрытого текста: {m3}

◾ Коментарии к публикации:
{m2}''',parse_mode='HTML',reply_markup=keyboard)

def db_table_val(link_id: str, link_coment: str, link_text: str):
    params = (link_id, link_coment, link_text)
    cursor.execute(f'''INSERT INTO links (link_id, link_coment, link_text) VALUES ('{m1}', '{m3}', '{m2}')''')
    conn.commit()
        
@bot.callback_query_handler(func=lambda call:True)
def podcategors(call):
    if call.data == 'go_to_db':
        msg = bot.send_message(call.message.chat.id, '➕ Введите главную ссылку.\n\n Внимание! По этой ссылке будет производится поиск в базе данных.',parse_mode='HTML')
        bot.register_next_step_handler(msg, add1)

    if call.data == 'getlink2':
        msg = bot.send_message(call.message.chat.id, '➕ Введите ссылку для поиска в базе данных',parse_mode='HTML')
        bot.register_next_step_handler(msg, getlinkm)
	
    if call.data == 'getlink3':
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        text = "➕ Введите ссылку для поиска в базе данных"
        img = open ('welc.webp', 'rb')
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="📩 Новый запрос", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="🏠 Главное меню", callback_data="go_home")
        keyboard.add(btn1, btn2)
        msg = bot.send_photo(call.message.chat.id, img, caption=text, reply_markup=keyboard, parse_mode='html')
        bot.register_next_step_handler(msg, getlinkm)

    if call.data[:14] == 'принятьзаявку_':
        idasd = call.data[14:]
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        main = telebot.types.ReplyKeyboardMarkup(True)
        bot.send_message(idasd,reply_markup=main, text='hhh')

        link_id = {m1}
        link_coment = {m3}
        link_text = {m2}
        db_table_val(link_id=link_id, link_coment=link_coment, link_text=link_text)

    if call.data == 'go_home':
        bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        text = "SORGENY — Я помогу тебе получить скрытую информацию с разных интернет ресурсов.\n\nУ меня есть база данных слитых хайдов с разных интернет площадок. Более подробнее о боте вы сможете узнать в разделе информация."
        img = open ('welc.webp', 'rb')
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="📩 Получить хайд", callback_data="getlink3")
        btn2 = types.InlineKeyboardButton(text="ℹ️ Информация", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="💭 Наш чат", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="📢 Наш канал", callback_data="test")
        btn5 = types.InlineKeyboardButton(text="📊 Статистика", callback_data="test")
        btn6 = types.InlineKeyboardButton(text="👥 Поддержка", callback_data="test")

        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        keyboard.add(btn5, btn6)
        bot.send_photo(call.message.chat.id, img, caption=text, reply_markup=keyboard, parse_mode='html')

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
	
bot.polling(none_stop = True, interval = 0)
