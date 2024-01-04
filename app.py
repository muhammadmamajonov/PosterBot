import asyncio
from loader import bot
from config import CHAT_ID

async def post_and_delete():
    msg =  await bot.send_message(chat_id=CHAT_ID, text="Salom test")
    await bot.delete_message(chat_id=CHAT_ID, message_id=msg.message_id)


if __name__ == "__main__":
    asyncio.run(post_and_delete())