import telebot
import requests
import json
import sqlite3
from telebot import types
from random import randint
from config import token

bot=telebot.TeleBot(token)
ADMIN = 641892529
idcanal = 1001418408821

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(types.InlineKeyboardButton(text="➕ Добавить в базу"))
kb.add(types.InlineKeyboardButton(text="📥 Новые запросы"))
kb.add(types.InlineKeyboardButton(text="📋 Рассылка"))

@bot.message_handler(commands=["start"])
def welcome(message):
    userid = str(message.chat.id)
    text = "🌈 SORGENY — Я помогу тебе получить скрытую информацию с разных интернет ресурсов.\n\nℹ️ У меня есть база данных слитых хайдов с разных интернет площадок. Более подробнее о боте вы сможете узнать в разделе информация."
    img = open ('welc.webp', 'rb')
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="🛠️ Получить скрытое содержимое", callback_data="uabtn")
    btn2 = types.InlineKeyboardButton(text="ℹ️ Информация", callback_data="test")
    btn3 = types.InlineKeyboardButton(text="📢 Наши проекты", callback_data="test")
    btn4 = types.InlineKeyboardButton(text="📊 Статистика", callback_data="test")
    btn6 = types.InlineKeyboardButton(text="📃 Открыть главное меню", callback_data="test")
    btn5 = types.InlineKeyboardButton(text="👥 Поддержка", callback_data="test")
    keyboard.add(btn1)
    keyboard.add(btn2, btn3)
    keyboard.add(btn6)
    keyboard.add(btn4, btn5)
    bot.send_photo(message.from_user.id, img, caption=text, reply_markup=keyboard, parse_mode='html')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):  
    if message.text == "➕ Добавить в базу":
        if message.from_user.id == ADMIN:
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="➕ Добавить", callback_data="податьзаявку")
            btn2 = types.InlineKeyboardButton(text="📃 Меню", callback_data="test")
            keyboard.add(btn1, btn2)
            bot.send_message(message.chat.id, "Для публикации нового поста нажмите на кнопку ниже.", reply_markup=keyboard, parse_mode='Markdown')

    if message.text == "ℹ Информация":  
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="🔩 Генераторы", callback_data="uabtn")
        btn2 = types.InlineKeyboardButton(text="⛓ Чекеры", callback_data="test")
        btn3 = types.InlineKeyboardButton(text="📢 Спам, Флуд", callback_data="test")
        btn4 = types.InlineKeyboardButton(text="🔨 Разные", callback_data="test")
        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)
        bot.send_message(message.chat.id, "🔍 *Выберите нужную вам страну для поиска данных.* \n\n*«Пробив»* — это противоправная услуга, с помощью которой злоумышленники получают из закрытых баз данных информацию о конкретном человеке или организации. Естественно, за деньги. Существование такого предложения было бы невозможно без инсайдеров — сотрудников, у которых есть доступ к нужной информации для выполнения служебных обязанностей.", reply_markup=keyboard, parse_mode='Markdown')
	
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

@bot.callback_query_handler(func=lambda call:True)
def podcategors(call):
	if call.data == 'податьзаявку':
		msg = bot.send_message(call.message.chat.id, '➕ Введите главную ссылку.\n\n Внимание! По этой ссылке будет производится поиск в базе данных.',parse_mode='HTML')
		bot.register_next_step_handler(msg, add1)

	if call.data[:14] == 'принятьзаявку_':
		idasd = call.data[14:]
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		main = telebot.types.ReplyKeyboardMarkup(True)
		bot.answer_callback_query(callback_query_id=call.id, show_alert=True, call_data=create_db, text="Готово")
		bot.send_message(idasd,reply_markup=main)

	if call.data == 'create_db':
		msg = bot.send_message(call.message.chat.id, '➕ Введите главную ссылку.\n\n Внимание! По этой ссылке будет производится поиск в базе данных.',parse_mode='HTML')
		bot.register_next_step_handler(msg, create_db1)

def create_db1(id): 
    global db
    db=sqlite3.connect('db.db') 
    cursor=db.cursor() 
    cursor.execute(f"""create table links_db (
    link_id varchar(90) NOT NULL,
    coment_link varchar(90) NOT NULL,
    hide_link varchar(90) NOT NULL,
    PRIMARY KEY (link_id)
    );""") 
    db.commit()

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
		
 
  
 ​if​ ​__name__​ ​==​ ​'__main__'​: 
 ​        ​try​: 
 ​                ​bot​.​polling​(​none_stop​ ​=​ ​True​, ​interval​ ​=​ ​0​) 
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​bot​.​send_message​(​admin_chat​, ​text​=​f"<b>Возникла ошибка</b>​\n​\n​{​e​}​"​, ​parse_mode​=​"HTML"​) 
 ​                ​while​ ​True​: 
 ​                        ​try​: 
 ​                                ​bot​.​polling​(​none_stop​ ​=​ ​True​, ​interval​ ​=​ ​0​) 
 ​                        ​except​ ​Exception​ ​as​ ​e​: 
 ​                                ​bot​.​send_message​(​admin_chat​, ​text​=​f"<b>Возникла ошибка!</b>​\n​\n​{​e​}​"​, ​parse_mode​=​"HTML"​)
