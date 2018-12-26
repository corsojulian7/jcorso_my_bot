from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import paho.mqtt.client as mqtt
import os

#Enable Logs
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#Init MQTT Client
client = mqtt.Client("TelegramBot")
client.username_pw_set(os.getenv('MQTT_USER'), password=os.getenv('MQTT_PASSWORD'))
client.connect('m15.cloudmqtt.com', port=12048)

#Init bot
updater = Updater(token=os.getenv('TOKEN'))
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Miau!")

def mqtth(bot, update):
    cmds = update.message.text.split(' ')
    rta = 'Error en la publicacion'
    if len(cmds) == 3:
        client.publish(cmds[1],cmds[2])
        rta = 'Publicado correctamente'
    else:
        rta = 'Parametros incorrectos'
    bot.send_message(chat_id=update.message.chat_id, text=rta)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

mqtt_handler = CommandHandler('mqtt', mqtth)
dispatcher.add_handler(mqtt_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
