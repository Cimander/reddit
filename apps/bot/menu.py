import telegram
from key_buttons import tele_button, create


def main_menu_keyboard():
    keyboard  = ([
        [telegram.KeyboardButton(tele_button[0]),],
        [telegram.KeyboardButton(tele_button[1]),],

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def create_menu_keyboard():
    keyboard  = ([
        [telegram.KeyboardButton(create[0]),],
        [telegram.KeyboardButton(create[1]),],
        [telegram.KeyboardButton(create[2]),],
        [telegram.KeyboardButton(create[3]),],
        [telegram.KeyboardButton(create[4]),],
        [telegram.KeyboardButton(create[5]), ],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )