

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackContext
   
)
from config import BOT_TOKEN
from database import add_user, user_exists

async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    if not user_exists(user.id):
        add_user(user.id, user.username, user.first_name, user.last_name)
        await update.message.reply_text('You have been registered!')
    else:
        await update.message.reply_text('You are already registered.')

def main():
    # updater = Updater(BOT_TOKEN)
    # dispatcher = updater.dispatcher

    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))

    # updater.start_polling()
    # updater.idle()
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
