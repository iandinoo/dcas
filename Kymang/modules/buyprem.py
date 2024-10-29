import os
import logging
import asyncio
import importlib

from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import *

@bot.on_callback_query(filters.regex("month1"))
async def month1(c: Bot, cb: CallbackQuery):
    await cb.edit_message_text(C10, reply_markup=KL10)

