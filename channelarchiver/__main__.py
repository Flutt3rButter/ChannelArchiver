import asyncio
from bot import ArchiveChannelBot
from config import BOT_TOKEN

if __name__ == "__main__":
    bot = ArchiveChannelBot()
    asyncio.run(bot.start(BOT_TOKEN))