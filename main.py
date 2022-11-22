from aiogram.utils import executor
import logging
import admin
import callback
import client
from config import dp
import fsmAdminMentor
from database.db import sql_create

async def on_startup(_):
    sql_create()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm_mentor(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
