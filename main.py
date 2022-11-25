from aiogram.utils import executor
import logging
from config import dp
from handlers import fsmAdminMentor, client, callback, admin, notification
from database.db import sql_create
import asyncio


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

notification.register_handlers_notification(dp)
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm_mentor(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
