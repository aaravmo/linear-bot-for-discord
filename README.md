# linear-bot-for-discord

A Discord bot that listens for urgent and high priority alerts in a Linear workspace and automatically sends reminders for these issues to the assigned worker at fixed intervals. 

# Usage

This program can be run 24/7 on a hosted server. Obtain a [webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for the discord channel with all Linear workers and obtain an [API Key](https://developers.linear.app/docs/graphql/working-with-the-graphql-api) for your Linear workspace. To run the program:


> $ python main.py --authorization:(YOUR_API_KEY) --webhookurl:(YOUR_WEBHOOK_URL) --scanfreq=10 --urgentfreq=6 --highfreq=15


**scanfreq**: How often (minutes) the program scans for new issues (default 10)

**urgentfreq**: How often (hours) reminders for urgent priority issues are sent to the discord channel (default 6)

**highfreq**: How often (hours) reminders for high priority issues are sent to the discord channel (default 15)
