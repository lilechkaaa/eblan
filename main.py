import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, executor, Dispatcher, types


load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ["token"])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("ваня соси бибу\n"
                        "https://github.com/lilechkaaa/eblan\n"
                        "питон лучше вашей пососной джавы")


@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    msg = message.text.lower()
    if msg == "да":
        await message.reply("пизда")
    elif msg == "нет":
        await message.reply("пидора ответ")
    elif msg == "привет":
        await message.reply("иди нахуй")
    elif msg == "лева" or msg == "лев":
        await message.reply("даун")
    else:
        await message.reply("че это за хуйня")


if __name__ == "__main__":
    executor.start_polling(dp)
