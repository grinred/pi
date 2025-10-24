import telebot
import time

telegram_token = "7950838719:AAFu0qG0yh5xXxfCe5VfIuG0P0qz7eOl7oc"
bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=["start"])
def main(message):
    print(message)
    bot.send_message(message.chat.id, message.chat.username)


bot.infinity_polling()
