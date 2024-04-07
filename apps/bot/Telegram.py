from telegram import Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters
)
from key_buttons import tele_button, create
from menu import main_menu_keyboard,  create_menu_keyboard

from blog import settings

TELEGRAM_TOKEN =settings.TELEGRAM_TOKEN

ABOUT = tele_button[0]
CREATE = tele_button[1]

POST = create[0]
LIKE = create[1]
COMMENT = create[2]
ACCOUNT = create[3]
CHAT = create[4]
BACK = create[5]



def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот поможет вам с вашими вопросами',
        reply_markup=main_menu_keyboard()
    )


def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'1. Запрещается вот это и вот это. блаблабалабабалаблаблабаалалаблабаблабалба'
    )

def reply_create(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Выбирайте',
        reply_markup=create_menu_keyboard()
    )

def create_post(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Чтобы сделать пост вам нужно......'
    )

def create_like(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Чтобы поставить лайк вам нужно......'
    )

def create_comment(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Чтобы оставить комментарий вам нужно......'
    )
def create_account(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Чтобы создать аккаунт вам нужно.......'
    )

def create_chat(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Чтобы создать свой чат вам нужно...........'
    )

def main_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Обратно в меню',
        reply_markup=main_menu_keyboard()
    )





updater = Updater(token=TELEGRAM_TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))



updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(POST),
    create_post
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LIKE),
    create_like
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COMMENT),
    create_comment
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ACCOUNT),
    create_account
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CHAT),
    create_chat
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    main_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CREATE),
    reply_create
))

updater.start_polling()
updater.idle()

