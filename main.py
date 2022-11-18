from aiogram.utils import executor
import logging
import admin
import callback
import client
from setting import dp
import fsmAdminMentor

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm_mentor(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

