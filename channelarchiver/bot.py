import discord
from datetime import datetime, timedelta, timezone
from .config import GUILD_ID, MONTHS_THRESHOLD, ARCHIVE_CATEGORY_NAME

class ArchiveChannelBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.messages = True
        super().__init__(intents=intents)

    async def on_ready(self):
        guild = self.get_guild(GUILD_ID)
        if not guild:
            print(f"Guild {GUILD_ID} not found")
            await self.close()
            return

        archive_category = await self.get_archive_category(guild)
        if not archive_category:
            print(f"Archive category {ARCHIVE_CATEGORY_NAME} not found")
            await self.close()
            return

        cutoff_date = datetime.now(timezone.utc) - timedelta(days=30 * MONTHS_THRESHOLD)
        archived_count = 0

        for channel in guild.text_channels:
            if channel.category and channel.category.name == ARCHIVE_CATEGORY_NAME:
                continue

            last_message = await self.get_last_message_date(channel)
            if last_message and last_message < cutoff_date:
                try:
                    await channel.edit(category=archive_category)
                    archived_count += 1
                    print(f"Archived: {channel.name}")
                except discord.Forbidden:
                    print(f"No permission to move: {channel.name}")

        print(f"Archived {archived_count} channels")
        await self.close()

    async def get_archive_category(self, guild):
        for category in guild.categories:
            if category.name == ARCHIVE_CATEGORY_NAME:
                return category
            return None

    async def get_last_message_date(self, channel):
        try:
            async for message in channel.history(limit=1):
                return message.created_at
            return None
        except discord.Forbidden:
            return None