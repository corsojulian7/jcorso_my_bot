from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Enable Logs
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#Init bot
updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Miau!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
