from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import logging

# Setup logging for debugging (optional)
logging.basicConfig(level=logging.INFO)

# Your Telegram user ID (replace with your actual ID)
OWNER_ID = 123456789  
PIN_KEYWORDS = ["Task:"]

# Create the bot
BOT_TOKEN = "7207998050:AAF-VBEQv7znDL1qJgv-zGbmbGF_gjwhv5w"

async def pin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    user_id = message.from_user.id
    text = message.text or ""

    # Check if message is from owner or contains keywords
    if user_id == OWNER_ID or any(keyword in text for keyword in PIN_KEYWORDS):
        try:
            await context.bot.pin_chat_message(
                chat_id=message.chat_id,
                message_id=message.message_id,
                disable_notification=True  # optional: don't notify group
            )
        except Exception as e:
            logging.warning(f"Failed to pin message: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), pin_handler)
    app.add_handler(message_handler)

    print("Bot is running...")
    app.run_polling() 
