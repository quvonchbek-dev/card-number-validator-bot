from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
import asyncio
from validator import validate_credit_card, format_number, extract_card_num

bot = Bot("6353520619:AAG_cEw60h0nLQByk6emDALVaj2nGA7kgVo", parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(msg: Message):
    await msg.answer(
        "👋 Привет, добро пожаловать. Отправьте номер каждой карты в отдельной строке. "
        "Вы можете отправить столько строк, сколько хотите. Например:\n\n"
        "<code>1234 5678 9012 3456\n4254-5478-9012-3756\n4244.5488.9012.3556</code>")


@dp.message_handler(content_types=["text"])
async def text_message(msg: Message):
    new_msg = await bot.send_message(msg.chat.id, "⌛ Сейчас проверяю...")
    txt = msg.text
    x, y = 0, 0
    h = ''
    z = ""
    clocks = "🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦"

    for i, card in enumerate(txt.split("\n")):
        card = await extract_card_num(card)
        if not len(card):
            continue
        try:
            valid = await validate_credit_card(card)
            x += valid
            y += not valid
            fm = await format_number(card)
            s = f"{'✅' if valid else '🚫'} {fm}\n"
            h += s
            z += s
            # await new_msg.edit_text(h + "\n" + clocks[i % 24] + " проверка...")
            # await asyncio.sleep(0.1)
        except Exception as e:
            await bot.send_message(msg.chat.id, f"⚠ Произошла ошибка в строке {i + 1}: <code>{e}</code>")
            # pass
    await new_msg.edit_text("☑ Результаты\n\n" + z)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
