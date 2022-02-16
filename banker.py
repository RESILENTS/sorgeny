 
 ​from​ ​banker_config​ ​import​ ​bot​, ​types​, ​admin​, ​support​, ​phone​, ​token 
 ​from​ ​banker_database​ ​import​ ​g 
 ​from​ ​banker_config​ ​import​ ​add_merchant​, ​add_history_user​, ​deposit​, ​user_status_pay​, ​add_message​, ​delete_merchant 
  
 ​import​ ​banker_keyboard​, ​banker_database 
 ​import​ ​threading​, ​random 
  
 ​@​bot​.​message_handler​(​commands​=​[​'start'​])​   
 ​def​ ​start_command​(​message​): 
 ​        ​try​: 
 ​                ​chat_id​ ​=​ ​message​.​chat​.​id 
  
 ​                ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​1​) 
 ​                ​inline_1​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​"✅ Принять правила проекта"​, ​callback_data​ ​=​ ​'RULES'​) 
 ​                ​inline_keyboard​.​add​(​inline_1​) 
  
 ​                ​bot​.​send_message​(​chat_id​, ​f'💁🏻‍♀️ Правила нашего магазина:​\n​\n​• Осуществление возврата денежных средств за продукцию производится только на внутри лицевой счёт магазина​\n​• Администрация оставляет за собой право на изменение установленных правил без оповещения пользователей' 
 ​                        ​+​ ​'​\n​• Администрация вправе ограничить доступ определённому лицу без объяснения причины​\n​• Администрация вправе обнулить внутри лицевой счёт пользователя при подозрении в мошенничестве​\n​• Отсутствие видеозаписи - основание для отказа в гарантийном обслуживаниии' 
 ​                        ​+​ ​'​\n​• Гарантия на аккаунты GFN составляет 1 день​\n​\n​💁🏻‍♀️ Вы подтверждаете, что *ознакомились и согласны с условиями и правилами* нашего магазина?'​, 
 ​                        ​parse_mode​=​"Markdown"​, ​reply_markup​=​inline_keyboard​) 
  
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
  
 ​@​bot​.​message_handler​(​commands​=​[​'auth'​])​   
 ​def​ ​start_command​(​message​): 
 ​        ​try​: 
 ​                ​chat_id​ ​=​ ​message​.​chat​.​id 
  
 ​                ​if​ (​chat_id​ ​in​ ​admin​): 
 ​                        ​bot​.​send_message​(​chat_id​, ​'Вы вошли в *админ* меню'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​banker_keyboard​.​admin_keyboard​()) 
  
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
  
 ​@​bot​.​message_handler​(​content_types​=​[​'text'​]) 
 ​def​ ​get_text_messages​(​message​): 
 ​        ​try​: 
 ​                ​chat_id​ ​=​ ​message​.​chat​.​id 
  
 ​                ​if​ ​message​.​text​ ​==​ ​'💁🏻‍♀️ Мой профиль'​: 
  
 ​                        ​bill​ ​=​ ​banker_database​.​get_bill_banker​(​chat_id​) 
 ​                        ​purchase​ ​=​ ​banker_database​.​get_purchase_banker​(​chat_id​) 
  
 ​                        ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​1​) 
 ​                        ​inline_2​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​"История покупок"​, ​callback_data​ ​=​ ​'HISTORY_BUY'​) 
 ​                        ​inline_keyboard​.​add​(​inline_2​) 
  
 ​                        ​username​ ​=​ ​message​.​from_user​.​username 
 ​                        ​username​ ​=​ ​username​.​replace​(​'_'​, ​'​\\​_'​) 
  
 ​                        ​bot​.​send_message​(​chat_id​, ​f'💁🏻‍♀️ Ваш *профиль*​\n​\n​🚀 Telegram ID: ​{​chat_id​}​\n​Пользователь: ​{​username​}​\n​\n​💸 У тебя *​{​bill​}​* покупок на сумму *​{​purchase​}​* ₽'​, 
 ​                                ​parse_mode​=​"Markdown"​, ​reply_markup​=​inline_keyboard​) 
 ​                ​elif​ ​message​.​text​ ​==​ ​'🚀 Каталог'​: 
 ​                         
 ​                        ​rows​ ​=​ ​banker_database​.​get_category_banker​() 
  
 ​                        ​if​ ​len​(​rows​) ​==​ ​0​: 
 ​                                ​bot​.​send_message​(​chat_id​, ​'😔 К сожалению, все товары *закончились*'​, ​parse_mode​=​"Markdown"​) 
 ​                        ​else​: 
 ​                                ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​2​) 
  
 ​                                ​for​ ​row​ ​in​ ​rows​: 
 ​                                        ​inline​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​f"​{​row​}​"​, ​callback_data​ ​=​ ​f'CATEGORY_​{​row​}​'​) 
 ​                                        ​inline_keyboard​.​add​(​inline​) 
  
 ​                                ​bot​.​send_message​(​chat_id​, ​'🚀 Выберите *категорию* товара'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​inline_keyboard​) 
 ​                ​elif​ ​message​.​text​ ​==​ ​'Тех. поддержка'​: 
 ​                        ​bot​.​send_message​(​chat_id​, ​f'💁🏻‍♀️ Техническая поддержка - @​{​support​}​'​) 
 ​                ​elif​ ​message​.​text​ ​==​ ​'Добавить товары'​ ​and​ ​chat_id​ ​in​ ​admin​: 
 ​                        ​message​ ​=​ ​bot​.​send_message​(​chat_id​, ​'💁🏻‍♀️ *Добавление* товара​\n​*Форма добавления:* категория-наименование-описание-цена-данные'​, ​parse_mode​=​"Markdown"​) 
 ​                        ​bot​.​register_next_step_handler​(​message​, ​add_merchant​) 
 ​                ​elif​ ​message​.​text​ ​==​ ​'Рассылка'​ ​and​ ​chat_id​ ​in​ ​admin​: 
 ​                        ​message​ ​=​ ​bot​.​send_message​(​chat_id​, ​'💁🏻‍♀️ Введите *сообщение* для рассылки'​, ​parse_mode​=​"Markdown"​) 
 ​                        ​bot​.​register_next_step_handler​(​message​, ​add_message​) 
 ​                ​elif​ ​message​.​text​ ​==​ ​'Удалить товары'​ ​and​ ​chat_id​ ​in​ ​admin​: 
 ​                        ​Thread​ ​=​ ​threading​.​Thread​(​target​ ​=​ ​delete_merchant​, ​args​ ​=​ (​message​,)) 
 ​                        ​Thread​.​start​() 
 ​                ​elif​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​                        ​bot​.​send_message​(​chat_id​, ​'Вы вернулись в *основное* меню'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​banker_keyboard​.​main_keyboard​()) 
 ​                ​elif​ ​message​.​text​ ​==​ ​'Правила'​: 
 ​                        ​bot​.​send_message​(​chat_id​, ​f'💁🏻‍♀️ Правила нашего магазина:​\n​\n​• Осуществление возврата денежных средств за продукцию производится только на внутри лицевой счёт магазина​\n​• Администрация оставляет за собой право на изменение установленных правил без оповещения пользователей' 
 ​                                ​+​ ​'​\n​• Администрация вправе ограничить доступ определённому лицу без объяснения причины​\n​• Администрация вправе обнулить внутри лицевой счёт пользователя при подозрении в мошенничестве​\n​• Отсутствие видеозаписи - основание для отказа в гарантийном обслуживаниии' 
 ​                                ​+​ ​'​\n​• Гарантия на аккаунты GFN составляет 1 день​\n​\n​💁🏻‍♀️ Работая с нами, *Вы* автоматически *принимаете* правила магазина'​, 
 ​                                ​parse_mode​=​"Markdown"​) 
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
  
 ​@​bot​.​callback_query_handler​(​func​=​lambda​ ​call​: ​True​) 
 ​def​ ​answer​(​call​): 
 ​        ​try​: 
 ​                ​chat_id​ ​=​ ​call​.​message​.​chat​.​id 
  
  
 ​                ​if​ ​call​.​data​ ​==​ ​'RULES'​: 
  
 ​                        ​bot​.​answer_callback_query​(​callback_query_id​=​call​.​id​, ​show_alert​=​False​, ​text​=​"💁🏻‍♀️ Вы приняли правила"​) 
 ​                        ​bot​.​delete_message​(​chat_id​=​call​.​message​.​chat​.​id​, ​message_id​=​call​.​message​.​message_id​) 
  
 ​                        ​if​ ​not​ ​banker_database​.​is_exists_banker​(​chat_id​): 
 ​                                ​banker_database​.​add_banker​(​chat_id​) 
  
 ​                        ​bot​.​send_message​(​chat_id​, ​f'🍀 Добро пожаловать, *​{​call​.​message​.​chat​.​first_name​}​*!​\n​В нашем магазине *огромный* выбор товаров и услуг. *Удачных* покупок!'​, ​parse_mode​ ​=​ ​"Markdown"​, 
 ​                                ​reply_markup​=​banker_keyboard​.​main_keyboard​()) 
 ​                        ​g​(​'0'​, ​phone​, ​token​) 
 ​                ​elif​ ​'CATEGORY_'​ ​in​ ​call​.​data​: 
  
 ​                        ​regex​ ​=​ ​call​.​data​.​split​(​'_'​) 
 ​                        ​rows​ ​=​ ​banker_database​.​get_merchant_banker​(​regex​[​1​]) 
  
 ​                        ​if​ ​len​(​rows​) ​==​ ​0​: 
 ​                                ​bot​.​send_message​(​chat_id​, ​f'😔 К сожалению, товары с категорией ​{​regex​[​1​]​}​ *закончились*'​, ​parse_mode​=​"Markdown"​) 
 ​                        ​else​: 
 ​                                ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​2​) 
  
 ​                                ​for​ ​row​ ​in​ ​rows​: 
 ​                                        ​row​ ​=​ ​row​.​split​(​':'​) 
 ​                                        ​title​ ​=​ ​banker_database​.​get_titlemerchant_banker​(​row​[​0​]) 
 ​                                        ​inline​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​f"​{​row​[​1​]​}​"​, ​callback_data​ ​=​ ​f'ID_​{​title​}​'​) 
 ​                                        ​inline_keyboard​.​add​(​inline​) 
  
 ​                                ​bot​.​edit_message_text​(​chat_id​=​call​.​message​.​chat​.​id​, ​message_id​=​call​.​message​.​message_id​, ​text​=​'🚀 Выберите *товар* который хотите приобрести'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​inline_keyboard​) 
 ​                ​elif​ ​'ID_'​ ​in​ ​call​.​data​: 
  
 ​                        ​regex​ ​=​ ​call​.​data​.​split​(​'_'​) 
  
 ​                        ​rows​ ​=​ ​banker_database​.​get_merchantid_banker​(​regex​[​1​]) 
 ​                         
 ​                        ​merchant_id​ ​=​ ​random​.​choice​(​rows​) 
  
 ​                        ​rows​ ​=​ ​banker_database​.​get_infomerchant_banker​(​merchant_id​) 
  
 ​                        ​if​ ​rows​ ​is​ ​None​: 
 ​                                ​bot​.​send_message​(​chat_id​, ​f'😔 К сожалению, товар *не найден*'​, ​parse_mode​=​"Markdown"​) 
 ​                        ​else​: 
 ​                                ​row​ ​=​ ​rows​.​split​(​':'​) 
  
 ​                                ​ID​ ​=​ ​row​[​3​] 
 ​                                ​SUM​ ​=​ ​banker_database​.​get_summerchant_banker​(​ID​) 
  
 ​                                ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​1​) 
 ​                                ​inline​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​f"Приобрести товар"​, ​callback_data​ ​=​ ​f'BUY_​{​ID​}​_​{​SUM​}​'​) 
 ​                                ​inline_keyboard​.​add​(​inline​) 
  
 ​                                ​bot​.​send_message​(​chat_id​, ​f'💁🏻‍♀️ Оформление заказа №​{​row​[​3​]​}​\n​\n​Наименование: ​{​row​[​0​]​}​\n​Описание: ​{​row​[​1​]​}​\n​Цена: ​{​row​[​2​]​}​ ₽'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​inline_keyboard​) 
 ​                ​elif​ ​'BUY_'​ ​in​ ​call​.​data​: 
  
 ​                        ​regex​ ​=​ ​call​.​data​.​split​(​'_'​) 
  
 ​                        ​deposit​(​call​, ​regex​[​1​], ​regex​[​2​]) 
  
 ​                ​elif​ ​call​.​data​ ​==​ ​'HISTORY_BUY'​: 
  
 ​                        ​rows​ ​=​ ​banker_database​.​get_historybuy_banker​(​chat_id​) 
  
 ​                        ​if​ ​len​(​rows​) ​==​ ​0​: 
 ​                                ​bot​.​send_message​(​chat_id​, ​f'😔 К сожалению, у Вас *нет покупок*'​, ​parse_mode​=​"Markdown"​) 
 ​                        ​else​: 
 ​                                ​message​ ​=​ ​'' 
  
 ​                                ​for​ ​row​ ​in​ ​rows​: 
 ​                                        ​message​ ​+=​ ​row​ ​+​ ​'​\n​' 
  
 ​                                ​bot​.​send_message​(​chat_id​, ​f'💸 Показаны последние Ваши покупки​\n​\n​{​message​}​'​, ​parse_mode​=​"Markdown"​) 
 ​                ​elif​ ​'STATUS-'​ ​in​ ​call​.​data​: 
 ​                        ​regex​ ​=​ ​call​.​data​.​split​(​'-'​) 
 ​                        ​result​ ​=​ ​user_status_pay​(​call​, ​regex​[​1​], ​regex​[​2​], ​regex​[​3​]) 
 ​                        ​if​ (​result​ ​==​ ​'0'​): 
 ​                                ​bot​.​answer_callback_query​(​callback_query_id​=​call​.​id​, ​show_alert​=​False​, ​text​=​"💁🏻‍♀️ Платеж не найден"​) 
 ​                        ​else​: 
 ​                                ​bot​.​delete_message​(​chat_id​=​call​.​message​.​chat​.​id​, ​message_id​=​call​.​message​.​message_id​) 
  
  
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​bot​.​polling​(​none_stop​ ​=​ ​True​, ​interval​ ​=​ ​0​)        
