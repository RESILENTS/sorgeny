​import​ ​telebot 
import​ ​requests 
​import​ ​json 
import​ ​sqlite3 
from​ ​telebot​ ​import​ ​types 
​from​ ​random​ ​import​ ​randint 
from​ ​config​ ​import​ ​token​,​otvetstart​,​idadmin​,​qiwinumber​,​token_qiwi​,​cena​,​oplatil​,​neoplatil 
  
  
 ​bot​=​telebot​.​TeleBot​(​token​) 
  
 ​@​bot​.​message_handler​(​commands​=​[​'start'​]) 
 ​def​ ​send_welcome​(​message​): 
 ​    ​bot​.​send_message​(​message​.​chat​.​id​, ​otvetstart​, ​reply_markup​=​btns​()) 
  
  
  
  
  
  
 ​@​bot​.​message_handler​(​content_types​=​"text"​) 
 ​def​ ​smsmms​(​message​): 
 ​    ​if​ ​message​.​text​ ​==​ ​"Купить доступ"​: 
 ​        ​con​ ​=​ ​sqlite3​.​connect​(​"data.db"​) 
 ​        ​cur​ ​=​ ​con​.​cursor​() 
 ​        ​comment​ ​=​ ​randint​(​10000​, ​9999999​) 
 ​        ​cur​.​execute​(​f"INSERT INTO oplata (id, code) VALUES(​{​message​.​chat​.​id​}​, ​{​comment​}​)"​) 
 ​        ​con​.​commit​() 
 ​        ​markup_inline​ ​=​ ​types​.​InlineKeyboardMarkup​() 
 ​        ​proverka​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Проверить оплату'​ ,​callback_data​=​'prov'​) 
 ​        ​otm​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Отмена'​ ,​callback_data​=​'ottm'​) 
 ​        ​markup_inline​.​add​(​proverka​) 
 ​        ​markup_inline​.​add​(​otm​) 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​,​f'♻️Переведите ​{​cena​}​₽ на счет Qiwi​\n​\n​Номер: `​{​qiwinumber​}​`​\n​Комментарий `​{​comment​}​` ​\n​ ​\n​Быстрая форма оплаты: [ОПЛАТА](https://qiwi.com/payment/form/99?extra%5B%27account%27%5D=​{​qiwinumber​}​&amountInteger=​{​cena​}​&amountFraction=0&currency=643&extra%5B%27comment%27%5D=​{​comment​}​)​\n​\n​_Нажмите на номер и комментарий, чтобы их скопировать_'​, 
 ​                                 ​parse_mode​=​'Markdown'​,​reply_markup​=​markup_inline​) 
 ​    ​else​: 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​,​"Нажмите на кнопку купить доступ для покупки."​) 
  
 ​         
  
 ​         
  
  
  
 ​@​bot​.​callback_query_handler​(​func​=​lambda​ ​call​:​True​) 
 ​def​ ​answer​(​call​): 
 ​     
 ​    ​con​ ​=​ ​sqlite3​.​connect​(​"data.db"​) 
 ​    ​cur​ ​=​ ​con​.​cursor​() 
 ​    ​if​ ​call​.​data​ ​==​ ​'prov'​: 
 ​         
 ​        ​user_id​ ​=​ ​call​.​message​.​chat​.​id 
 ​        ​QIWI_TOKEN​ ​=​ ​token_qiwi 
 ​        ​QIWI_ACCOUNT​ ​=​ ​str​(​qiwinumber​) 
 ​        ​s​ ​=​ ​requests​.​Session​() 
 ​        ​s​.​headers​[​'authorization'​] ​=​ ​'Bearer '​ ​+​ ​QIWI_TOKEN 
 ​        ​parameters​ ​=​ {​'rows'​: ​'50'​} 
 ​        ​h​ ​=​ ​s​.​get​(​'https://edge.qiwi.com/payment-history/v1/persons/'​ ​+​ ​QIWI_ACCOUNT​ ​+​ ​'/payments'​,​params​=​parameters​) 
 ​        ​req​ ​=​ ​json​.​loads​(​h​.​text​) 
 ​        ​try​: 
 ​             
 ​            ​cur​.​execute​(​f"SELECT * FROM oplata WHERE id = ​{​user_id​}​"​) 
 ​            ​result​ ​=​ ​cur​.​fetchone​() 
 ​            ​comment​ ​=​ ​str​(​result​[​1​]) 
 ​             
 ​            ​for​ ​x​ ​in​ ​range​(​len​(​req​[​'data'​])): 
 ​                ​if​ ​req​[​'data'​][​x​][​'comment'​] ​==​ ​comment​: 
 ​                    ​cena​ ​=​ (​req​[​'data'​][​x​][​'sum'​][​'amount'​]) 
 ​                    ​cur​.​execute​(​f"DELETE FROM oplata WHERE id = ​{​user_id​}​"​) 
 ​                    ​con​.​commit​() 
  
 ​                    ​bot​.​send_message​(​idadmin​,​f"💸Успешное пополнение💸"​) 
 ​                    ​bot​.​send_message​(​call​.​message​.​chat​.​id​,​oplatil​) 
  
 ​                     
 ​                    ​break 
 ​                ​else​: 
 ​                     
 ​                    ​bot​.​send_message​(​call​.​message​.​chat​.​id​,​neoplatil​) 
 ​                     
 ​                    ​break 
  
  
 ​        ​except​: 
 ​            ​pass 
  
 ​    ​elif​ ​call​.​data​ ​==​ ​'ottm'​: 
 ​        ​bot​.​send_message​(​call​.​message​.​chat​.​id​,​"Заказ отменен"​) 
 ​        ​cur​.​execute​(​f"DELETE FROM oplata WHERE id = ​{​call​.​message​.​chat​.​id​}​"​) 
 ​        ​con​.​commit​() 
  
 ​         
 ​    ​else​: 
 ​        ​pass 
  
 ​def​ ​btns​(): 
 ​    ​markup​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​) 
 ​    ​key1​ ​=​ ​types​.​KeyboardButton​(​"Купить доступ"​) 
 ​    ​markup​.​add​(​key1​) 
  
 ​    ​return​ ​markup 
  
  
 ​if​ ​__name__​ ​==​ ​'__main__'​: 
 ​    ​bot​.​polling​(​none_stop​=​True​)
