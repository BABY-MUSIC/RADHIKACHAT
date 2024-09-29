from telegram.ext import Application, MessageHandler, filters

async def auto_reaction(update, context):
    # Define the reaction (emoji, sticker, etc.)
    reaction = "👍"  # You can use other emoji or stickers

    # Reply to the user with the reaction
    await context.bot.send_message(chat_id=update.message.chat_id, text=reaction)

async def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
    application = Application.builder().token('7242058454:AAHd0UU2_-cKAc2FhDut0HS4ROcN8mLeF1E').build()

    # Add a handler for text messages to trigger auto-reaction
    application.add_handler(MessageHandler(filters.TEXT, auto_reaction))

    # Start the bot
    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
