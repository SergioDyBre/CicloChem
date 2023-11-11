#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import CommandHandler, ApplicationBuilder
    
print('Starting a bot....')
     
async def start_commmand(update, context):
    await update.message.reply_text('Hello! Welcome To Store!')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6763041623:AAH_s7vJ0iGR_dke-7UnAoeKDbxPH9vzkXY').build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))

    # Run bot
    application.run_polling(1.0)


#<3