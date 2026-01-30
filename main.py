from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.environ.get("TOKEN")  # Set this in Railway

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Welcome to FlySaver Bot ✈️")

def track(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 3:
        update.message.reply_text("Usage: /track FROM TO YYYY-MM-DD")
        return
    from_city, to_city, date = args
    price = 320  # Placeholder
    update.message.reply_text(f"Tracking flight {from_city} → {to_city} on {date}. Current price: £{price}")

updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("track", track))

updater.start_polling()
updater.idle()
