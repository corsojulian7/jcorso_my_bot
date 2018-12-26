from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import paho.mqtt.publish as publish
import os

#Enable Logs
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#Init bot
updater = Updater(token=os.getenv('TOKEN'))
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Miau!")

def mqtth(bot, update):
    auth = {'username':os.getenv('MQTT_USER'), 'password':os.getenv('MQTT_PASSWORD')}
    publish.single(topic='esp/test', payload=update.message.text[6:], qos=0, hostname='m15.cloudmqtt.com', port=12048, client_id='TelegramBot', auth=auth)
    bot.send_message(chat_id=update.message.chat_id, text='Publicado correctamente')

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

mqtt_handler = CommandHandler('mqtt', mqtth)
dispatcher.add_handler(mqtt_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
