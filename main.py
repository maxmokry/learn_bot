from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename='bot.log')

def talk_to_me(bot, update):
    user_text = "Привет {}, ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s',
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)
    # print(update.message)
    update.message.reply_text(user_text)
    return

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    logging.info(update)
    update.message.reply_text(text)
    pass
    return

def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()