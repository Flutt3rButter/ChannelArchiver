import asyncio
from bot import ArchiveChannelBot
from config import BOT_TOKEN

if __name__ == "__main__":
    bot = ArchiveChannelBot()
    bot.run(BOT_TOKEN, log_handler=None)