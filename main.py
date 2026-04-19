 import telebot

TOKEN = 8707019763:AAGxW6l8NkDmLnEMVRh8Nwosf7tOO-dT_wk

bot = bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Вітаю! Це твій бот для заробітку.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Ти написав: " + message.text)

print("Бот запущений...")
bot.polling(none_stop=True)
