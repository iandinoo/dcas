import os
import logging
import asyncio
import importlib

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import *
from pytz import timezone

now = datetime.datetime.now(timezone("Asia/Jakarta"))
expired = now + relativedelta(days=int(30))
DATE = expired.strftime("%d-%B-%Y")  

C10 = """
<b>🛒 Keranjang</b>
• <b>Order:</b> Force Sub

[•] <b>Tanggal Kadaluarsa:</b> {}

<b>Total Harga: Rp.40.000</b>
"""

@bot.on_callback_query(filters.regex("month1"))
async def month1(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C10.format(DATE), reply_markup=KL10)

