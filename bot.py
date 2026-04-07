
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import CommandStart
from image_gen import generate_image

BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: Message):
    await message.answer("Привет! 🎨\nОтправь мне любой текст — и я сгенерирую картинку по твоему описанию.")


@dp.message(F.text)
async def handle_message(message: Message):
    prompt = message.text
    await message.answer("⏳ Генерирую...")

    image_bytes = await asyncio.to_thread(generate_image, prompt)

    if image_bytes:
        await message.answer_photo(photo=BufferedInputFile(image_bytes, filename="image.jpg"))
    else:
        await message.answer("❌ Не удалось сгенерировать картинку, попробуй ещё раз")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
