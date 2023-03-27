from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Let's START",
                         reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Start",
                                                                                      web_app=WebAppInfo(url="https://papasavage.github.io/"))))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
