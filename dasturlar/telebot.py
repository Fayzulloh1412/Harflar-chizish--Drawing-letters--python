import telebot
from transliterate import to_cyrillic as toc, to_latin as tol

BOT_TOKEN = '7069644322:AAGVbbbS-k0UJienAvbPQJch8Fyo8eCelJg'

bot = telebot.TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f'Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!'
    xabar += '\nMatningizni yuboring.'
    bot.reply_to(message, xabar)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu aleykum, xush kelibsiz. Bu botni Fayzulloh_aka degan mashhur inson yaratgan")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if message.isascii():
        bot.reply_to(message, toc(message.text))
    else:
        bot.reply_to(message, tol(message.text))


        
bot.polling()

