"""
coding: utf-8
@Software: PyCharm
@Time:  3:25
@Author: Fake77
@Module Name:
"""
import telebot


class TelegramBot:
    STATE_IDLE = 0
    STATE_ACTIVE = 1
    STATE_PAUSED = 2

    def __init__(self):
        # 自己去找token
        self.state = self.STATE_IDLE

    def update_state(self, new_state):
        # 可以在这里添加状态转换的逻辑
        self.state = new_state

    def handle_message(self, message):
        # 根据当前状态处理消息
        if self.state == self.STATE_IDLE:
            # 处理空闲状态下的消息
            return '???'
        elif self.state == self.STATE_ACTIVE:
            # 处理活动状态下的消息
            try:
                hello = {'what\'s your name?': 'Daniel',
                'where are you?': 'I\'m in telegram','Do you want to work?': 'No.Fuck you'}
                return hello[message]
            except:

                return 'Hay bro'
        else:
            # 处理暂停状态下的消息
            return 'Have a good day!'


    def start_reply(self):
        self.state = self.STATE_ACTIVE

    def stop_reply(self):
        self.state = self.STATE_PAUSED

    def idle_reply(self):
        self.state = self.STATE_IDLE


if __name__ == '__main__':
    BOT_TOKEN = '6390291715:AAFlDCZ_0zAIaqU83NumckPb-k90k0bWtI8'
    bot = telebot.TeleBot(BOT_TOKEN)
    tgbot = TelegramBot()


    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        tgbot.start_reply()
        bot.reply_to(message, tgbot.handle_message(message))


    @bot.message_handler(commands=['bye'])
    def send_pause(message):
        tgbot.stop_reply()
        bot.reply_to(message, tgbot.handle_message(message.text))


    @bot.message_handler(commands=['tuzi'])
    def send_tuzi(message):
        tgbot.idle_reply()
        bot.reply_to(message, tgbot.handle_message(message.text))

    @bot.message_handler(func=lambda msg: True)
    def common_echo(message):
        bot.reply_to(message, tgbot.handle_message(message.text))
    bot.infinity_polling()
