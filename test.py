import telebot

# Замените 'YOUR_API_TOKEN' на ваш реальный API токен, который вы получили от BotFather
API_TOKEN = "7322712668:AAGPuSMP0REGzWZ3xiUOThr59hvZwbjl9oU"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "этот бот лежит на локальном сервисе с автозапуском")


if __name__ == '__main__':
    bot.polling(none_stop=True)