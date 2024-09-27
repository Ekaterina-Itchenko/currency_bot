from aiogram.types import Message
from aiohttp import ClientSession
from bot.poviders import provide_api
from config import API_URL


async def greeting_handler(message: Message) -> None:
    greeting_message = "Добрый день! Как Вас зовут?"
    await message.answer(text=greeting_message)


async def currency_handler(message: Message) -> None:
    name = message.text
    async with ClientSession() as session:
        api_adapter = provide_api(api_url=API_URL, session=session)
        usd_exchange_rate = await api_adapter.get_currency_rate(
            currency="USD"
        )
    response = f"Рад знакомству, {name}! Курс доллара сегодня {usd_exchange_rate.rate} рублей."
    await message.answer(text=response)
