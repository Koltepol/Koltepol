import asyncio
from pytgcalls import idle
from Music import LOG_CHAT
from Music.Client.tgcalls import call_py, Bot, sex as abhi

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await Bot.start()
    await Bot.send_message(
                           LOG_CHAT,
                           "<b>Koltepol Bot Successfully Started!</b>"
    ), 

    print("[INFO]: STARTING PYTGCALLS CLIENT")

    await call_py.start()
    
    await abhi.send_message(
                            LOGGER,
                            "<b>Koltepol Assistant Successfully Started!</b>"
    ), 
    await abhi.join_chat("KoltepolSupport"), 
    await abhi.join_chat("KoltepolUpdate") 
    print("[INFO]: STOPPING BOT & USERBOT")    
    await Bot.stop()

await idle()
