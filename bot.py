from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from timezones import create_image_timeline, generate_time_display

async def times(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = generate_time_display()
    await update.message.reply_text(message, parse_mode='MarkdownV2')
async def timesImage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the image
    img_bytes = create_image_timeline()
    # Send as photo
    await update.message.reply_photo(img_bytes)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Use /times to see the time zones comparison.')

def main():
    # Get token from environment variable, not hardcoded
    token = os.environ.get('BOT_TOKEN')
    # Replace with your bot token
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("times", times))
    app.add_handler(CommandHandler("timesImage", timesImage))
    app.run_polling()

if __name__ == '__main__':
    main() 
