import requests
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7115257666:AAHCW6ieacA4XTTogf4Gq8EXtOPxXrYA3Fw"

dp = Dispatcher()

menu_keyboard = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton("Стар", callback_data="start")
button2 = InlineKeyboardButton("Все репозитории", callback_data="get_all")
menu_keyboard.add(button1, button2)

@dp.message(CommandStart())
async def command_start_hadler(message: Message) -> None:
    await message.answer("Привет, здесь ты можешь получить все репозитории Hrpl")

@dp.message(Command("get_all"))
async def get_all_repository(message: Message) -> None:
    repositories = requests.get('https://api.github.com/users/Hrpl/repos').json()
    response = ""
    for repository in repositories:
        response += f"Репозиторий [{repository['name']}]({repository['html_url']}), \n"

    await message.answer(response, parse_mode='Markdown')


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())