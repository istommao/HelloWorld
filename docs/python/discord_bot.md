---
title: Discord Bot
order: 10
nav:
  title: Python
  order: 1
group:
  title: 实战
  order: 1
---

```python
import asyncio
import discord
from discord.ext import commands


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(">>>>", message)
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

TOKEN = "your discord token"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


async def conn_handler(queue):
    print("conn_handler")


async def discord_bot(queue):
    print("bot start")
    await bot.start(TOKEN)

async def main():
    queue = asyncio.Queue()

    L = await asyncio.gather(
        discord_bot(queue),
        conn_handler(queue),
    )
    print(L)


asyncio.run(main())
```