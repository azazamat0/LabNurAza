import telebot
TOKEN = '7070202629:AAFQcYBicTkBmuzuhk7pyViV0LTkgR3E9RM'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Hello!")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
 bot.reply_to(message, message.text)
if __name__ == '__main__':
 bot.infinity_polling()