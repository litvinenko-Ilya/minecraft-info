from config import *
from telebot import TeleBot
import sqlite3
from config import DB_Manager 

bot = TeleBot("8683561535:AAFPPpzIbtK2xVQ_oYWmh8fVMX-6q0yrK30")


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот по игре майнкрафт чтобы ты мог узнать харакеристики брони элитр оружию феерверкам
зарядам ветра и т. д. напиши /help чтобы узнать все команды!) 
""")
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, '''/help показывает все команды и их смысл,
                     /minecraft чтобы узнать характеристики всего и вся по оружию броне и т. д.
                     /opartament аникдот с кс''')
    
def connect_db():
    conn = sqlite3.connect('minecraft.db')
    return conn.cursor()

@bot.message_handler(commands=['minecraft'])
async def minecraft_command(message):
    bot.send_massege(connect_db())

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,'''1 спашиват 2 где бамба 1 отвечает сзади 2 начинает крутиться прошёл 24 часа говорит нету 1 говорит время мы проиграли''')
    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()