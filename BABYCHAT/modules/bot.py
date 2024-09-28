from telegram.ext import Updater, MessageHandler, Filters

def auto_reaction(update, context):
    # Define the reaction (emoji, sticker, etc.)
    reaction = "👍"  # This can be any emoji or even a sticker file_id

    # Reply to the user with the reaction
    context.bot.send_message(chat_id=update.message.chat_id, text=reaction)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
    updater = Updater('7242058454:AAHd0UU2_-cKAc2FhDut0HS4ROcN8mLeF1E', use_context=True)
    dp = updater.dispatcher

    # Listen for all messages and react
    dp.add_handler(MessageHandler(Filters.text, auto_reaction))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
