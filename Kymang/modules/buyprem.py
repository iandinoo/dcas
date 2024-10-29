from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import *
from pytz import timezone

now = datetime.datetime.now(timezone("Asia/Jakarta"))
expired = now + relativedelta(days=int(30))
DATE = expired.strftime("%d-%B-%Y")  

@bot.on_callback_query(filters.regex("month0"))
async def month0(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text("Null", reply_markup=SATU_BULAN)

C10 = """
<b>🛒 Keranjang</b>
• Fsub Premium 1 Bulan

[•] <b>Tanggal Kadaluarsa:</b> {}

• <b>Harga: Rp.40.000</b>
• <b>Total Harga: Rp.40.000</b>
"""

SATU_BULAN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📅Bulan", callback_data="JK10"),
        ],
        [
            InlineKeyboardButton("-1 Bulan", callback_data="month0"),
            InlineKeyboardButton("+1 Bulan", callback_data="month2"),
        ],
        [
            InlineKeyboardButton("❌ Batalkan", callback_data="back_start"),
            InlineKeyboardButton("✅ Lanjutkan", callback_data="mulai"),
        ],
    ]
)

@bot.on_callback_query(filters.regex("month1"))
async def month1(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C10.format(DATE), reply_markup=SATU_BULAN)
    
C15 = """
<b>🛒 Keranjang</b>
• Fsub Premium 2 Bulan

[•] <b>Tanggal Kadaluarsa:</b> {}

• <b>Harga: Rp.80.000</b>
• <b>Diskon: -Rp.5.000</b>
• <b>Total Harga: Rp.75.000</b>
"""

DUA_BULAN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📅Bulan", callback_data="JK10"),
        ],
        [
            InlineKeyboardButton("-1 Bulan", callback_data="month1"),
            InlineKeyboardButton("+1 Bulan", callback_data="month2"),
        ],
        [
            InlineKeyboardButton("❌ Batalkan", callback_data="back_start"),
            InlineKeyboardButton("✅ Lanjutkan", callback_data="mulai"),
        ],
    ]
)

@bot.on_callback_query(filters.regex("month2"))
async def month2(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C15.format(DATE), reply_markup=DUA_BULAN)
