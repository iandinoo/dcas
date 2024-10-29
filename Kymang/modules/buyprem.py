import os
import logging
import asyncio
import importlib

from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import *

C10 = """
<b>🛒 Keranjang</b>
• <b>Order:</b> Force Sub

[•] <b>Tanggal Kadaluarsa:</b> {}

<b>Total Harga: Rp.40.000</b>
"""

now = datetime.datetime.now(timezone("Asia/Jakarta"))
expired = now + relativedelta(days=int(25))
DATE = expired.strftime("%d-%B-%Y")  

@bot.on_callback_query(filters.regex("month1"))
async def month1(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C10.format(DATE), reply_markup=KL10)

