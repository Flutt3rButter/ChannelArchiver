import os

BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
GUILD_ID = int(os.environ['DISCORD_GUILD_ID'])
MONTHS_THRESHOLD = int(os.environ.get('MONTHS_THRESHOLD', 6))
ARCHIVE_CATEGORY_NAME = os.environ.get('ARCHIVE_CATEGORY_NAME', 'Archive')
