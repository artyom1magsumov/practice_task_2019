import telebot
import database_commands
import sqlite3

token = '866968772:AAHjcONtmxgqh91Z11ASL6lYIbiEV5bD9fs'
bot = telebot.TeleBot(token)

db = sqlite3.connect('Users.sqlite', check_same_thread=False)
cursor = db.cursor()

keyboard = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)

keyboard.add('Rate person1')
keyboard.add('Show results')
keyboard.add('Show stats')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, what do you want to do?',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Show stats':
        stats = database_commands.get_stats_list(cursor)
        stats_values = database_commands.get_stat_value(cursor)
        mess = ''
        for stat in stats:
            mess += f'{stat[0]} - {stat[1]}\n'
        bot.send_message(message.chat.id, mess, reply_markup=keyboard)
    elif message.text == 'Rate person1':
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        stats = database_commands.get_stats_list(cursor)
        for stat in stats:
            keyboard1.add(telebot.types.InlineKeyboardButton(text=stat[1], callback_data=f'a%{stat[0]}'))
            print(stat[1])
        bot.send_message(message.chat.id, "Choose the stat", reply_markup=keyboard1)
        if message.text == 'Speed' or 'Correctness' or 'Performance':
            markup1 = telebot.types.InlineKeyboardMarkup()
            markup1.add(telebot.types.InlineKeyboardButton(
                text='1', callback_data=mess))
            markup1.add(telebot.types.InlineKeyboardButton(
                text='2', callback_data=mess))
            markup1.add(telebot.types.InlineKeyboardButton(
                text='3', callback_data=mess))
            bot.send_message(message.chat.id, 'Choose the mark',
                             reply_markup=markup)
            if message.text == '1':
                database_commands.get_state(message.chat.id, cursor)
                database_commands.set_state(message.chat.id, 2, cursor, db)
                database_commands.add_stat_value(message.chat.id, message.text, cursor, db)
            elif message.text == '2':
                database_commands.get_state(message.chat.id, cursor)
                database_commands.set_state(message.chat.id, 2, cursor, db)
                database_commands.add_stat_value(message.chat.id, message.text, cursor, db)
            elif message.text == '3':
                database_commands.get_state(message.chat.id, cursor)
                database_commands.set_state(message.chat.id, 2, cursor, db)
                database_commands.add_stat_value(message.chat.id, message.text, cursor, db)
            else:
                database_commands.get_state(message.chat.id, cursor)
                database_commands.set_state(message.chat.id, 1, cursor, db)
        else:
            database_commands.get_state(message.chat.id, cursor)
            database_commands.set_state(message.chat.id, 1, cursor, db)

    elif database_commands.get_state(message.chat.id, cursor) == 1:
        database_commands.set_state(message.chat.id, 2, cursor, db)
        database_commands.insert_name_of_user(message.chat.id, message.text, cursor, db)
        bot.send_message(message.chat.id, "Your name is" + message.text +
                         " you rated stat of person1 for " + database_commands.get_name_stat(message.chat.id, cursor) + " mark "
                         + + database_commands.get_stat_value(message.chat.id, cursor))
    else:
        bot.send_message(message.chat.id, '!!!')


@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
    if call.data.split('%')[0] == "a":
        database_commands.add_stat_value(call.message.chat.id, call.data.split('%')[1], cursor, db)
        database_commands.insert_name_stat(call.data.split('%')[1], cursor, db)
        database_commands.set_state(call.message.chat.id, 1, cursor, db)
        bot.send_message(call.message.chat.id, 'You rated '
                         + database_commands.get_name_stat_from_user(call.message.chat.id, cursor) + '.')



bot.polling()