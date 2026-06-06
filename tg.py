from config import *
from telebot import TeleBot
import sqlite3
from config import DB_Manager 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
import csv
import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name

bot = TeleBot("8179173631:AAEEw5Y3E2QbxC6ruyj21BrnsRAoXWW_PBk")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Привет! Я бот по игре майнкрафт чтобы ты мог узнать харакеристики брони элитр оружию феерверкам""")

   


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, '''/help показывает все команды и их смысл,
                     /minecraft чтобы узнать характеристики всего и вся по оружию броне и т. д.
                      ''')
    
@bot.message_handler(commands=['minecraft'])
def send_minecraft(message):

    markup = types.InlineKeyboardMarkup()
    
    callback_button = types.InlineKeyboardButton(text="open", callback_data="minecraft.db")
    markup.add(callback_button)
    bot.send_message(message.chat.id, "Привет! Выберите действие:", reply_markup=markup)

# Обработчик нажатия на кнопку с callback_data
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "test_action":
        bot.answer_callback_query(call.id, "Кнопка нажата!")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы нажали на кнопку!")

    db_manager_class = "minecraft.db"

def connect_db():
    conn = sqlite3.connect('minecraft.db')
    return conn.cursor()

@bot.message_handler(commands=['minecraft'])
async def minecraft_command(message):
    bot.send_message(message.chat.id, connect_db())


    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.polling(none_stop=True)
    bot.infinity_polling()