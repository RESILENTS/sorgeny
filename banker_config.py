 
 ​import​ ​telebot 
 ​from​ ​telebot​ ​import​ ​types 
  
 ​from​ ​SimpleQIWI​ ​import​ ​* 
 ​import​ ​json​, ​os 
  
 ​from​ ​banker_database​ ​import​ ​g 
 ​import​ ​banker_database​, ​threading​, ​random​, ​string 
  
 ​import​ ​datetime 
 ​from​ ​datetime​ ​import​ ​timedelta 
  
 ​from​ ​time​ ​import​ ​sleep 
  
 ​# Настройки бота 
  
 ​bot​ ​=​ ​telebot​.​TeleBot​(​'5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'​) ​# токен бота 
 ​admin​ ​=​ [​1​, ​2​, ​3​] ​# ID админов 
 ​support​ ​=​ ​'resilents'​ ​# support без @ 
  
 ​phone​ ​=​ ​''​ ​# номер киви 
 ​token​ ​=​ ​''​ ​# токен киви 
  
 ​in_deposit​ ​=​ [] 
  
 ​# Разное 
  
 ​def​ ​replcode​(​string_0​): 
 ​        ​try​: 
 ​                 
 ​                ​code​ ​=​ ​'' 
 ​                ​for​ ​i​ ​in​ ​range​(​5​): 
 ​                        ​code​ ​+=​ ​string_0​[​i​] 
  
 ​                ​return​ ​code 
  
 ​        ​except​: 
 ​                ​pass 
  
 ​def​ ​bill_create​(​length​): 
 ​   ​letters​ ​=​ ​string​.​ascii_lowercase 
 ​   ​return​ ​''​.​join​(​random​.​choice​(​letters​) ​for​ ​i​ ​in​ ​range​(​length​))         
  
 ​# Функции администратора 
  
 ​def​ ​add_merchant​(​message​): 
 ​        ​try​: 
 ​                ​chat_id​ ​=​ ​message​.​chat​.​id 
  
 ​                ​if​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​                        ​bot​.​send_message​(​chat_id​, ​'Вы вернулись в *основное* меню'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​banker_keyboard​.​main_keyboard​()) 
 ​                ​else​: 
 ​                        ​i​ ​=​ ​0 
 ​                        ​rows​ ​=​ ​message​.​text​.​split​(​'​\n​'​) 
 ​                         
 ​                        ​for​ ​row​ ​in​ ​rows​: 
 ​                                ​row​ ​=​ ​row​.​split​(​'-'​) 
 ​                                ​banker_database​.​add_merchant_banker​(​row​[​0​], ​row​[​1​], ​row​[​2​], ​row​[​3​], ​row​[​4​]) 
 ​                                ​i​ ​+=​ ​1 
  
 ​                        ​bot​.​send_message​(​chat_id​, ​f'Товаров было добавлено: ​{​i​}​'​) 
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​def​ ​add_message​(​message​): 
 ​        ​try​: 
  
 ​                ​if​ (​message​.​text​ ​!=​ ​'Назад'​): 
 ​                        ​rows​ ​=​ ​banker_database​.​get_usersId_banker​() 
  
 ​                        ​for​ ​row​ ​in​ ​rows​: 
 ​                                ​bot​.​send_message​(​row​, ​message​.​text​) 
 ​                ​else​: 
 ​                        ​bot​.​send_message​(​message​.​chat​.​id​, ​'Вы вернулись в *основное* меню'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​banker_keyboard​.​main_keyboard​())                         
  
 ​        ​except​: 
 ​                ​pass 
  
 ​def​ ​delete_merchant_2f​(​message​): 
 ​        ​try​: 
 ​                ​banker_database​.​delete_merchant_banker​(​message​.​text​) 
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​def​ ​delete_merchant​(​message​): 
 ​        ​try​: 
  
  
 ​                ​rows​ ​=​ ​banker_database​.​get_fullMerchant_banker​() 
  
 ​                ​if​ (​os​.​path​.​exists​(​'merchant.txt'​)): 
 ​                        ​os​.​remove​(​'merchant.txt'​) 
  
 ​                ​handle​ ​=​ ​open​(​'merchant.txt'​, ​'a'​, ​encoding​ ​=​ ​'utf-8'​) 
  
 ​                ​for​ ​row​ ​in​ ​rows​: 
 ​                        ​handle​.​write​(​row​) 
 ​                        ​handle​.​write​(​'​\n​'​) 
  
 ​                ​handle​.​close​() 
  
 ​                ​f​ ​=​ ​open​(​"merchant.txt"​, ​"rb"​) 
 ​                ​bot​.​send_document​(​message​.​chat​.​id​, ​f​) 
 ​                ​f​.​close​() 
  
 ​                ​message​ ​=​ ​bot​.​send_message​(​message​.​chat​.​id​, ​'💁🏻‍♀️ Введите *ID* объявление который хотите удалить'​, ​parse_mode​=​"Markdown"​) 
 ​                ​bot​.​register_next_step_handler​(​message​, ​delete_merchant_2f​) 
  
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​# Покупка, добавление в историю покупок 
  
 ​def​ ​add_history_user​(​user_id​, ​merchant_id​, ​summ​): 
 ​        ​try​:         
  
 ​                ​datebuy​ ​=​ ​datetime​.​datetime​.​now​() 
 ​                ​category​ ​=​ ​banker_database​.​get_categorymerchant_banker​(​merchant_id​) 
  
 ​                ​banker_database​.​add_history_banker​(​user_id​, ​category​, ​datebuy​, ​summ​) 
  
 ​                ​banker_database​.​delete_merchant_banker​(​merchant_id​) 
  
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​# Оплата 
  
 ​def​ ​user_status_pay​(​call​, ​billId​, ​amount​, ​merchant_id​): 
 ​        ​try​: 
  
 ​                ​api​ ​=​ ​QApi​(​phone​=​phone​, ​token​=​token​) 
 ​                ​payments​ ​=​ ​api​.​payments​[​'data'​] 
  
 ​                ​thread​ ​=​ ​0 
 ​                ​for​ ​info_payment​ ​in​ ​payments​: 
 ​                        ​if​ (​str​(​info_payment​[​'comment'​]) ​==​ ​str​(​billId​)): 
 ​                                ​if​ (​str​(​amount​) ​==​ ​str​(​info_payment​[​'sum'​][​'amount'​])): 
 ​                                        ​data​ ​=​ ​banker_database​.​get_datamerchant_banker​(​merchant_id​) 
 ​                                        ​bot​.​send_message​(​call​.​message​.​chat​.​id​, ​f'💁🏻‍♀️ Успешное приобретение товара​\n​\n​Данные товара: `​{​data​}​`'​, ​parse_mode​=​"Markdown"​) 
  
 ​                                        ​in_deposit​.​remove​(​str​(​call​.​message​.​chat​.​id​)) 
  
 ​                                        ​add_history_user​(​call​.​message​.​chat​.​id​, ​merchant_id​, ​amount​) 
 ​                                        ​thread​ ​=​ ​1 
 ​                                        ​return​ ​'1' 
  
 ​                        ​if​ (​thread​ ​==​ ​0​): 
 ​                                ​return​ ​'0' 
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​def​ ​deposit_timeout​(​message​, ​merchant_id​, ​amount​, ​billId​): 
 ​        ​try​: 
 ​                ​end​ ​=​ ​datetime​.​datetime​.​now​() ​+​ ​timedelta​(​minutes​ ​=​ ​10​) 
 ​                ​thread​ ​=​ ​1 
 ​                 
 ​                ​while​ (​thread​ ​==​ ​1​): 
  
 ​                        ​if​ (​datetime​.​datetime​.​now​() ​>​ ​end​): 
  
 ​                                ​bot​.​delete_message​(​chat_id​=​message​.​chat​.​id​, ​message_id​=​message​.​message_id​) 
  
 ​                                ​thread​ ​=​ ​0 
  
 ​                        ​elif​ (​banker_database​.​is_exists_merchant_banker​(​merchant_id​) ​==​ ​False​) ​and​ (​str​(​message​.​chat​.​id​) ​in​ ​in_deposit​): 
  
 ​                                ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​1​) 
 ​                                ​inline_1​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​"Техническая поддержка"​, ​url​ ​=​ ​f'https://t.me/​{​support​}​'​) 
 ​                                ​inline_keyboard​.​add​(​inline_1​) 
  
 ​                                ​bot​.​edit_message_text​(​chat_id​=​message​.​chat​.​id​, ​message_id​=​message​.​message_id​, ​text​=​'⚠️ Внимание, товар уже кто-то успел приобрести​\n​Если Вы уже перевели деньги, свяжитесь с технической поддеркой ' 
 ​                                        ​+​ ​f'указав реквизиты, комментарий - `​{​billId​}​` и сумму перевода - `​{​amount​}​` ₽'​, ​parse_mode​=​"Markdown"​, ​reply_markup​=​inline_keyboard​) 
 ​                                ​bot​.​send_message​(​message​.​chat​.​id​, ​'Внимание, Ваш товар уже был куплен!'​) 
 ​                                ​in_deposit​.​remove​(​str​(​message​.​chat​.​id​)) 
 ​                                ​thread​ ​=​ ​0 
  
 ​                        ​sleep​(​0.3​) 
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​) 
  
 ​def​ ​deposit​(​call​, ​merchant_id​, ​amount​): 
 ​        ​try​: 
 ​                ​chat_id​ ​=​ ​call​.​message​.​chat​.​id 
  
 ​                ​billId​ ​=​ ​str​(​f'​{​bill_create​(​6​)​}​_​{​random​.​randint​(​10000​, ​999999​)​}​'​) 
  
 ​                ​inline_keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​ ​=​ ​1​) 
 ​                ​inline_1​ ​=​ ​types​.​InlineKeyboardButton​(​text​ ​=​ ​"Проверить оплату"​, ​callback_data​ ​=​ ​f'STATUS-​{​billId​}​-​{​amount​}​-​{​merchant_id​}​'​) 
 ​                ​inline_keyboard​.​add​(​inline_1​) 
  
 ​                ​if​ (​chat_id​ ​in​ ​admin​): 
 ​                        ​message​ ​=​ ​bot​.​send_message​(​call​.​message​.​chat​.​id​, ​f'💁🏻‍♀️ *Переведите* ​{​str​(​amount​)​}​ ₽ на QIWI​\n​Счет действителен *10* минут​\n​\n​Номер: `+​{​phone​}​`​\n​Комментарий: `​{​billId​}​`​\n​\n​_Нажмите на реквизиты и комментарий чтобы их скопировать_'​, ​parse_mode​=​"Markdown"​, 
 ​                                ​reply_markup​=​inline_keyboard​) 
 ​                ​else​: 
 ​                        ​message​ ​=​ ​bot​.​send_message​(​call​.​message​.​chat​.​id​, ​f'💁🏻‍♀️ *Переведите* ​{​str​(​amount​)​}​ ₽ на QIWI​\n​Счет действителен *10* минут​\n​\n​Номер: `+​{​phone​}​`​\n​Комментарий: `​{​billId​}​`​\n​\n​_Нажмите на реквизиты и комментарий чтобы их скопировать_'​, ​parse_mode​=​"Markdown"​, 
 ​                                                        ​reply_markup​=​inline_keyboard​) 
  
 ​                ​in_deposit​.​append​(​str​(​call​.​message​.​chat​.​id​)) 
  
 ​                ​Thread​ ​=​ ​threading​.​Thread​(​target​ ​=​ ​deposit_timeout​, ​args​ ​=​ (​message​, ​merchant_id​, ​amount​, ​billId​)) 
 ​                ​Thread​.​start​() 
  
 ​        ​except​ ​Exception​ ​as​ ​e​: 
 ​                ​print​(​e​)
