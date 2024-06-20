import telebot
import telebot.types as types
import sqlite3


class CuteBot:
    def __init__(self, token: str):
        self.__db = sqlite3.connect('Users.db', check_same_thread=False)
        self.__cur = self.__db.cursor()
        self.__bot = telebot.TeleBot(token)

        self.__bot.polling(non_stop=True)


if __name__ == '__main__':
    CuteBot("6173436476:AAFhXIOzPvyk5e8CCamgN4t_-oV5ZaVaYto")
