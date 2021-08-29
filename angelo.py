print("[INFO]: Importing Your BOT_TOKEN")
import re
import os
from asyncio import (gather, get_event_loop, sleep)

from aiohttp import ClientSession
from pyrogram import (Client, filters, idle)
from Python_ARQ import ARQ

from config import bot, BOT_TOKEN, ARQ_API_KEY, ARQ_API_BASE_URL, LANGUAGE
bot_token= BOT_TOKEN
is_config = os.path.exists("config.py")
print("[INFO]: Checking... Your BOT_TOKEN")

bot_id = int(bot_token.split(":")[0])
print("[INFO]: CODED BY ALBIN PRAVEEN")
arq = None

luna = Client(
    ":memory:",
    bot_token=bot_token,
    api_id=6,
    api_hash="d6e0095d9f089d956ec3c298ca0471ba",
)

bot_id = int(bot_token.split(":")[0])
arq = None

async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("Luna", "angelo")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "angelo")
    else:
        responsess = responsee
    if "Who is angelo?" in responsess:
        responsess2 = responsess.replace("Who is angelo?", "Heroine Of Telegram")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(filters.command("owner") & ~filters.edited)
async def repo(_, message):
    await message.reply_text(
        "[Owner](https://albinpraveen.ml)"
        + " | [Contact](t.me/i_am_albin_praveen)",
        disable_web_page_preview=True,
    )
    

@bot.on_message(filters.command("boss") & ~filters.edited)
async def repo(_, message):
    await message.reply_text(
        "[Owner](https://albinpraveen.ml)"
        + " | [Contact](t.me/i_am_albin_praveen)",
        disable_web_page_preview=True,
    )


@bot.on_message(filters.command("help") & ~filters.edited)
async def start(_, message):
    await bot.send_chat_action(message.chat.id, "typing")
    await sleep(2)
    await message.reply_text("/repo - Get Repo Link")



@bot.on_message(
    ~filters.private
    & filters.text
    & ~filters.command("start")
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}iris[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)

@bot.on_message(
    filters.private
    & ~filters.command("start")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        await message.reply_text("Ufff... Ignoring .... ¯\_(ツ)_/¯")
        return
    await type_and_send(message)


@bot.on_message(filters.command("start") & ~filters.edited)
async def startt(_, message):
    await message.reply_text("Hi, I'm Alive ╮(. ❛ ᴗ ❛.)╭ I am a AI chat bot made by ALBINPRAVEEN.You can chat with me .Learn more about the developer: https://albinpraveen.ml")


async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await bot.start()
    print(
        """
Your angelo Is Deployed Successfully.
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())
