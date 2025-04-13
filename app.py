from telegram.ext import Updater, CommandHandler

# Replace with your bot token
TOKEN = "7291462264:AAFb3_wycd2R3fi0TqAoVZxy_t8WLiTrEHE"

def start(update, context):
    update.message.reply_text("Namaskar! I am Krishi Bandhu – Green Pulse. How can I help you today?")

def help_command(update, context):
    update.message.reply_text("You can ask about crops, fertilizers, diseases, and more!")

# Set up the bot
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Add command handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))

# Start polling (keep Pyroid running!)
updater.start_polling()
updater.idle()
