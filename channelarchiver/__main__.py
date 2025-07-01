import asyncio
from .bot import ChannelArchiveBot
from .config import BOT_TOKEN

if __name__ == "__main__":
    bot = ChannelArchiveBot()
    asyncio.run(bot.start(BOT_TOKEN))