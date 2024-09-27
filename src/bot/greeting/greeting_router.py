from aiogram import F, Router
from aiogram.types import Message
from bot.greeting.greeting_handler import greeting_handler, currency_handler


start_router = Router()


@start_router.message(F.text == "/start")
async def route_greeting_handler(msg: Message) -> None:
    await greeting_handler(msg)


@start_router.message()
async def route_currency_handler(msg: Message) -> None:
    await currency_handler(msg)
