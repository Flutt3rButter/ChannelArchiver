# Channel Archiver

Simple Python script that moves Discord channels with no activity in the last N months to a specified category.

## Discord Bot

Create a Discord bot and give it these permissions
- Manage Channels
- Read Message History

## Setup

1. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   export DISCORD_BOT_TOKEN="your_bot_token"
   export DISCORD_GUILD_ID="your_server_id"
   export MONTHS_THRESHOLD="6"  # optional, defaults to 6
   export ARCHIVE_CATEGORY_NAME="Archive"  # optional, defaults to "Archive"
   ```

4. Run the script:
   ```bash
   python discord_archiver.py
   ```

The script runs once and exits.
To run it periodically you can create a cron job.