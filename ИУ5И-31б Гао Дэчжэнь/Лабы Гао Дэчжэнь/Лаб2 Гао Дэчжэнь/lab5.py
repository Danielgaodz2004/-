"""
coding: utf-8
@Software: PyCharm
@Time:  3:29
@Author: Fake77
@Module Name:
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# 你的 Bot API Token
TOKEN = 'YOUR_BOT_TOKEN'


# 定义键盘布局
def create_keyboard():
    keyboard = [[InlineKeyboardButton("选项1", callback_data='option1')],
                [InlineKeyboardButton("选项2", callback_data='option2')],
                [InlineKeyboardButton("选项3", callback_data='option3')]]
    return InlineKeyboardMarkup(keyboard)


# 处理 /start 命令
def start(update, context):
    update.message.reply_text("欢迎！请选择一个选项：", reply_markup=create_keyboard())


# 处理按钮点击事件
def button(update, context):
    query = update.callback_query
    query.answer()  # 回应点击事件
    query.edit_message_text(text=f"你选择了: {query.data}")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()  # 开始轮询更新
    updater.idle()  # 阻塞直到用户中断程序（如按 Ctrl+C）


if __name__ == '__main__':
    main()