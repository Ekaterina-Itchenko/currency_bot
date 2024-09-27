import asyncio
from typing import Any

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

from bot import start_router
from config import TELEGRAM_TOKEN


async def main() -> Any:
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    commands = [BotCommand(command="start", description="Старт/Start")]
    await bot.set_my_commands(commands=commands)

    dp.include_router(start_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
