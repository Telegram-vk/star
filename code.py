from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import threading

TELEGRAM_BOT_TOKEN = '6184145071:AAGk-c7IIrDb7nVhZO1lgZwdqdupJH52EQ0'

def get_welcome_message(user_name):
    return f"""? Info ? 
Hey {user_name}! This bot will work with you only once, for free. To start, send /show ?? ??"""

SUPPORTED_SOCIAL_MEDIA_DOMAINS = ["facebook.com", "instagram.com", "snapchat.com", "twitter.com"]

def send_additional_message(chat_id: int, message_text: str) -> None:
    updater.bot.send_message(chat_id=chat_id, text=message_text)

def start(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.first_name
    user_id = update.message.from_user.id

    with open('/home/crespo/Desktop/ip.txt', 'r') as file:
        existing_ids = file.readlines()

    if f"{user_id}\n" in existing_ids:
        update.message.reply_text("??You can not use the bot again. You must subscribe now to use it. Contact us on Instagram: @s_aher01.")
        return

    with open('/home/crespo/Desktop/ip.txt', 'a') as file:
        file.write(f"{user_id}\n")

    update.message.reply_text(get_welcome_message(user_name))

def show(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send the victim's link for social media account ?? ?")

def handle_email_or_link(update: Update, context: CallbackContext) -> None:
    user_response = update.message.text.lower()
    user_name = update.message.from_user.first_name

    if any(domain in user_response for domain in SUPPORTED_SOCIAL_MEDIA_DOMAINS):
        update.message.reply_text(f"? Please wait, {user_name}, until the information to log in to the account is sent to you within 60 min. For more features, contact us on @DoomAi1bot")

        threading.Timer(120.0, send_additional_message, args=[update.message.chat_id, """?This is the password for the account (@@black-**). Use the username, or in the case of Facebook, use the account IP and password through Google Chrome because it does not save basic logins, so the victim will not know that his account has been hacked.

? Reminder, the last letters of the password have been encrypted, and this is for subscription reasons"""]).start()
    else:
        update.message.reply_text("Invalid link or email. Make sure to provide a valid social media link or email.")

def main() -> None:
    global updater
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("show", show))
    dp.add_handler(MessageHandler(Filters.regex(r"(http|@).+\.com"), handle_email_or_link))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
