import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, executor, Dispatcher, types


load_dotenv()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ["token"])
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def send_text(message: types.Message):
    if message.text.lower() == "да":
        await message.reply("пизда")
    elif message.text.lower() == "нет":
        await message.reply("пидора ответ")
    elif message.text.lower() == "привет":
        await message.reply("иди нахуй")
    else:
        await message.reply("че это за хуйня")


if __name__ == "__main__":
    executor.start_polling(dp)