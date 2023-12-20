import telebot


BOT_TOKEN = '6390291715:AAFlDCZ_0zAIaqU83NumckPb-k90k0bWtI8'


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello, my name is Daniel")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

