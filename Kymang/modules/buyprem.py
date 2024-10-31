from dateutil.relativedelta import relativedelta
from datetime import datetime
from Kymang import Bot, bot 
from pykeyboard import InlineKeyboard
from pyrogram import Client, filters
from pyrogram.types import *
from pytz import timezone
import datetime

now = datetime.datetime.now(timezone("Asia/Jakarta"))
expired = now + relativedelta(days=int(30))
DATE = expired.strftime("%d-%B-%Y")  

@bot.on_callback_query(filters.regex("month0"))
async def month0(c: Bot, cb: CallbackQuery):
    await cb.answer("Null", reply_markup=SATU_BULAN)

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
            InlineKeyboardButton("+1 Bulan", callback_data="month3"),
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

C20 = """
<b>🛒 Keranjang</b>
• Fsub Premium 3 Bulan

[•] <b>Tanggal Kadaluarsa:</b> {}

• <b>Harga: Rp.120.000</b>
• <b>Diskon: -Rp.10.000</b>
• <b>Total Harga: Rp.110.000</b>
"""

TIGA_BULAN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📅Bulan", callback_data="JK10"),
        ],
        [
            InlineKeyboardButton("-1 Bulan", callback_data="month2"),
            InlineKeyboardButton("+1 Bulan", callback_data="month4"),
        ],
        [
            InlineKeyboardButton("❌ Batalkan", callback_data="back_start"),
            InlineKeyboardButton("✅ Lanjutkan", callback_data="mulai"),
        ],
    ]
)

@bot.on_callback_query(filters.regex("month4"))
async def month4(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C20.format(DATE), reply_markup=TIGA_BULAN)
    
C25 = """
<b>🛒 Keranjang</b>
• Fsub Premium 4 Bulan

[•] <b>Tanggal Kadaluarsa:</b> {}

• <b>Harga: Rp.160.000</b>
• <b>Diskon: -Rp.15.000</b>
• <b>Total Harga: Rp.145.000</b>
"""

EMPAT_BULAN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📅Bulan", callback_data="JK10"),
        ],
        [
            InlineKeyboardButton("-1 Bulan", callback_data="month3"),
            InlineKeyboardButton("+1 Bulan", callback_data="month5"),
        ],
        [
            InlineKeyboardButton("❌ Batalkan", callback_data="back_start"),
            InlineKeyboardButton("✅ Lanjutkan", callback_data="mulai"),
        ],
    ]
)

@bot.on_callback_query(filters.regex("month4"))
async def month4(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C25.format(DATE), reply_markup=EMPAT_BULAN)

C30 = """
<b>🛒 Keranjang</b>
• Fsub Premium 5 Bulan

[•] <b>Tanggal Kadaluarsa:</b> {}

• <b>Harga: Rp.200.000</b>
• <b>Diskon: -Rp.20.000</b>
• <b>Total Harga: Rp.180.000</b>
"""

LIMA_BULAN = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📅Bulan", callback_data="JK10"),
        ],
        [
            InlineKeyboardButton("-1 Bulan", callback_data="month4"),
            InlineKeyboardButton("+1 Bulan", callback_data="month6"),
        ],
        [
            InlineKeyboardButton("❌ Batalkan", callback_data="back_start"),
            InlineKeyboardButton("✅ Lanjutkan", callback_data="mulai"),
        ],
    ]
)

@bot.on_callback_query(filters.regex("month5"))
async def month5(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C30.format(DATE), reply_markup=LIMA_BULAN)

