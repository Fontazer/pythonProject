# 1 шаг -   pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler,Callbackcontaxt,filters
from telegram.ext import update

def start(update=Update,contaxt = callbackcontext):
    update.message.reply_text("Hi bro")



def echo(update=Update,contaxt = callbackcontext):
    update.message.reply_text(update.message.text) # бот пересылает сообщение пользователя



def main():
    updater  = Updater("# - тут должен быть вписан токен доступа ")
    dispatcher=updater.dipatcher
    dispatcher.add_handler(commandhandler("start",statr()))
    dispatcher.add_handler(Messagehandler(filters.text & ~filters.command, echo))
    updater.start_polling()
    updater.idle()


main()